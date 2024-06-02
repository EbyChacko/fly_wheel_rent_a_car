from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Booking

@receiver(post_save, sender=Booking)
def send_booking_confirmation(sender, instance, created, **kwargs):
    if created:
        # Booking was just created
        subject = 'Booking Confirmation - FlyWheel Rent a Car'
        from_email = 'noreply@flywheelrentacar.com'
        to_email = instance.email
        
        context = {
            'booking': instance,
        }
        
        text_content = render_to_string('emails/booking_confirmation.txt', context)
        html_content = render_to_string('emails/booking_confirmation.html', context)
        
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()