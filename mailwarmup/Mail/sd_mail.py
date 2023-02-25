import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

from dotenv import load_dotenv


def send(date):
    """Função para enviar emails.

    Args:
        date (string): Data e Hora do dia.
    """
    load_dotenv()
    _from = os.getenv('SD_FROM')
    _from = list(_from.split(', '))
    _to = os.getenv('SD_TO')
    _to = list(_to.split(', '))
    _server = os.getenv('SMTP_SERVER')
    _port = os.getenv('SMTP_PORT')
    _pwd = os.getenv('SMTP_PWD')

    for sd_from in _from:
        msg = MIMEMultipart()
        msg['From'] = sd_from
        msg['To'] = ', '.join(_to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = f'Relatório de Envios {date}'

        body = f'Segue Relatório de Envios {date}. \n\nAt.te, \nInfraestrutura COGECT'
        msg.attach(MIMEText(body, 'plain'))

        s = smtplib.SMTP(_server, _port)
        s.starttls()
        s.login(sd_from, _pwd)
        text = msg.as_string()
        s.sendmail(sd_from, _to, text)
        s.quit()
