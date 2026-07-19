# ==========================================
# DAY 6 - FUNCTIONS 
def sum (a,b):
    s=a+b
    return s
print(sum(2,3))

#RECURSION
def show (n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("end")
show(3) 
   
# ==========================================
# DAY 6 - PRACTICE 1
#WAF to convert USD to INR
def converter(usd_value):
    inr_value = usd_value*83
    print(usd_value,"USD =",inr_value,"INR")

converter(5)

#WAF to find factorial of n (n is parameter)

def fact(n):
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print(factorial)

fact(3)   

# Calculator Function
def calculator (a,b):
    s=a+b
    x=a-b
    y=a*b
    v= a/b
    return s,x,y,v
print(calculator(2,3))

# Student Result Function
def student_result(marks):
    total = sum(marks)
    avg = total/len(marks)
    highest_marks = max(marks)
    lowest_marks = min(marks)
    return total, avg, highest_marks,lowest_marks
marks=[1,2,3,4]
print(student_result(marks))

# ==========================================
#level-2 
#Student Grade System
def calculate_grade(marks):
    total=sum(marks)
    avg = total/len(marks)
    if avg >=90:
        return "A"
    elif avg >=80:
        return "B"
    elif avg >=70:
        return "C"
    else:
        return "D"  
marks=[10,20,30,90]
calculate_grade(marks) 

# Word Analyzer
def word_analyzer(word):
    length = len(word)
    first_character = word[0]
    last_character = word[-1]
    vowel=0
    for character in word:
        if character in  "aeiou":
            vowel +=1

    print("length=",length,"\n" "first_character=",first_character,"\n""last_character=",last_character,"\n""vowels=",vowel)        
word_analyzer("mathematics")




