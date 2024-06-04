from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from checkout.models import Booking

import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Booking)
def send_booking_cancelation_email(sender, instance, created, **kwargs):
    if instance.status == 'Canceled':
        logger.info(f'Booking cancellation email triggered for booking: {instance.booking_number}')
        subject = _('Booking Cancellation - FlyWheel Rent a Car')
        from_email = settings.EMAIL_HOST_USER
        to_email = instance.email
        
        context = {
            'booking': instance,
            'name': instance.name,
            'booking_number': instance.booking_number,
            'company_email': from_email,
            'company_contact_number': '0892336291',
        }
        
        text_content = render_to_string('emails/booking_cancellation.txt', context)
        html_content = render_to_string('emails/booking_cancellation.html', context)
        
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
