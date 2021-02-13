from celery import shared_task 
from django.core import mail 
from django.core.mail import message, send_mail
from .models import Order

@shared_task
def order_created(order_id):
    """
    Task to send an email notification 
    when an order is successfully created
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.firt_name}.\n\n'\
              f'Your have a successfully place an order.'\
              f'Your order ID is {order.id}'
    mail_sent = send_mail(subject,
                          message,
                          'admin@boryn_shop.com',
                          [order.id])
    return mail_sent