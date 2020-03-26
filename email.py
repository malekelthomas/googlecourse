from email.message import EmailMessage
import os.path
import smtplib
import mimetypes
import getpass


def generate_email(sender, receiver, title, body, attachment):
  message = EmailMessage()
  message["From"] = sender
  message["To"] = receiver
  message["Subject"] = title
  message.set_content(body)
  attachment_filename = os.path.basename(attachment)
  mime_type, _ = mimetypes.guess_type(attachment)
  mime_type, mime_subtype = mime_type.split('/', 1)

  with open(attachment, 'rb') as a:
    message.add_attachment(a.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=attachment_filename))

  return message


def send_email(message):
  mail_server = smtplib.SMTP('localhost')
  mail_pass = getpass.getpass()
  mail_server.login(sender, mail_pass)
  mail_server.send_message(message)
  mail_server.quit



