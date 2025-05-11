for i in range(10, 0, -2):
    print(i)

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

for i in range(5):
    print("I love Python", i)


for index, fruit in enumerate(fruits):
    print(index, fruit)
    
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

count = 1

while count <= 5:
    print("Counting:", count)
    count += 1


for i in range(10):
    if i == 5:
        break
    print(i)


for i in range(5):
    if i == 2:
        continue
    print(i)

for i, x in enumerate(['A', 'B', 'C']):
    print(i, x)