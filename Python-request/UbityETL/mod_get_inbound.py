import requests
import os
import datetime
import time

def getinboundfiles():
    username = "nmanseau@distech-controls.com"
    password = "ubity2015"

    root = "https://studio.ubity.com"
    s = requests.Session()

    login_r = s.post(root + "/login_handler",
                     data={'login': username, 'password': password})


    data = {'dis0003': ['dis0003-CustomerService', 'dis0003-Support',
                          'dis0003-FieldDevices'],
              'dis0006': ['dis0006-Reception', 'dis0006-Serviceclientanglais',
                          'dis0006-Serviceclientfrancais',
                          'dis0006-Supporttechniqueanglais',
                          'dis0006-Supporttechniquefrancais']}


    for accountcode, queues in data.items():
        stats_url = root + "/switch_to/" + accountcode

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
                root, queue, int(from_ts), int(to_ts))

            url_access = s.get(url).text.encode('utf-8').decode('utf-8')
            sections = []
            section = []
            for line in url_access.split('\n'):
                if line:
                    section.append(line)
                else:
                    sections.append(section)
                    section = []
            if section:
                sections.append(section)
            for i, section in enumerate(sections):
                open(os.path.join("file", "%s-%d.csv" % (queue, i + 1)),
                     "wb").write('\n'.join(section).encode('utf-8'))
