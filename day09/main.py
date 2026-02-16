# main.py
# Using decorator with arguments

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is running...")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' finished execution.")
        return result
    return wrapper


@logger
def multiply(a, b):
    return a * b


result = multiply(4, 5)
print("Result:", result)
