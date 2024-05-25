from django.http import HttpResponse
import stripe
import time
from .models import Booking

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        print(pid)
        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        billing_details = stripe_charge.billing_details
        metadata = stripe_charge.metadata
        # metadata = intent.metadata
        grand_total=self.request.session.get('grand_total',0)
        print("inside the webhook")
        print(metadata)
        booking_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                booking = Booking.objects.get(
                    name = billing_details.name,
                    email = billing_details.email,
                    mobile = billing_details.phone,
                    country = billing_details.address.country,
                    eir_code = billing_details.address.postal_code,
                    town = billing_details.address.city,
                    address_1 = billing_details.address.line1,
                    address_2 =billing_details.address.line2,
                    county = billing_details.address.state,
                    grand_total = grand_total,
                    stripe_pid = pid,
                )
                booking_exists = True
                break
            except Booking.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if booking_exists:
            self._send_confirmation_email(booking)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified booking already in database',
                status=200)
        else:
            booking = None
            try:
                title_id = billing_details.title
                county_id = billing_details.address.state
                booking = Booking.objects.create(
                    title = get_object_or_404(Title, pk=title_id),
                    name = billing_details.name,
                    email = billing_details.email,
                    mobile = billing_details.phone,
                    country = billing_details.address.country,
                    date_of_birth = intent.metadata.date_of_birth,
                    eir_code = billing_details.address.postal_code,
                    town = billing_details.address.city,
                    address_1 = billing_details.address.line1,
                    address_2 = billing_details.address.line2,
                    county = get_object_or_404(County, pk=county_id) if county_id else None,
                    licence_number = intent.metadata.licence_number,
                    licence_expiry = intent.metadata.licence_expiry,
                    personal_id = intent.metadata.personal_id,
                    id_number = intent.metadata.id_number,
                    country_issued = intent.metadata.country_issued,
                    id_expiry = intent.metadata.id_expiry,
                    
                    car_id = request.session.get('car_id'),
                    pick_up_city = request.session.get('pick_up_city'),
                    pick_up_county = request.session.get('pick_up_county'),
                    drop_off_city = request.session.get('drop_off_city'),
                    drop_off_county = request.session.get('drop_off_county'),
                    pick_up_date = request.session.get('pick_up_date'),
                    drop_off_date = request.session.get('drop_off_date'),
                    pick_up_time = request.session.get('pick_up_time'),
                    drop_off_time = request.session.get('drop_off_time'),
                    booster_seat = request.session.get('booster_quantity', 0),
                    child_seat = request.session.get('childseat_quantity', 0),
                    infant_car_capsule = request.session.get('infant_quantity', 0),

                    booster_total = request.session.get('booster_total', 0),
                    childseat_total = request.session.get('childseat_total', 0),
                    infant_total = request.session.get('infant_total', 0),
                    total_rent = request.session.get('total_rent', 0),
                    grand_total = request.session.get('grand_total', 0),
                    days = request.session.get('days', 0),
                    hours = request.session.get('hours', 0),
                    stripe_pid=pid,
                )
            except Exception as e:
                if booking:
                    booking.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created Booking in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)