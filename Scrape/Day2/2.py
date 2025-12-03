# Dictionaries

# It has keys and values

# Key is an index by label 

Dist = {"Thriller":1982, "Back in Black":1980, "The Dark Side of the Moon":1973, "The Bodyguard":1992, "Bat Out of Hell":1977}

print(Dist)

print(Dist["Thriller"])

# Adding elements to the dictionary

Dist["Jurrasic Park"] = 1997

print(Dist)

# Deleting elements from the dictionary

del(Dist["Thriller"])

print(Dist)

# Finding element in the dictionary

print("The Bodyguard" in Dist)

print("Jurrasic Park" in Dist)


print(Dist.keys())

print(Dist.values())

print(Dist.items())

Dict1={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}


print(Dict1["D"])

