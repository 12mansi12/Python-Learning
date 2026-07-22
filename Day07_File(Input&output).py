# ==========================================
# DAY 1 FILES I/O
#how to open, read file 
f = open("demo.txt","r")
data = f.read()
print(type(data))
print(data)

#Reading a file
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)
f.close()

#Writing a file 
f = open("demo.txt","w")
f.write("this is a new line")

f = open("demo.txt","a+")
f.write("\nthis is a new line 2")

f= open("sample.txt","a") #create new file

f = open("demo.txt","r+") #OVWERWRITE IN THE FILE 
f.write("ABC")
print(f.read())
f.close()

#WITH SYNTAX
with open("demo.txt","r") as f:
    data = f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("new data")

with open("sample.txt", "w") as f:
    f.write("Hello")
    f.close()

 
# deleting a file 
import os

os.remove("sample.txt") # IF U HAVENT CLOSE ANY FILE YET THEN U CANT DELETE THE FILE AGAIN.