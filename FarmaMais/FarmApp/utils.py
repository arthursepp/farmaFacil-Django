import secrets
from django.core.mail import EmailMessage
from django.conf import settings

def generate_hex_code():
    """Gera um código hexadecimal aleatório de 6 caracteres."""
    return secrets.token_hex(3)

def send_verification_email(email, code):
    """Envia um e-mail de verificação para o usuário."""
    subject = 'Seu Código de Verificação'
    message = f'Seu código de verificação é: {code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    
    email = EmailMessage(subject, message, email_from, recipient_list)
    email.send()