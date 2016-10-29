import smtplib
import email.mime.multipart as mp
import email.mime.text as t

SERVER = "mail.fonis.rs"
PORT = 25
SENDER_ADDR = "office@fonis.rs"
PASSWORD = "nemakazne.42"
SUBJECT = "Obavestenje o narednom krugu selekcije - HAKATON"
TEXT = """\
Poštovane kolege,

Zbog mnogobrojnih molbi koje ste nam uputili odlučili smo da poslednji krug selekcije - mini hakaton odložimo sa termina planiranog za nedelju 30. oktobar na jedan od radnih dana u toku naredne nedelje. Tačne informacije o rezultatima trećeg kruga selekcije i novom terminu hakatona za one kandidate koji se na njega budu plasirali dobićete početkom naredne nedelje.

Želimo sreću svim kolegama koji u nedelju polažu prvi kolokvijum iz Programiranja 2!

Pozdrav,
Vaš FONIS
"""

MAILING_LIST = []
TEST_LIST = ['kostadinovic995@gmail.com', 'sara.94.po@gmail.com', 'mjelenabg@gmail.com']


def get_recievers(path):
    with open(path, 'r') as recievers:
        recs = recievers.read()
        recs = recs.splitlines()
        return recs


MAILING_LIST = get_recievers("recievers.txt")


def create_connection():
    try:
        server = smtplib.SMTP(host=SERVER, port=PORT)
        server.login(SENDER_ADDR, PASSWORD)
        return server
    except Exception:
        print("Neuspesan login na server")


def send(server, reciever, message):
    try:
        server.sendmail(SENDER_ADDR, reciever, message)
        print("Message sent to %s" % reciever)
    except Exception:
        print("\n-----------> Message sending to %s failed <-----------\n" % reciever)


def send_group_mail():
    server = create_connection()
    if server:
        print(server)
        print("Uspesno konektovan na server\n\n")
        for obj in MAILING_LIST:
            message = mp.MIMEMultipart()
            message['From'] = SENDER_ADDR
            message['To'] = obj
            message['Subject'] = SUBJECT
            message.attach(t.MIMEText(TEXT, 'plain'))
            text = message.as_string()
            send(server, obj, text)
        """
        for test in TEST_LIST:
            message = mp.MIMEMultipart()
            message['From'] = SENDER_ADDR
            message['To'] = test
            message['Subject'] = SUBJECT
            message.attach(t.MIMEText(TEXT, 'plain'))
            text = message.as_string()
            send(server, test, text)
        """
    else:
        print("Greska pri konektovanju na server\n")


send_group_mail()
