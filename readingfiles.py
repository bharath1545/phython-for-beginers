#open() makes the posible to read the file and open(filename,mode)
fhand=open('hello.py')
print(fhand)
#nindicates to a new line
stuff='X\nY'
print(stuff) 

xfile=open("hello.py")
for hours in xfile:
  print(hours)

fhand=open("functions.py")
count=0
for line in fhand:
  count=count+1
print("line count:",count)

zfile=open("strings.py")
inp=zfile.read()
print(len(inp))
print(inp[:20])
