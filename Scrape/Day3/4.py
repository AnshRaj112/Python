# Exception Handling

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("That's not a valid number!")
else:
    print(f"Result: {result}")


# r for read, w for write, a for append, r+ for read and write
try:
    getfile = open("test.txt", "w")
    getfile.write("Hello")
except IOError:
    print("Cannot write to file")
finally:
    getfile.close()
    print("File closed")
    

a = 1
try:
    b = int(input("Please enter a number to divide a: "))
    a = a / b
    print("Success a =", a)
except:
    print("There was an error")