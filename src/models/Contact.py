from django.db import models


class Contact(models.Model):
    fullname = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    subject = models.CharField(max_length=255, null=True)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
