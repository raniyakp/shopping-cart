from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def mailing(emailid, user_name, order_id):
    send_mail(
            'Order placed successfully',
            f'Hi {user_name},\n\
Your order with order no. {order_id} has been successfully placed. Thank you for shopping with us.',
            settings.EMAIL_HOST_USER,
            [emailid],
            fail_silently=False,
        )