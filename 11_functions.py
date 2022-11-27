def say_hi():
    print("Hello User")

say_hi()

def say_hi(name):
    print("Hello " + name)

say_hi("Mike")
say_hi("Steve")

def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

say_hi("Mike", "35")
say_hi("Steve", "70")

def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hi("Mike", 35)
say_hi("Steve", 70)