# Functions

def add(a):
    b = a + 1
    return b

print(add(10))

help(add)

def Mult(a, b):
    return a*b

print(Mult(10,20))

print(Mult(2, "Ansh "))

def MJ():
    print("Hello")

MJ()

# Function with empty body

def NoWork():
    pass
    return None

print(NoWork())

def print_function(A):
    for a in A:
        print(a + '1')
print_function(['a', 'b', 'c'])