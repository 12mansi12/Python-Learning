# ==========================================
# DAY 3 - LIST
marks = [87,64,33,95,76]
print(marks[4])
marks[0]=56
print(marks[0])  #muteable

#list methods
list=[2,1,4,3]
list.append(5)
list.sort()
print(list)
list.sort(reverse=True)
list.insert(3,8)
print(list)

# ==========================================
#TUPLE IN PYTHON

tup= (78,54,33,98)
print(tup[3])
# tup[0]=69 not allowed unmuteable

# ==========================================
# DAY 3 - PRACTICE 1

marks=[]
marks.append(int(input("Enter Python marks: ")))
marks.append(int(input("Enter Maths marks: ")))
marks.append(int(input("Enter English marks: ")))
marks.append(int(input("Enter SQL marks: ")))
marks.append(int(input("Enter AI marks: ")))
#can go for loop etc other option
highest_score= max(marks)
lowest_score= min(marks)
total= sum(marks)
avg= total/len(marks)

print("Marks:", marks)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Total:", total)
print("Average:", avg)

# Search Name
student = ["mansi","riya","siya","junu","rana"]
name = input("Enter your name ")
if name in student:
    print("Student found")
else:
    print("Still finding")    

# Duplicate counter
numbers = [5, 2, 5, 7, 5, 9, 2]

count_5 = numbers.count(5)
count_2 = numbers.count(2)

print("5 appears:", count_5, "times")
print("2 appears:", count_2, "times")

# list to tuple
list=[1,2,3,4,5]
tup=tuple(list)
print("list : ",list)
print("tuple : ",tup)
print(type(list))
print(type(tup))

# student database


names = []
marks = []

names.append(input("Enter Student 1 Name: "))
marks.append(int(input("Enter Marks: ")))

names.append(input("Enter Student 2 Name: "))
marks.append(int(input("Enter Marks: ")))

names.append(input("Enter Student 3 Name: "))
marks.append(int(input("Enter Marks: ")))

print("\n===== STUDENT DATABASE =====")
print("NAME       MARKS")
print("_____________")

print(names[0], "-", marks[0])
print(names[1], "-", marks[1])
print(names[2], "-", marks[2])
