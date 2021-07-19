class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def square_root(self, x):
        return __import__("math").sqrt(x)

    def divide(self, x, y):
        return x / y

    def multiply(self, x, y):
        return x * y

    def power(self, x, y):
        return __import__("math").pow(x, y)
