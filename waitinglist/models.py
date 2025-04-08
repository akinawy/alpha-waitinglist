from django.db import models

class WaitingUser(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('AR', 'Arabic'),
    ]

    email = models.EmailField(unique=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

class PDFDownloadUser(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('AR', 'Arabic'),
    ]
    email = models.EmailField(unique=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

