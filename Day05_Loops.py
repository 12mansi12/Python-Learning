# ==========================================
# DAY 5 - Loops

#WHILE LOOP 
i=1
while i <=5:
    print("MINMIN")
    i +=1
print(i)

# #2nd way
i=5
while i >=1:
    print("MINMIN")
    i -=1
print(i) 

# #PRACTICE 1
# ## multiplication table of a number n
n=int(input("Enter your number"))
i=1
while i<=10:
    print(n*i)
    i += 1

##Print the elements of the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]
n = [1,4,9,16,25,36,49,64,81,100]

i = 0
while i < len(n):
    print(n[i])
    i += 1
  
#BREAK
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1

print("end")

#CONTINUE
i=0
while i<= 10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

#For loops
nums=[1,2,3,4]
for val in nums:
    print(val)
else:
    print("done")        
 
#RANGE
for el in range(5):
    print(el) 

for el in range(1,5):
    print(el)

for el in range(1,10,2):
    print(el)    

#PASS STATEMENT
for el in range(5):
    pass
print("done")


