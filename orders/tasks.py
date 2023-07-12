from celery import shared_task
from django.core.mail import send_mail
from .models import Order

# The shared_task decorator is used to define a Celery task.
# This is a decorator that transforms the order_created function into a Celery task. 
# It allows the function to be executed asynchronously by Celery.

@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order no. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
                f'You have successfully placed an order.' \
                f'Your order ID is {order.id}.'
    
    mail_sent = send_mail(subject,
                message,
                'admin@myshop.com',
                [order.email])
    return mail_sent

# send_mail() function provided by Django to send an email notification to the user
# This line uses the send_mail function to send an email. 
# It takes the subject, message, sender email address, and recipient(s) as arguments