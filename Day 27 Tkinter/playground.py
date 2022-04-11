def add(*args):
    print(f"The first input is {args[0]}")
    total = 0
    for arg in args:
        total += arg
    return total

print(add(3,5,6))

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    return n

calculate(n=3, add=23, multiply=9)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") #using .get() is like selecting with square bracket but returns None if there's nothing
        self.model = kw.get("model")

my_car = Car()
print(my_car.make)