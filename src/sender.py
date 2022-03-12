#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 


import os
import pprint
#import pdb; pdb.set_trace()

#from colored import fg, bg, attr
from dotenv import load_dotenv
from datetime import datetime
import time

from Mail import sd_mail

def main():
    i = 0
    while true:
        date_and_time = datetime.now()
        date_and_time = date_and_time.strftime('%d/%m/%Y %Hh%Mmin')
        sd_mail.send(date_and_time)
        i += 1
        time.sleep(300)

if __name__ == "__main__":
	load_dotenv()
	main()
