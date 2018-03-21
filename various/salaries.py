file = open("E:\\Sources\\Salaries\\rawdata.csv","r")
values = []
for i in file:
    line = i.split(",")
    values.append(int(line[19]))

sum = 0
for i in values:
    sum += i

print(sum)