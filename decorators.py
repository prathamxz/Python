def Hello():
    print("Hello World")

def greet (fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx


@greet
def Hello():
    print("hello world")

def add(a,b):
    print(a+b)

Hello()


















# Python Decorators

# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.
# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function.
# The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:
# @decorator_function def my_function():
# pass
# The @decorator_function
# Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.
# Practical use case
# One common use of decorators is to add logging to a function. For