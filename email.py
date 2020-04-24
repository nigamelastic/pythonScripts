import smtplib, ssl

def sendmail():
    port = 587 
    smtp_server = "smtp.gmail.com"
    sender_email = "teraemail@gmail.com"
    receiver_email = "tera hi mail :P@gmail.com"
    password = input("Type your password and press enter:")
    message = """\
    Subject: slots available

    wangoo pe slots available he bhai."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)