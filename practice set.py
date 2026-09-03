#write a program to store seven marks
#  in a list entered by the user 
marks= [] # Initialize an empty list to store marks

f1=int(input("Enter enter the marks  1: ")) # Prompt user for the first mark
marks.append(f1) # Add the first mark to the list
f2=int(input("Enter the marks 2: ")) # Prompt user for the second mark
marks.append(f2) # Add the second mark to the list    
f3=int(input("Enter the marks 3: ")) # Prompt user for the third mark
marks.append(f3) # Add the third mark to the list
f4=int(input("Enter the marks 4: ")) # Prompt user for the fourth mark
marks.append(f4) # Add the fourth mark to the list
f5=int(input("Enter the marks 5: ")) # Prompt user for the fifth mark
marks.append(f5) # Add the fifth mark to the list
f6=int(input("Enter the marks 6: ")) # Prompt user for the sixth mark
marks.append(f6) # Add the sixth mark to the list
f7=int(input("Enter the marks 7: ")) # Prompt user for the seventh mark
marks.append(f7) # Add the seventh mark to the list
print(marks) # Print the list of marks
marks.sort() # Sort the list of marks in ascending order
print(marks) # Print the sorted list of marks
