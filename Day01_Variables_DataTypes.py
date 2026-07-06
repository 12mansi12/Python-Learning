# ==========================================
# DAY 1 - VARIABLES

name = "Mansi"
age = 19
cgpa = 8.5
is_student = True

print(name)
print(age)
print(cgpa)
print(is_student)

# ==========================================
# DAY 1 - DATA TYPES

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

# ==========================================
# DAY 1 - TYPE CONVERSION

num = "250"

print(type(num))

num = int(num)

print(num)
print(type(num))

# ==========================================
# DAY 1 - PRACTICE 1
# Student Information Program

# ==========================================
# PRACTICE 1 : STUDENT PROFILE

name = input("Enter your name: ")
age = int(input("Enter your age: "))
college = input("Enter your college name: ")

print("\n===== STUDENT PROFILE =====")
print("Welcome,", name)
print("You are", age, "years old.")
print("You study at", college)

# ==========================================
# DAY 1 - PRACTICE 2
print("\n")
# Marks Calculator

python_marks = int(input("Enter Python marks: "))
maths_marks = int(input("Enter Maths marks: "))
english_marks = int(input("Enter English marks: "))
sql_marks = int(input("Enter SQL marks: "))

total = python_marks + maths_marks + english_marks + sql_marks

average = total / 4

highest = max(
    python_marks,
    maths_marks,
    english_marks,
    sql_marks
)

lowest = min(
    python_marks,
    maths_marks,
    english_marks,
    sql_marks
)

print("\n===== RESULT =====")
print("Total :", total)
print("Average :", average)
print("Highest :", highest)
print("Lowest :", lowest)
