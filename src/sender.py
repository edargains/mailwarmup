#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import pprint
import random

from dotenv import load_dotenv
from datetime import datetime
import time

from Mail import sd_mail

def main():
    while True:
        date_and_time = datetime.now()
        date_and_time = date_and_time.strftime('%d/%m/%Y %H:%M:%S')
        sd_mail.send(date_and_time)
        time.sleep(random.randint(65,120))

if __name__ == "__main__":
        load_dotenv()
        main()
