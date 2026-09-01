#list is a container to store the data in a sequential manner
friends = ["Rohit", "Rahul", "Ramesh", "Rakesh", 5, 6, 7, 8, 9]
print(friends[0])
friends[0] = "Rohit Sharma" #unlike strings, lists are mutable, we can change the value of a list
print(friends[0])
print(friends[1:4]) #slicing the list
#list methods
friends.append("Suresh") #adds an element to the end of the list
print(friends)
l1 = [5, 2, 3, 4, 6]
l1.sort() #sorts the list in ascending order
print(l1)
l1.reverse() #reverses the list
print(l1)
l1.insert(3,3.3333) #inserts an element at a specific index
print(l1)
l1.pop(3) #removes the element at index 3 from the list
print(l1)
l2 = [1, 2, 3, 4, 5]
l2.remove(3) #removes the first occurrence of the value 3 from the list
print(l2)