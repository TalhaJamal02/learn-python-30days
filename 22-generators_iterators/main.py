# What are Generators?
# Generators are special functions that allow you to yield values one at a time instead of returning them all at once. They are memory-efficient and great for handling large data streams.

def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
for num in gen:
    print(num)


# What are Iterators?
# An iterator is an object that contains a sequence of data and can be iterated (looped) one element at a time.

nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3


# Practice Tasks
# Create a generator that yields even numbers from 1 to 10.
def even_numbers():
    for num in range(1, 11):
        if num % 2 == 0:
            yield num


for n in even_numbers():
    print(n)

# Write a custom iterator that iterates through a string word by word.
class WordIterator:
    def __init__(self, text):
        self.words = text.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return word


sentence = "Python is a powerful language"
it = WordIterator(sentence)
for word in it:
    print(word)


# Create a Fibonacci generator that yields numbers up to a given limit.
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a+b


for num in fibonacci(50):
    print(num)