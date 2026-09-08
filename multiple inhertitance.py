
class Employee:
  company="ITC"
  name="default name"
  def show(self):
    print("the name of the employee is  {self.name}and the company is {self.company}")

class coder:
  language="phython"
  def printlanguages(self):
    print(f"out pf all languages her is ur language{self.language}")

class Programmer(Employee,coder): #derived class or child class
  company="ITC infotech"
  def show(self):
    
    print(f"the name is {self.company}and the salary is {self.language}")
a=Employee()
b=Programmer()
b.show()
b.printlanguages()


print(a.company,b.company)
