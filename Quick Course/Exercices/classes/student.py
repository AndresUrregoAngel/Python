
class Subject:
    def __init__(self,name):
        self.name = name
        self.grade = None
    def __str__(self):
        return ('{},{}'.format(str(self.name),int(self.grade)))

    def add_grade(self,grade):
        self.grade = grade





class student:
    def __init__(self,gender,age,name):
        self.gender=gender
        self.age=age
        self.name=name
        self.subject = {}

    def __str__(self):
       return ('{},{},{}'.format(str(self.gender),int(self.age),str(self.name)))

    def add_subject (self, name):
        self.subject[name] = Subject(name)

    def add_grade_student(self, subject_name,grade):
        subject = self.subject[subject_name]
        subject.add_grade(grade)





new = student('M',25,'Fabio')
new.add_subject('maths')
new.add_subject('science')
new.add_grade_student('maths',5)
new.add_grade_student('science',5)


f = 'maths'
print(new)
for c,v in new.subject.items():
    if (c == f):
        print(v)