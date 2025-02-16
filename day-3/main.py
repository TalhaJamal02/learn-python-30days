name:str = "John"
age:int = 20

print(f"Hello, my name is {name} and I am {age} years old.")
# output: Hello, my name is John and I am 20 years old.

Str: str = "Hello, World!"


print(Str[0:5])
# output: Hello

print(Str[6:])
# output: World!

print(Str[::-1])
# output: !dlroW ,olleH

print(Str.lower(), Str.upper(), Str.strip(), Str.replace("World","python"), Str.split(","))
# output: hello, world! HELLO, WORLD! Hello, World! Hello, python! ['Hello', ' World!']

print("Hello" in Str)
# output: True

print("Python" not in Str)
# output: True