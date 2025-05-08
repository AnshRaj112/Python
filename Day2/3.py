# Sets

# Types of collections
# Unlike list and tuple they are unordered
# Sets only have unique elements

#set() is used to convert a list into a set

A = {"Thriller", "Men in Black", "AC/DC"}

print(A)

A.add("Jurrasic Park")

print(A)

A.remove("Jurrasic Park")

print(A)

B = {"AC/DC", "Jurrasic Park", "Bahubali"}

print(A.union(B))

print(A.intersection(B))

print(A.difference(B))

print(A&B)

# issubset method is used to check for subset

