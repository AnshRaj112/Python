# Opening a file

# r for read, w for write, a for append, r+ for read and write

# file1 = open("test.txt", "r") #File path, mode 

# print(file1.read())

# file1.close()

# with open("test.txt", "r") as file1:
#     file_stuff = file1.read()
#     print(file_stuff)
# print(file1.closed)
# print(file_stuff)
# file1.close()

with open("test.txt", "r") as file1:
    file_stuff = file1.readline(4)
    print(file_stuff)
    
file1 = open("test.txt", "w") #File path, mode 

print(file1.write("Hello"))

file1.close()

file1 = open("test.txt", "a") #File path, mode 

print(file1.write("World"))

file1.close()
