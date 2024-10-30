import trackourse.nonmodify.alert_handler as ah
import trackourse.const_config as cc


def ping():
    """Tests notification methods"""
    match cc.notif_method:
        case "sms":
            ah.send_sms("SMS Ping Test Success", "TracKourseASU")
        case "email":
            ah.send_email("Email Ping Test Success", "TracKourseASU")
        case "both":
            ah.send_email("Email Ping Test Success", "TracKourseASU")
            ah.send_sms("SMS Ping Test Success", "TracKourseASU")


if __name__ == "__main__":
    ping()
