
def add(x, y):
    """add function"""
    return x + y

def subtract(x, y):
    """subtract function"""
    return x - y

def multiply(x, y):
    """multiply function"""
    return x * y

def divide(x, y):
    """divide function"""
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y

#print(divide(8,2))