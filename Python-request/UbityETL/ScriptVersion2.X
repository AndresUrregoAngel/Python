#!/usr/bin/env python

import os
import time
import urllib
import urllib2
import cookielib
import datetime

# Here are your queue names
QUEUES = {'dis0003': ['dis0003-CustomerService', 'dis0003-Support',
                      'dis0003-FieldDevices'],
          'dis0006': ['dis0006-Reception', 'dis0006-Serviceclientanglais',
                      'dis0006-Serviceclientfrancais',
                      'dis0006-Supporttechniqueanglais',
                      'dis0006-Supporttechniquefrancais']}


# Your admin login and password
LOGIN = "xxx"
PASSWORD = "xxx"
ROOT = "https://studio.ubity.com"


# The client have to take care of the cookies.
jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))

# POST login query on '/login_handler' (post data are: 'login' and 'password').
req = urllib2.Request(ROOT + "/login_handler",
                      urllib.urlencode({'login': LOGIN,
                                        'password': PASSWORD}))
opener.open(req)


# Set the right accountcode

for accountcode, queues in QUEUES.items():
    req = urllib2.Request(ROOT + "/switch_to/" + accountcode)
    opener.open(req)

    NOW = datetime.datetime.now()
    YEAR = NOW.year
    FROM_MONTH = NOW.month
    TO_MONTH = NOW.month
    FROM_DAY = NOW.day
    TO_DAY = NOW.day

    from_ts = time.mktime(datetime.datetime(
        YEAR, FROM_MONTH, FROM_DAY).timetuple())
    to_ts = time.mktime(datetime.datetime(
        YEAR, TO_MONTH, TO_DAY).timetuple())

    # Get the CSV and write it to files
    for queue in queues:
        url = "%s/queue/csv/stats/%s/%s/%s" % (
            ROOT, queue, int(from_ts), int(to_ts))
        sections = []
        section = []
        for line in opener.open(urllib2.Request(url)).read().split('\n'):
            if line:
                section.append(line)
            else:
                sections.append(section)
                section = []
        if section:
            sections.append(section)
        for i, section in enumerate(sections):
            open(os.path.join("file", "%s-%d.csv" % (queue, i + 1)),
                 "wb").write('\n'.join(section))
