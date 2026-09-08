class Employee:
  company="ITC"
  def show(self):
    print("the name is {self.name}and the salary is {self.salary}")



class Programmer(Employee): #derived class or child class
  company="ITC infotech"
  def show(self):
    
    print(f"the name is {self.name}and the salary is {self.salary}")
a=Employee()
b=Programmer()


print(a.company,b.company)