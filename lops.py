friends=["Joseph", "Glenn", "Sally"]
for friend in friends:
    print("Happy New Year:", friend)
print("Done!")
#loop idioms and patterns
print("Before")
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print("After")

largest_so_far=-1
print("Before:", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num>largest_so_far:
        largest_so_far=the_num
    print(largest_so_far, the_num)
print("After:", largest_so_far)

largest_so_far=-1
print("Before:", largest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if num>largest_so_far:
        largest_so_far=num
        print("largest_so_far,the_num")
print("After:", largest_so_far)

zork=0
print("Before:", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork=zork+1
    print(zork, thing)
print("After:", zork)

zork=0
print("Before:", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork=zork+thing
    print(zork, thing)
print("After:", zork)
count=0
sum=0
print("Before:", count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count=count+1
    sum=sum+value
    print(count, sum, value)
print('after',count,sum,sum/count)
found=False
print('before',found)
for value in [9,41,12,3,74,15]:
    if value ==3:
       
        
       found=True
    print(found,value)
print("after",found)

largest_so_far=None
print('before')
for value in [9,41,12,3,74,15]:
    if largest_so_far is None:
        largest_so_far=value
    elif value>largest_so_far:
        largest_so_far=value
    print(largest_so_far,value)
print ('after',largest_so_far)
#is and is not
#now what happens is that 0==0.0  is true but 0is0.0 is not true because in is there type and value both must be same 