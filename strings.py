str="hello world "#string
#we can add the strings 
#each charecter has a seperate index banana '
#banana
#012345
fruit='banana'
letter=fruit[1]
print(letter)
#u cant ask for index if its not there 
fruit="apple"
print(len(fruit))
fruit="bannna"
index=0
while index<len(fruit):
  letter=fruit[index]
  print(index,letter)
  index=index+1
fruit="kivi"
for letter in fruit:
  print(letter)
#string operation 
s="bharath"
print(s[0:4])#start from 0 but dont include the 4
print(s[6:20])
#u can eliminate the first or last it assumes 0 and the end of the string
a="hello"
b=a+" "+'there'
print(b)
#we can use in as a operator to find whether the charector belongs to the string or not 
fruit="kola"
if 'a' in fruit:
  print("makabosada")

#string library 
greet='BHARATH'
x=greet.lower()#.lower()
print(x)
stuff='hello world '
type(stuff)
#.find()
fruit="john"
x=fruit.find('joh')
print(x)
#.upper(),.lower()
#.replace('a','b')it replaces with b 
hi="hello bharath"
nstr=hi.replace('bharath','jhon')
print(nstr)
#stripping whitespace 
great='   hello bvc    '
great.lstrip()
print(great)
great.rstrip()
print(great)
great.strip()
print(great)
line='please have a nice day'
x=line.startswith('please')
print(x)
data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2006'
atpos=data.find("@")
print(atpos)

