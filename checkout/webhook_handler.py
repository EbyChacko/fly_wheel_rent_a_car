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

        # Get the Charge object
        # stripe_charge = stripe.Charge.retrieve(
        #     intent.latest_charge
        # )
        # billing_details = stripe_charge.billing_details
        # metadata = stripe_charge.metadata
        metadata = intent.metadata
        grand_total=self.request.session.get('grand_total',0)
        print("inside the webhook")
        print(metadata)
        print(mobile)
        booking_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                booking = Booking.objects.get(
                    name__iexact = metadata.get('name', ''),
                    email__iexact = metadata.get('email', ''),
                    mobile__iexact = metadata.get('mobile', ''),
                    country__iexact = metadata.get('country', ''),
                    eir_code__iexact = metadata.get('eir_code', ''),
                    town__iexact = metadata.get('town', ''),
                    address_1__iexact = metadata.get('address_1', ''),
                    address_2__iexact = metadata.get('address_2', ''),
                    county__iexact = metadata.get('county', ''),
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
                booking = Booking.objects.create(
                    title = metadata.get('title', ''),
                    name = metadata.get('name', ''),
                    email = metadata.get('email', ''),
                    mobile = metadata.get('mobile', ''),
                    country = metadata.get('country', ''),
                    date_of_birth = metadata.get('date_of_birth', ''),
                    eir_code = metadata.get('eir_code', ''),
                    town = metadata.get('town', ''),
                    address_1 = metadata.get('address_1', ''),
                    address_2 = metadata.get('address_2', ''),
                    county = metadata.get('county', ''),
                    licence_number = metadata.get('licence_number', ''),
                    licence_expiry = metadata.get('licence_expiry', ''),
                    personal_id = metadata.get('personal_id', ''),
                    id_number = metadata.get('id_number', ''),
                    country_issued = metadata.get('country_issued', ''),
                    id_expiry = metadata.get('id_expiry', ''),
                    
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