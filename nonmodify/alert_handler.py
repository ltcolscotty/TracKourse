"""Handles alert operations"""

import os
from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib

from nonmodify.class_info import class_info as ci

# Load environment variables from .env file
load_dotenv()


def send_sms(
    message: str,
    subject: str = "TracKourseASU",
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
        print("SMS alert sent successfully")
    except Exception as e:
        print(f"Failed to send SMS: {str(e)}")


def send_email(body, subject, is_html=False):
    """Sends email to configured email address
    Args:
        body: body of email content
        subject: title
        is_html: body type
    """
    to_email = os.getenv("TARGET_EMAIL")
    from_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("SENDER_PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    if is_html:
        msg.set_content(body, subtype="html")
    else:
        msg.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(from_email, password)
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


def construct_sms(course):
    """Creates SMS message for one class
    Args:
        course: dict - dictionary for course info

    Returns:
        str: formatted text message
    """
    return (
        f"""Course seat opened!
        Course ID: {course["ID"]}
        Instructors: {course["Professors"]}
        Days: {course["Days"]}
        Start: {course["Start_time"]}
        End: {course["End_time"]}
        """
    )
