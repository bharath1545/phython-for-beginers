# Conditional Expressions in Python
# Conditional expressions, also known as ternary operators, allow you to evaluate a condition and return one of two values based on whether the condition is True or False. The syntax for a conditional expression is:
#if else 
x=int(input("Enter a number: "))
if x>5:
  print("The number is greater than 5")
else:
  print("The number is less than or equal to 5")
#if elif else lader 
g=int(input("Enter ur age: "))
#if statement no 1
if g%2==0:
  print("Your age is even.")
#end of if statement no 1
#if statement no 2
if g>=18:
  print("You are eligible to vote.")
  print("good for you")

elif g<0:
  print("Invalid age entered.")
else:
  print("You are not eligible to vote.")
#end of if statement no 2
#relational operators are used to compare values and return a boolean result (True or False). The common relational operators in Python are:
# Greater than (>) 
# Less than (<)
# Equal to (==)
# Not equal to (!=)
# Greater than or equal to (>=)
# Less than or equal to (<=)
#logical operators are used to combine multiple conditions and return a boolean result. The common logical operators in Python are:
# and: Returns True if both conditions are True
# or: Returns True if at least one condition is True
# not: Returns True if the condition is False

#multiple if statements can be used to evaluate multiple conditions in a sequence. Each condition is checked in order, and the first one that evaluates to True will execute its corresponding block of code. If none of the conditions are True, the else block (if present) will execute.



