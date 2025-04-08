from django.core.mail import send_mail


def send_email(email):
    send_mail(
        subject='Welcome to the Waitlist!',
        message='Thanks for joining! We’ll notify you when we go live.',
        from_email='your_email@yourdomain.com',
        recipient_list=['user@example.com'],
        fail_silently=False,
    )