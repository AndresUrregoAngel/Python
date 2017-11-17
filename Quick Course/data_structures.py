# _*_ coding:utf-8 _*_

'''The examples below gives main insights
about how to deal with data structures'''

## Lists

information =[]

data = input('store the first value in the list')
information.append(data)
print("adding data:",information)

data = input('add a new value in the list')
information.insert(1,data)
print('inserting data:',information)

print('#'*10,'adding numbers to a list','#'*10)

for number in range(1,10):
    information.append(number)

print('print after add numbers:',information)

information.remove('owen')

print('print after a remove:',information)
information.remove('andres')

information.sort()
print('print with sort',information)
information.reverse()
print('print list reversed:',information)

information.clear()
print('print after clear the list',information)

for number in range(20,30):
    information.append(number)


for number in information:
    if (number > 25):
        print('the numbers greater than 25 are:',number)
    else:
        print('the number less than 25 are:',number)
