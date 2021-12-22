def increment(number, by):
    return number + by

# This will show you how to make "by" optional Arguments instead of default, which already is

def increment(number, by=1):
    return number + by

print(increment(19))

#By is optional, so if you ron the bottom code

def increment(number, by=1):
    return number + by

print(increment(3, 4))

#It proves it all, wow

# RULE : ALL OPTIONAL ARGUMENTS MUST COME AT THE END, AFTER ALL DEFAULT ARGUMENTS, otherwise it will be error

def hi(number, another_number, by=2):
    return number + another_number +by

print(hi(30+5, 2, 3))
# OR
print(hi(305, 20))