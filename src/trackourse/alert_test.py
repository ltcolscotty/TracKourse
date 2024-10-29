import trackourse.nonmodify.alert_handler as ah
import trackourse.const_config as cc


def ping():
    match cc.notif_method:
        case "sms":
            ah.send_sms("SMS Ping Test Success", "NotifyRegisterASU")
        case "email":
            ah.send_email("Email Ping Test Success", "NotifyRegisterASU")
        case "both":
            ah.send_email("Email Ping Test Success", "NotifyRegisterASU")
            ah.send_sms("SMS Ping Test Success", "NotifyRegisterASU")


if __name__ == "__main__":
    ping()
