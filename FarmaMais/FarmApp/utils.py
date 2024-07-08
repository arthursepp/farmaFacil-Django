import uuid
from django.core.mail import send_mail

def generate_hex_code():
    return uuid.uuid4().hex

def send_verification_email(email, code):
    subject = 'Verificação de Cadastro'
    message = f'Seu código de verificação é: {code}'
    email_from = 'noreply@seuprojeto.com'
    recipient_list = [email,]
    send_mail(subject, message, email_from, recipient_list)