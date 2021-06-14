import smtplib
import email.mime.multipart as mp
import email.mime.text as t
from getdata import *

MAIL_PATH = get_mailpath()
REC_PATH = get_recpath()
SERVER, PORT, SENDER_ADDR, PASSWORD = get_metadata()
SUBJECT, TEXT = get_email(MAIL_PATH)
MAILING_LIST = get_receivers(REC_PATH)


# TEST_LIST = ['random_email']

def create_connection():
    try:
        server = smtplib.SMTP(host=SERVER, port=PORT)
        server.login(SENDER_ADDR, PASSWORD)
        return server
    except Exception:
        print("Failed to login to server")


def send(server, receiver, message):
    try:
        server.sendmail(SENDER_ADDR, receiver, message)
        print("Message sent to %s" % receiver)
    except Exception:
        print("\n-----------> Message sending to %s failed <-----------\n" % receiver)


def send_group_mail():
    server = create_connection()
    if server:
        print(server)
        print("Connection to server succeeded! \n\n")
        for obj in MAILING_LIST:
            message = mp.MIMEMultipart()
            message['From'] = SENDER_ADDR
            message['To'] = obj
            message['Subject'] = SUBJECT
            message.attach(t.MIMEText(TEXT, 'plain'))
            text = message.as_string()
            send(server, obj, text)

    else:
        print("Connection error :(\n")

# send_group_mail()
