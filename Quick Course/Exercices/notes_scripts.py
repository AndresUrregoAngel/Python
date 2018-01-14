

grades = []

with open('E:\\Sources\\student.txt') as file:
   next(file)
   for item in file:
        line = item.split(',')
        f = (line[3].strip()+','+line[4].strip()+','+line[5].strip()+','+line[6]+','+line[7]+','+line[8]+','+line[9].replace('\n',''))
        grades.append(f)


reports = {}
number_report = range(11)
results = []


for report in number_report:
    reports[report] = grades[report]

for k,v in reports.items():
       while (k == 0 ):
           for i in v:
               grade = i.strip().split('\n')
               if (grade > 3):
                print(grade)
           k+=1
