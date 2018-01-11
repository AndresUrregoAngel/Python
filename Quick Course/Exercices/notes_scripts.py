

grades = []

with open('E:\\Sources\\student.txt') as file:
   next(file)
   for item in file:
        line = item.split(',')
        f = (line[3]+','+line[4]+','+line[5]+','+line[6]+','+line[7]+','+line[8]+','+line[9].replace('\n',''))
        grades.append(f)


reports = {}
number_report = range(11)


for report in number_report:
    reports[report] = grades[report]

for k,v in reports.items():
        print(k,v)
'''

with open('E:\\Sources\\student.txt') as file:
    next(file,None)
    for i in file:
        item = i.split(',')
        for report in number_report:
            reports[report] = item


    for k,v in reports.items():
        print(v)

'''