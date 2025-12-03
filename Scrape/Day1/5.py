# A string can be enclosed in single quotes

# A string can be enclosed in double quotes

# A string can be enclosed in triple quotes

# A string can be spaces or digit

# A string can also be special characters

Name = "Ansh Raj"

print(Name[0])
print(Name[-1])

print(Name[0:4]) #Ansh is the output 

#Stride 

print(Name[::2])
print(Name[::-1])

print(Name[0:4:2])

# String methods

print(Name.upper())
print(Name.lower())

print(len(Name))

#Tuples

print(3 * Name)

# To put a backslash in a string you need to use \\ double backslash or you can use raw strings by adding an r in front of the string

# To put a single quote in a string you need to use \' single quote

# To put a double quote in a string you need to use \" double quote

# String Methods

Name2 = Name.replace("Ansh", "Raj")
print(Name2)

print(Name.find("Ansh"))

print(Name.count("a"))

print(Name.isalpha())

print(Name.isdigit())

print(Name.isalnum())

print(Name.isspace())

age = 20 

print(f"My name is {Name} and I am {age} years old.")

print("My name is {} and I am {} years old.".format(Name, age))

print("My name is {0} and I am {1} years old.".format(Name, age))

print("My name is {name} and I am {age} years old.".format(name=Name, age=age))

print("My name is %s and I am %d years old." % (Name, age))




