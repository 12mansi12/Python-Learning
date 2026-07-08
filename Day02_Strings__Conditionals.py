# ==========================================
# DAY 1 - STRINGS

str1= "Mansi"
str2="\tTyagi"

#concatenation
print(str1 + str2)
#length of string
print(len(str2))
#indexing in strings
print(str1[2])
#Slicing in strings
print(str1[0:4])
print(str1[:4])
print(str1[0:])

# # ==========================================
# #string Functions
str = "hey im a student"
print(str.endswith("ent"))
print(str.capitalize())

print(str.find("h"))
print(str.count("e"))

# # ==========================================
# # DAY 2 - PRACTICE 1

# #Student Introduction Take the user's:
# # Student Introduction
name = input("Enter your name: ")
age = int(input("Enter your age: "))
college = input("Enter your college name: ")

print("\n===== STUDENT INTRODUCTION =====")
print(f"Hello! I'm", name)
print("My current age is", age)
print("I'm studying at", college)

# #Email Checker Ask the user to enter an email. Check whether it contains "@".

email = input("Enter your Email for checking ")
if "@" in email:
    print("correct Email")
else:
    print("incorrect Email")    


# #Password Length Ask the user to enter a password. If its length is 8 or more.
password = input("Enter your password \t: ")

if len(password) >= 8:
    print("Correct Password")
else:
    print("Incorrect Password")

#Reverse a Word
word = input("Enter a word: ")

reverse = word[::-1]

print("Original Word :", word)
print("Reversed Word :", reverse)  

# ==========================================
# DAY 2 - PRACTICE 1
#odd and even
number = int(input("Enter your number : "))
if number%2==0 :
    print("Even")
else:
    print("odd")    

#greater number
a = input("Enter your first number : ")
b = input("Enter your second number : ")

if a>b :
    print("a is greater")
else:
    print("b") 

#grade calculator
marks = int(input("Enter yous marks : "))

if marks>=90 :
    print("A")
elif marks>=80 and marks<90:
    print("B")
elif marks>=70 and marks<80:
    print("B")
elif marks>=60 and marks<70:
    print("B")
else:
    print("Fail")

#age checker
age=int(input("Enter your age : "))
if age<13 :
    print("child")
elif age>=13 and age<19:
    print("Teen")
elif age>=20 and age<59:
    print("adult") 
else:
    print("Senuor citizen")   

#vowel or consonant
alpha = input("Enter your alphabet : ").lower()
if alpha in "a,e,i,o,u" :
    print("vowel")
else:
    print("consonant")    

