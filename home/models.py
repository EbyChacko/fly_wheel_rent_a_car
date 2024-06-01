from django.db import models

# model fo the customer message from the contact.html
class CustomerMessage(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MailChimpMails(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
