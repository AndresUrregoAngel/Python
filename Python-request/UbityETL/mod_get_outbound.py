#!/usr/bin/python

import os
#import urllib
#import urllib2
#import cookielib
import datetime
import requests


def getoutboundfiles():
    # Here are your accounts (canada and france)
    ACCOUNTS = ['dis0003', 'dis0006']

    # Your admin login and password
    username = "nmanseau@distech-controls.com"
    password = "ubity2015"

    root = "https://studio.ubity.com"
    s = requests.Session()

    login_r = s.post(root + "/login_handler",
                     data={'login': username, 'password': password})



    now = datetime.datetime.now()
    year = now.year
    month = now.month



    for accountcode in ACCOUNTS:
        stats_url = root + "/switch_to/" + accountcode
       # print(stats_url)
       # req = urllib2.Request(ROOT + "/switch_to/" + accountcode)
       # opener.open(req)
        # Get the cdr

        url = root + "/cdr_api/csv/cdrs-%d-%02d-outgoing.csv" % (year,month)
        #print(url)
        url_access = s.get(url).text.encode('utf-8')
        #    url = ROOT + "/cdr_api/csv/cdrs-%d-%02d-outgoing.csv" % (year, month)
         #   req = urllib2.Request(url)
          #  csv = opener.open(req).read()
        open(os.path.join("file", "outgoing-%s-%s-%02d.csv" % (accountcode, year, month)), "wb").write(url_access)


