# functions_advanced.py
# Advanced function concepts

def greet(name, message="Welcome to Python"):
    return f"Hello {name}! {message}"

def add(a, b):
    return a + b

def calculate(a, b):
    return add(a, b), a * b  # multiple return values

def get_total(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def print_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# Example usage
if __name__ == "__main__":
    print(greet("Krishnam"))
    print("Add:", add(5, 3))
    sum_val, product = calculate(4, 5)
    print("Sum:", sum_val, "Product:", product)
    print("Total:", get_total(1, 2, 3, 4))
    print_profile(name="Krishnam Singh", role="Python Developer")
