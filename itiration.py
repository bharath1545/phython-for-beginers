n=5
while n>0:
    print(n)
    n=n-1
print("Blastoff!")
print(n)
#there are two types of loops one is finite loop and another is infinite loop
while True:
    line=input("> ")
    if line=="done":
        break#comes out of the loop if we enter done
    print(line)
print("Done!")

while True:
    line=input("> ")
    if line[0]=="#":
        continue#skips the current iteration of the loop and goes to the next iteration   
    if line=="done":
        break
    print(line)
print("Done!")

#while loops are called indefinite loops because we don't know how many times the loop will run
#definite loops are called for loops because we know how many times the loop will run for example if we want to print numbers from 1 to 10 we can use for loop
#for loops are used to iterate over a sequence (list, tuple, dictionary, set, or string).
for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")