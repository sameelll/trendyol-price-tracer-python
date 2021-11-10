# Mail server imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(to_mail, subject, content):
    
    # mail sender
    from_mail = "mail_sender@mail.com"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # It sends email to the upper floor
    server.starttls()
    # Server login
    server.login(from_mail, "sender_password")
    # To send the email with an html page
    message = MIMEMultipart('alternative')
    message['Subject']= subject

    html_content = MIMEText(content, 'html')
    message.attach(html_content)

    server.sendmail(
        from_mail,
        to_mail,   
        message.as_string()
    )
    print("email has been sent successfully!")
    server.quit()


