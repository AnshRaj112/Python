#List and Tuple

#Tuples are an ordered sequence 

Rating = (10, 6, 8, 9, 2, 1)

tuple1 = ("String", 10, 2.5, True)

print(type(tuple1))

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])

tuple2 = tuple1 + ("Hello", 10)

print(tuple2)

print(tuple2[0:3])

#tuples are immutable 

#tuple2[0] = "Hello"

#print(tuple2) #Traceback (most recent call last):
  #File "C:\Users\KIIT0001\OneDrive\Desktop\Programming languages\Python\Day2\1.py", line 24, in <module>
   # tuple2[0] = "Hello"
 #   ~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment


NT = (1, 2, ("Pop", "Rock"), 3, 4)

print(NT[2][1])
print(NT[2][1][1])


#Lists

List = [1, 2, 3, 4, 5]

print(List)

#Lists are mutable

List[0] = 10

print(List) 

#We can also nest tuples in lists

List.extend(NT)

print(List)

#We can also nest lists in lists

List.append(NT)

print(List)

del(List[10])

print(List)

print("Ansh Raj".split())

print("Ansh Raj".split("a"))


List2 = List[:]

print(List2)

say_what=('say','what','you','will') 
print( say_what[-1]) 

A=(1,2,3,4,5)

print(A[1:4])

B = [1,2,3] + [1,1,1]

print(B)

C = [1]
C.append([2, 3, 4, 5])

print(C)