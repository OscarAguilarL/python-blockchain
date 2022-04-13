name = "Oscar"
age = 22


def print_data():
    print(f"{name}, {age}")


def print_any_data(arg1, arg2):
    print(f"{arg1}, {arg2}")


def calculate_decades(years):
    return years / 10


print_data()
print_any_data("Hello", "World")
print(calculate_decades(age))
