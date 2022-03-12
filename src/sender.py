#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 


import os
import pprint
#import pdb; pdb.set_trace()

#from colored import fg, bg, attr
from dotenv import load_dotenv
from datetime import datetime

from Mail import sd_mail

def main():
    date_and_time = datetime.now()
    date_and_time = date_and_time.strftime('%d/%m/%Y %H:%M')
    sd_mail.send(date_and_time)

if __name__ == "__main__":
	load_dotenv()
	main()
