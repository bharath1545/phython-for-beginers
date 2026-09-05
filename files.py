'''
a="a very long string with emails'

emails=[]
3 seconds
'''

f=open("file.txt","r")
data=f.read()
print(data)
f.close()

#there are two files text files and binary files 
# how to write in files
st="hey harry you are amzing"
f=open("myfile .txt","a")

f.write(st)
f.close()


f=open("file.txt")
lines=f.readlines()
print(lines)
print(lines,type(lines))
f.close()

#there are two types in this so its like read line()where it reads one by one 
#there is another type where it reads whole thing which is readlines()
f=open("file.txt")
line =f.readline()
while(line!=""):
  print(line)
  line=f.readline()

f.close()

'''
the same can be written using with statement as 
with open("file.txt") as f:
    print(f.read())

you dont have to explicitly close the file
'''
