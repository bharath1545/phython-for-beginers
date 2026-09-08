class employee:
  a=1


class programmer(employee):
  b=2

class Manager(programmer):

  c=3


o=employee()
 
print(o.a)#prints the attribute
#print(o.b)#shows an error as there is no b attribute in Employee class

o=programmer()
print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)