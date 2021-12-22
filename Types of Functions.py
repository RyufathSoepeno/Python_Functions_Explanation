# Type 1: Perform a task

# print() are type 1 functions
# greet() are also type 1 functions





# Type 2: "Return" a Value

# round() are type 2 functions
# ceil() are also type 2 functions


# Type 2 Example

def get_greeting(name):
    return "Hi" + name

get_greeting("Ryufath")

message = get_greeting("Ryufath")
print(message + " You are good")

# This does not print a value, it returns it
# Think of it as if you want to write a message to an email(To a print function), you need to create a function,
# Which means we cannot use type 1 values since they are not usable (You cannot print a print)


# If you try to use type 1 for that situation:
# You will get "none" in the bottom of console, since the return value is none

def greet(name):
    print("Hi There" + name)
    print("Welcome Aboard")

here = greet("Ryufath")
print(here)
#OR
print(greet('Ryufath'))

# To fix this

def greet(name):
    print("Hi There" + name)
    print("Welcome Aboard")
    return "Ok"

print(greet("Reischya"))
# OR
w = greet("Reischya")
print(w)