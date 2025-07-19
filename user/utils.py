# utils.py

import random
from twilio.rest import Client
from django.conf import settings

def generate_otp():
    return str(random.randint(1000, 9999))

def send_otp(mobile_number, otp):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f'Your OTP code is {otp}. Do not share with anyone',
        from_=settings.TWILIO_PHONE_NUMBER,
        to=mobile_number
    )
    return message.sid  # Indentation corrected here
