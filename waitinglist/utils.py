from django.core.mail import send_mail


def send_email(email_address, reason, language, score=None):
    if score:
        message = f"your score is {score}"
    else:
        message = 'Thanks for joining! We’ll notify you when we go live.'
    send_mail(
        subject='Welcome to the Waitlist!',
        message=message,
        from_email='info@alalphahealth.com',
        recipient_list=[email_address],
        fail_silently=False,
    )