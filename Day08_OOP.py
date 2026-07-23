# ==========================================
# DAY 1 - OOP
# Class and objects 
class Student:
    name = "Mansi"  # CREATING CLASS
S1 = Student()      # CREATING OBJECTS
print(S1.name)

# __init Function
class Student:      # CREATING CLASS  
    def __init__(self,fullname):
        self.name = fullname   
S1 = Student("Karan")      # CREATING OBJECTS
print(S1.name)

class Student:      # CREATING CLASS  
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks   
S1 = Student("Karan",97)      # CREATING OBJECTS
print(S1.name)
print(S1.marks)

# Class & instance Attributes

class Student:
    college_name = "ABC college"
    name = "anonymous"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
print("adding new student in the database..")   

S1 = Student("Karan",97)
print(S1.name)
print(Student.college_name)

# METHODS IN PYTHON
class Student():
    def __init__(self,fullname):
        self.name = fullname
    def hello(self):
        print("hello",self.name)
S1 = Student("Karan")
S1.hello()        

class Student():
    college_name = "ABC college"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def Welcome(self):
        print("Welcome Student,",self.name)

    def get_marks(self):
        return self.marks

S1 = Student("karan",97)
S1.Welcome()
print(S1.get_marks())            

# # ==========================================
# # DAY 8 - PRACTICE 1
# Create student class that takes name and marks of 3 subjects as argument in constructor then crete a method to print the avg

class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hy",self.name,"Your score is ",sum/3)
S1 = Student("tony",[78,90,66])
S1.get_avg()

S1.name = "Spider"
S1.get_avg()

# STATIC METHOD

class Student():
    @staticmethod
    def college():
      print("ABC college")
Student.college()
