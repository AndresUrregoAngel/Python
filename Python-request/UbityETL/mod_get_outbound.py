#!/usr/bin/python

import os
#import urllib
#import urllib2
#import cookielib
import datetime
import requests


def getoutboundfiles(accountcode):
    # Here are your accounts (canada and france)
    #ACCOUNTS = ['dis0003', 'dis0006']
    # Your admin login and password
    username = "xxxx"
    password = "xxx"
    root = "https://studio.ubity.com"
    s = requests.Session()

    login_r = s.post(root + "/login_handler",
                     data={'login': username, 'password': password})

    now = datetime.datetime.now()
    year = now.year
    month = now.month

    stats_url = root + "/switch_to/" + accountcode
    url = root + "/cdr_api/csv/cdrs-%d-%02d-outgoing.csv" % (year,month)
    url_access = s.get(url).text.encode('utf-8')
    open("C:\\Batches\\UbityETL\\file\\outgoing-%s-%s-%02d.csv" % (accountcode, year, month), "wb").write(url_access)



