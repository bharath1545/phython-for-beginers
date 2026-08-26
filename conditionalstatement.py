#there is a indentation for conditional statements
x=5
if x==5:
    print("x is positive")
    print("55")
if x<0:
    print("x is negative")
print("Goodbye")
x=5
if x>2:
    print("Bigger than 2")
    print("Still bigger")
print("Done with 2")

for i in range(5):
    print(i)
    if i>2:
        print("Bigger than 2")
    print("Done with i", i)
print("All done")
#ifelse statement
x==2
if x>2:
    print("bigger")
else:
    print("smaller")
print("All done")
#if else if statement
x=4
if x>2:
    print("bigger")
elif x==2:
    print("equal")  
print("All done")
#try and except statement
astr="hello"
try:
    istr=int(astr)
except:
    istr=-1
print("First", istr)
raw=input("Enter a number: ")
try:
    ival=int(raw)
except:
    ival=-1
if ival>0:
    print("Nice work")
else:
    print("Not a number")