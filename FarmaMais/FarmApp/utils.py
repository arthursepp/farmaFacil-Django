import uuid
from django.core.mail import send_mail as django_send_mail
import random

def gerar_codigo():
    codigo = random.randint(0x1000, 0xFFFF)

    codigo = format(codigo, '04X')

    print(codigo)
    return codigo

codigo = gerar_codigo()

def send_verification(codigo):
    django_send_mail(
        'Código de verificação',
        f'Seu código de verificação é: {codigo}',
        'arthursouzasepp@gmail.com',
        ['to@example.com'],
        fail_silently=False,
    )

send_verification(codigo)
