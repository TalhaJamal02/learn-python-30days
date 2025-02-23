# mutable: list, dict, set
# immutable: int, float, string, tuple, bool, None

# List
fruits = ["apple", "banana", "cherry", ["orange", "mango", "pineapple"]]

# Indexing & Slicing
print(fruits[0])    # Access first element -> apple
print(fruits[-1])   # Access last element -> cherry
print(fruits[3][2]) # Access nested element -> pineapple
print(fruits[1:])   # Slice from index 1 onwards -> ['banana', 'cherry']

# Common List Methods
fruits.append("peach") # Add element to end
fruits.remove("cherry") # Remove first occurrence of value
fruits.insert(2, "watermelon") # Insert at index
fruits.pop() # Remove and return last element
fruits.clear()  # Remove all elements
print(fruits)

# Tuples
colors = ("red", "green", "blue", "red")
print(colors)

# Indexing & Slicing
print(colors[0])   # Access first element -> red
print(colors[-1])  # Access last element -> blue
print(colors[1:])  # Slice from index 1 onwards -> ('green', 'blue')

# Tuple Methods
print(colors.count("red")) # Count occurrences of value
print(colors.index("green")) # Find index of value

# Tuples are immutable
colors[0] = "yellow" # This will raise an error

# Practice Task
# Create a list of your 5 favorite movies.
# Replace the second movie with another one.
# Convert the list into a tuple and try modifying an element (observe the error).

movies = ["The Dark Knight", "Inception", "The Matrix", "The Lord of the Rings", "The Hobbit"]
movies[4] = "The Dark Knight Rises"
movies = tuple(movies)
movies[0] = "The Dark Knight" # This will raise an error
print(movies)