print(10 * "=", "Variadic Parameter with *args", 10 * "=")


class Calculator:
    def __init__(self, *args):  # Variadic parameter
        total = 0
        for value in args:
            total += value

        print(total)


cal1 = Calculator(1, 2, 3)  # Output: 6
cal2 = Calculator(10, 20, 30, 40)  # Output: 100

print(10 * "=", "Variadic Parameter with *kwargs", 10 * "=")


class User:
    def __init__(self, **kwargs):  # Variadic parameter
        for key, value in kwargs.items():
            print(f"{key}: {value}")


user1 = User(name="Alice", age=30, city="New York")
