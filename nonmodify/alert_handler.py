"""Handles alert operations"""

import os
from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib

# Load environment variables from .env file
load_dotenv()


def send_sms(
    message: str,
    subject: str = "NotifyRegisterASU Notification",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 587,
):
    """Sends sms
    Args:
        message: str - message to send
        subject: str - subject if there is any
        smtp_server: str - keep as smtp.gmail.com, don't mess with this
        smtp_port: - port, don't mess with this
    """
    # Environment variable stuff
    sender_email = os.getenv("SENDER_EMAIL")
    email_password = os.getenv("SENDER_PASSWORD")
    number = os.getenv("PHONE_NUMBER")
    provider = os.getenv("CARRIER")

    # Check for missing config values
    if not all([sender_email, email_password, number, provider]):
        raise ValueError("Missing required environment variables")

    # Carrier gateway dictionary
    carriers = {
        "att": "txt.att.net",
        "tmobile": "tmomail.net",
        "verizon": "vtext.com",
        "sprint": "messaging.sprintpcs.com",
        "boost": "sms.myboostmobile.com",
        "cricket": "sms.cricketwireless.net",
        "uscellular": "email.uscc.net",
        "virgin": "vmobl.com",
    }

    if provider.lower() not in carriers:
        raise ValueError(f"Invalid carrier: {provider}")

    to_email = f"{number}@{carriers[provider.lower()]}"

    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(sender_email, email_password)
            smtp.send_message(msg)
        print("SMS sent successfully")
    except Exception as e:
        print(f"Failed to send SMS: {str(e)}")


send_sms(
    message="Hello from Python!",
)


def send_mail():
    """Should take formatted aggregated data and send to inbox."""
    pass
