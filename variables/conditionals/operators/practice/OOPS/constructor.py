# all classes have a function called init function,is always executed when class is being initiated.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in database")
s1=Student("tushar",98)
print(s1.name,s1.marks)
s2=Student("vivek",97)
print(s2.name,s2.marks)