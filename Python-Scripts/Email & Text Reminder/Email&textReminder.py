import smtplib
from email.message import EmailMessage


def email_reminder(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "shreyashsurvey12@gmail.com"  #sender's email address
    msg['from'] = user
    password = " "  #Generated app password in " "

    server = smtplib.SMTP("smtp.gmail.com")
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


if __name__ == "__main__":
    email_reminder("Hey", "Hey There!,This is a Email Reminder",
                   "shreyashmohadikar@gmail.com")
    # format -->(Subject, Body, reciever's email address)

# for text message reminder use the following:

# if __name__ == "__main__":
#     email_reminder("Hey","This is a Email Reminder","number@airtelkk.com")

#here, replace 'number' with your 10 digit mobile number
