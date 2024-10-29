"""Handles alert operations"""

from email.message import EmailMessage
import smtplib

import trackourse.const_config as cc


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
    sender_email = cc.settings["sender_email"]
    email_password = cc.settings["sender_password"]
    number = cc.settings["phone_number"]
    provider = cc.settings["carrier"]

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
    to_email = cc.settings["target_email"]
    from_email = cc.settings["sender_email"]
    password = cc.settings["sender_password"]

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
    return f"""Course seat opened!
        Course ID: {course["ID"]}
        Instructors: {course["Professors"]}
        Days: {course["Days"]}
        Start: {course["Start time"]}
        End: {course["End time"]}
        """


def construct_email(course_list):
    """Constructs format for email notifications
    Args:
        course_list: list of course info dictionaries

    Returns:
        str: formatted email body
    """
    body = ""
    for course in course_list:
        body += f"""{construct_sms(course)}

        """

    return body


def send_alerts(course_list):
    """Handles alerts with the differences list
    Args:
        course_list: list - List of courses that are open with the most recent update
    """
    if not course_list:
        pass
    else:
        match cc.notif_method:
            case "sms" | "both":
                for course in course_list:
                    send_sms(construct_sms(course))
            case "email" | "both":
                send_email(construct_email(course_list))
            case _:
                raise ValueError(
                    "Invalid notif_method in course_config.py, use 'sms', 'email' or 'both'"
                )
