"""
file = open("E:\\Sources\\Salaries\\rawdata.csv","r")
values = []
for i in file:
    line = i.split(",")
    values.append(int(line[19]))

sum = 0
for i in values:
    sum += i

print(sum)



files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}


def group_by_owners(files):
    dic = {}
    for k,v in files.items():
        if( v in dic.keys()):
            key = v
            dic.setdefault(key, []).append(k)
        else:
            key = v
            dic.setdefault(key, []).append(k)



    return dic

print(group_by_owners(files))

"""
x = range(6)
y =[0]*len(x)
print(y)



"""
def is_palindrome(word):
    answer = ''
    if (word.lower()  == word.lower()[::-1]):
        #print('True')
        answer = 'True'
    else:
        #print('False')
        answer = 'False'
    return answer




print(is_palindrome('Deleveled'))
"""
