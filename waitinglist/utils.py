from django.core.mail import send_mail


def send_email(email_address, reason, language):
    send_mail(
        subject='Welcome to the Waitlist!',
        message='Thanks for joining! We’ll notify you when we go live.',
        from_email='info@alalphahealth.com',
        recipient_list=[email_address],
        fail_silently=False,
    )