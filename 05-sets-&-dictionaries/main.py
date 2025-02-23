# Sets are unordered collections of unique elements
# Dictionaries are unordered collections of key-value pairs

# Sets:
# Sets are unordered collections of unique elements
# Sets are mutable
# Sets are unindexed
# Sets are unordered
# Sets are unordered

my_set = {1, 2, 3, 4, 5}
print(my_set)

# print(my_set[1])
my_set.add(6)
my_set.remove(2)
my_set.discard(3)
my_set.pop()

# print(my_set)

# Dictionaries:
# Dictionaries are unordered collections of key-value pairs
# Dictionaries are mutable
# Dictionaries are unindexed
# Dictionaries are unordered
# Dictionaries are unordered

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)  # Union: {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersection: {3, 4}
print(A - B)  # Difference: {1, 2}
print(A ^ B)  # Symmetric Difference: {1, 2, 5, 6}

my_dict = {"name": "Talha", "age": 18, "city": "Karachi"}
print(my_dict)
print(my_dict["name"])

my_dict["name"] = "Ali"
my_dict["email"] = "ali@gmail.com"
print(my_dict)

print(my_dict.keys())  # Get all keys  
print(my_dict.values())  # Get all values  
print(my_dict.items())  # Get key-value pairs  