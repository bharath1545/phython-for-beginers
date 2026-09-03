#dictonaries are used to store data values in key:value pairs
d={}# Initialize an empty dictionary
marks={
     'harry': 45,
     'rohan': 56,
     'skillf': 67
      
}
print(len(marks)) # Print the number of key-value pairs in the dictionary


print(marks,type(marks)) # Print the dictionary of marks
print(marks['harry']) # Print the marks of 'harry'
#property of dictionary is that it is unordered and indexed
#it is mutable and can be changed
#it cannot contain duplicate keys but can contain duplicate values
#methods of dictionary
print(marks.items()) # Print the items (key-value pairs) of the dictionary
print(marks.keys()) # Print the keys of the dictionary
print(marks.values()) # Print the values of the dictionary
marks.update({'harry': 100}) # Update the marks of 'harry' to 100
print(marks) # Print the updated dictionary of marks
marks.update({'hammad': 90}) # Add a new entry for 'hammad' with marks 90
print(marks) # Print the updated dictionary of marks
print(marks.get('harry')) # Get the marks of 'harry'
#difference between get and [] is that if the key is not present in the dictionary then get will return None but [] will give an error
print(marks.get('hello')) # Get the marks of 'hello' we will get None because 'hello' is not a key in the dictionary
#print(marks['hello']) # This will give an error because 'hello' is not a key in the dictionary
print(marks.pop('harry')) # Remove the entry for 'harry' from the dictionary
print (marks.popitem()) # print the last inserted item and remove it from the dictionary