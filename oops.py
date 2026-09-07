class Employee:
    language="py" #this is a class attribute
    salary=1200000
    def getinfo(self):
      print(f"the language is{self.language}. the salary is {self.salary}")
    @staticmethod
    def greet(self):
      print("good morning")


harry =Employee
harry.name="harry" #this is a object(instance) attribute
print(harry.name,harry.salary,harry.language) #salary and language are class attributes
Employee.greet(harry)

rohan=Employee
rohan.name="rohan"
rohan.language="javascript" #instance attributes takes over class attributes during assignment and retrival
print(rohan.name,rohan.salary,rohan.language)
Employee.getinfo(rohan)
#here name is object(instance) attributes and salary and language are class attributes as they directly belong to the class


