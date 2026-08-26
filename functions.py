def thing():
    print("Hello")
    print("Fun")

thing()
print("Zip")
thing()
def sum():
    x=5
    y=7
    print(x+y)

sum()
sum()
#there are two types of functions one is built in function and another is user defined function
big= max("Hello world")#max is a built in function which gives the maximum value of the string
print("big:", big)

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

number=int(input("Enter a number: "))
if number>0:
    print_lyrics()
else:
    print("You entered a negative number")
def greet(lang):
    if lang=="es":
        return "Hola"
    elif lang=="fr":
        return "Bonjour"
    else:
        return "Hello"

print(greet("es"), "Glenn")
def addtwo(a, b):
    added=a+b
    return added

print(addtwo(3, 5))
