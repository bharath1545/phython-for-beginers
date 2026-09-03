#tuples are immutable sequences, typically used to store collections of heterogeneous data. They are similar to lists, but unlike lists, they cannot be changed after they are created. Tuples are defined by enclosing the elements in parentheses `()`.
a=(1, 2, 3, 4, 5)
print(type(a))
b=(1,)##single element tuple
print(type(b))
c=(1,"rohan","bharath")
#c[0]=2 #this will give an error because tuples are immutable
print(c)
#methods of tuples
d=(1,2,3,4,5)
print(d.count(2)) #returns the number of occurrences of the value 2 in the tuple
numbers=(1,2,3,4,5)
print(numbers.index(3)) #returns the index of the first occurrence of the value 3 
print(len(numbers)) #returns the number of elements in the tuple