# decorators_basic.py
# Day 09 - Basic Decorators

def simple_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@simple_decorator
def greet():
    print("Hello, Krishnam!")


greet()


#krishnam
#ai