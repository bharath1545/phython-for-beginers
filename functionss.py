#group of statements performing a specific task is called function. It is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
a=12
b=45
c=56


average=(a+b+c)/3
print(average)
#function defenation is done using def keyword. The syntax for defining a function is:
# def function_name(parameters):
def avg():
  a=int(input("Enter first number: "))
  b=int(input("Enter second number: "))
  c=int(input("Enter third number: "))
  average=(a+b+c)/3
  print(average)


#function call is done by using the function name followed by parentheses. The syntax for calling a function is:
avg()
print("bharath bhat")



def gooday(name,ending):
  print("Good day, "+name+"!")
  print("Have a great "+ending+"!")
  return "ok" # return statement is used to return a value from a function. The syntax for using the return statement is:


a= gooday("john", "day")
print(a) # the value returned by the function is stored in the variable a, which can be used later in the program. In this case, the function gooday() returns the value "ok", which is then printed to the console.
#there are two types of functions in python: built-in functions and user-defined functions. Built-in functions are pre-defined functions that are available in python, such as print(), len(), and range(). User-defined functions are functions that are defined by the user to perform a specific task.

#functions with arguments are functions that take one or more parameters as input. The parameters are specified in the function definition and can be used within the function body. The syntax for defining a function with arguments is:

#default arguments are arguments that have a default value assigned to them in the function definition. If the caller does not provide a value for a default parameter, the default value will be used. The syntax for defining a function with default parameters is:
def greet(name, greeting="Hello"):
  print(greeting + ", " + name + "!")

greet("Alice")  # Output: Hello, Alice!
#if i give an argumet to the function, it will override the default value. For example:
greet("Bob", "Hi")  # Output: Hi, Bob!




