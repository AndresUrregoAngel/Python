
numbers =[] #List
for number in range(10):
    numbers.append(number)
#numbers.insert(3,8)
#numbers.remove(8)
counter = 1 # starting counter for "while"
while (counter <= 5):
    print("Hola Owen")
    print (counter)
    counter +=1 # counter = counter  + 1

grade = []

grade_prametter = input("provide grade starting point")

file_family = open("E:\\Sources\\family_grades.txt","r") # read a file
save_file = open("E:\\Sources\\output.txt","w") # write file

next(file_family) # skipe the file headers

for line in file_family:
    grade_unit = line.split(',')
    print("the student name is :" ,
           grade_unit[0],"and his grade was: ",grade_unit[1])
    grade.append(grade_unit[1])

counter = False # original value in counter before start the loop while/ boolean variable
while (counter != True): # while runs until counter will be true
    factor = 2
    for item in grade:
        if (item >= grade_prametter):
            new_score = int(item) + factor
            save_file.write(str(new_score)) # write in a file
            print("the value: ",new_score, "is saved it in the file")


    print("the program is over")

    counter = True

#Examples for Tuples

exa = [] # List
New_tuple = (1,2) #Tuple
New_tupleb = (2,2)
result = New_tuple + New_tupleb
print(result)
print(len(result))






