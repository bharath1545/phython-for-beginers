#recursion is a programming technique where a function calls itself in order to solve a problem. It is often used to break down complex problems into simpler subproblems. Recursion typically involves a base case that stops the recursion and prevents infinite loops.
#The syntax for defining a recursive function is similar to that of a regular function, but the function calls itself within its own body. The base case is a condition that determines when the recursion should stop. Without a base case, the function would continue to call itself indefinitely, leading to a stack overflow error.
#factorial(1)=1
#factorial(2)=2*1
#factorial(3)=3*2*1
#factorial(4)=4*3*2*1
#factorial(5)=5*4*3*2*1
#factorial(n)=n*(n-1)*(n-2)*...*1
#factorial(n)=n*factorial(n-1)


def factorial(n):
  if(n==1 or n==0):
    return 1
  return factorial(n-1)*n



n=int(input("enter a number: "))
print(f"the factorial of this number is :{factorial(n)}")