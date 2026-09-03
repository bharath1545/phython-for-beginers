#set is a collection of non-repetitive elements. It is unordered and unindexed. In python, set is defined in the set class. It is mutable but it can only contain immutable (hashable) objects.
#sets are used to store multiple items in a single variable. It is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.
s={1,2,3}# Initialize a set with three elements
print(type(s)) # Print the type of the set
e=set()# Initialize an empty set
print(type(e)) # Print the type of the empty set
#dont use {} to create an empty set because it will create an empty dictionary instead
f={1,3,555,555,5,7}
print(f) # only one time 555 will be printed because set does not allow duplicate values
#methods of set
g={1,2,3,4,5,"rohan"}
print(g) # Print the set g
g.add("bharath") # Add the element "bharath" to the set g
print(g) # Print the updated set g
#properties of set
#1. unordered
#2. #unindexed
#3. mutable
#there is no way to change the items in a set, but you can add new items
#sets do not contain duplicate items. Duplicate items will be ignored
