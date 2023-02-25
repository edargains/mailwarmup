# -*- coding: utf-8 -*-

import random
import time
from datetime import datetime

from Mail import sd_mail


def main():
    while True:
        date_and_time = datetime.now()
        date_and_time = date_and_time.strftime('%d/%m/%Y %H:%M:%S')
        sd_mail.send(date_and_time)
        time.sleep(random.randint(10, 40))


if __name__ == '__main__':
    main()
