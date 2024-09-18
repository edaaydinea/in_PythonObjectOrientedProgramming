# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass()  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0
    
    def somefunc(self, newval):
        self.value2 = newval


obj = ImmutableClass()
print(obj.value1)

# TODO: attempting to change the value of an immutable class throws an exception
obj2 = ImmutableClass("Another Value", 15)
print(obj2)

# TODO: even functions within the class can't change anything
obj.value1 = "Another value"
print(obj.value1)

obj.somefunc(20)
