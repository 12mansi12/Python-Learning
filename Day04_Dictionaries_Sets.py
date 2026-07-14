# ==========================================
# DAY 4 - dictinary 

dict = {
    "Name":"Mansi",
    "CGPA":9.6,
    "Marks":[98,78,90]
}
print(dict)
print(dict["Name"])

#dictionary methods
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("Name"))
dict.update({"NEW":23})
print(dict)

# ==========================================
# DAY 4 - sets

collection={1,2,3,4}
print(collection)
print(type(collection))

#set methods
collection.add(5)
collection.remove(1)
collection.pop()
print(collection)

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))

# # ==========================================
# # DAY 4 - PRACTICE 1

student = {
    "name": "Rahul",
    "age": 19
}
student.update({"College":"IPEM"})
print(student)

#STUDENT MARKS- MIN MAX SUM TOTAL AVG
student = {
    "Python":95,
    "SQL":90,
    "English":88,
    "Maths":91
}

marks=list(student.values())
print(marks)

highest = max(marks)
lowest = min(marks)
total = sum(marks)
avg = total/len(marks)

print("Student marks ", student)
print("highest marks ", highest)
print("lowest marks", lowest)
print("total marks", total)
print("avg marks ", avg)

#SEARCH KEY
student = {
     "Python":95,
     "SQL":90,
     "English":88,
     "Maths":91
 }
key= input("Enter your key ")
if key in student:
    print("key found")
    print("marks : ",student[key])
else:
    print("not found")  

#EMPLOYEE DETAILS
emp={}
a=input("Enter your name :")
b=input("Enter your department: ")
c=int(input("Enter your salary: "))

emp.update({"Name":a})
emp.update({"Department":b})
emp.update({"Salary":c})

print(emp)

#BONUS QUES MIX OF SET ND DICTIONARY
student1 = {
    "name":"Mansi",
    "skills":{"Python","SQL","Excel"}
}

student2 = {
    "name":"Rahul",
    "skills":{"Python","Java","C"}
}
common= student1["skills"].intersection(student2["skills"])
print("common skills ",common)

only_mansi= student1["skills"].difference(student2["skills"])
print("only mansi have these skills ",only_mansi)
only_rahul= student2["skills"].difference(student1["skills"])
print("only rahul have these skills ",only_rahul)

all_skills= student1["skills"].union(student2["skills"])
print("all skills ",all_skills)

