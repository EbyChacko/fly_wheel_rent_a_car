from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Booking

@receiver(post_save, sender=Booking)
def send_booking_confirmation(sender, instance, created, **kwargs):
    if created:
        subject = 'Booking Confirmation - FlyWheel Rent a Car'
        from_email = 'flywheelrent@gmail.com'
        to_email = instance.email
        
        context = {
            'booking': instance,
            'name':instance.name,
            'booking_number':instance.booking_number,
            'make':instance.car.make,
            'model':instance.car.model,
            'category':instance.car.category,
            'pick_up_city':instance.pick_up_city,
            'pick_up_county':instance.pick_up_county,
            'pick_up_date':instance.pick_up_date,
            'pick_up_time':instance.pick_up_time,
            'drop_off_city':instance.drop_off_city,
            'drop_off_county':instance.drop_off_county,
            'drop_off_date':instance.drop_off_date,
            'drop_off_time':instance.drop_off_time,
            'grand_total':instance.grand_total,
        }
        
        text_content = render_to_string('emails/booking_confirmation.txt', context)
        html_content = render_to_string('emails/booking_confirmation.html', context)
        
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()