#loops are used to repeat a block of code multiple times. In Python, there are two main types of loops: for loops and while loops.
print(1)
print(2)
print(3)  
print(4)
print(5)
#the same task can be accomplished using a loop, which is more efficient and less error-prone. For example, we can use a for loop to print the numbers from 1 to 5:
for i in range (1,6):
  print(i)

#while loops are used to repeat a block of code as long as a certain condition is true. The syntax for a while loop is:
i=1
while i<6: # the condition is checked before each iteration of the loop. If the condition is True, the code block inside the loop is executed. If the condition is False, the loop terminates and the program continues with the next statement after the loop.
  print(i)
  i+=1
i=0
while i<5:
  print("bharath bhat")
  i=i+1


#list using while loop
l=[1,"harry",3.5,"python",False]
i=0
while (i<len(l)):
  print(l[i])
  i+=1


#for loops are used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence. The syntax for a for loop is:
x=int(input("Enter a number: "))
for i in range(0,x,4): # step value of 4 is used to increment the loop variable i by 4 in each iteration. This means that the loop will start at 1 and increment by 4 until it reaches or exceeds the value of x.
  print(i)
#for loops with lists
o=[1,2,4,5,6,7,786]
for i in o:
  print(i) 
#for loops with tuples
t={6,231,75,122}
for i in t:
  print(i)
#for loops with strings
s="bharath"
for i in s:
  print(i)

#range function is used to generate a sequence of numbers. It can take one, two, or three arguments:
# range(stop): Generates numbers from 0 to stop-1
# range(start, stop): Generates numbers from start to stop-1
# range(start, stop, step): Generates numbers from start to stop-1, incrementing by step. The range function is commonly used in for loops to iterate over a sequence of numbers.
#for with else loop is used to execute a block of code after the for loop has completed all iterations. The else block will only execute if the for loop completes without encountering a break statement. If the loop is terminated by a break statement, the else block will be skipped.
b=[1,2,3,4,5]
for item in b:
  print(item)
else:
  print("No items left.")

#break statement is used to exit a loop prematurely, before the loop has completed all iterations. When a break statement is encountered inside a loop, the loop is immediately terminated, and the program continues with the next statement after the loop.
for i in range(1, 10):
  
  if i == 5:
    break #exit the loop right now when i is equal to 5. The loop will not continue to iterate through the remaining numbers in the range.
  print(i)
for i in range(1, 10):
  
  if i == 5:
    continue #skip the rest of the loop body when i is equal to 5. The loop will continue to iterate through the remaining numbers in the range.
  print(i)

#the difference between break and continue is that break exits the loop entirely, while continue skips the current iteration and moves on to the next one.

#pass statement is used as a placeholder for code that has not been implemented yet. It does nothing and allows the program to continue executing without raising an error. The pass statement is often used in situations where a block of code is required syntactically, but no action is needed.
h=[1,2,3,4,5]
for item in h:
  pass #do nothing and continue with the next iteration of the loop. The loop will iterate through all the items in the list, but no action will be taken for each item.