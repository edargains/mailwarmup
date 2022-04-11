import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


def send(date):
    _from = os.getenv('SD_FROM')
    _to = os.getenv('SD_TO')
    #_to2 = ['erickdargains@hotmail.com', 'erickmedrado@hotmail.com', 'pmf202204@outlook.com']
    _to = list(_to.split(', '))
    #print(_to)
    #print(_to2)
    exit
    _server = os.getenv('SMTP_SERVER')
    _port = os.getenv('SMTP_PORT')
    _pwd = os.getenv('SMTP_PWD')

    msg = MIMEMultipart()
    msg['From'] = _from
    msg['To'] = ", ".join(_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = f'Relatório de Envios WIN {date}'

    body = f'Segue Relatório WIN de Envios {date}. \n\nAt.te, \nInfraestrutura COGECT'
    msg.attach(MIMEText(body, 'plain'))

    s = smtplib.SMTP(_server, _port)
    s.starttls()
    s.login(_from, _pwd)
    text = msg.as_string()
    s.sendmail(_from, _to, text)
    s.quit()