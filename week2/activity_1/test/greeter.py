'''Considering reuse (modularisation)
when creating python programs'''


def greet(name):
    print(f"Hello, {name}!")


# create a calculator class and re-use this by instantiating it in the main.py
class Calculator:
    def __init__(self, numbers, method):
        self.numbers = numbers
        self.method = method
        self.result = self.calculate()

    def calculate(self):
        result = 0
        if self.method in ["add", "+", "sum"]:
            for number in self.numbers:
                result += number
        elif self.method in ["subtract", "-", "minus"]:
            for number in self.numbers:
                if number == self.numbers[0]:
                    result = number
                else:
                    result -= number
        elif self.method in ["multiply", "*", "times", "product"]:
            for number in self.numbers:
                if number == self.numbers[0]:
                    result = number
                else:
                    result *= number
        elif self.method in ["divide", "/"]:
            for number in self.numbers:
                if number == self.numbers[0]:
                    result = number
                else:
                    result /= number
        elif self.method in ["power", "**", "exponent"]:
            for number in self.numbers:
                if number == self.numbers[0]:
                    result = number
                else:
                    result **= number
        else:
            print("Invalid Method. Default Result: 0")
            result = 0
        return result

    def get_numbers(self):
        for _ in self.numbers:
            print(_)

    def set_number(self, new_numbers):
        self.numbers = new_numbers

    def get_method(self):
        return self.method

    def set_method(self, new_method):
        self.method = new_method

    def get_result(self):
        return self.result
# So as not to contaminate your global namespace, it is good practice to use a main function.

# so that we can reuse our code as both a module and
# we can use an if statement to ensure that some code is only executed when name is __main__

# module name when imported

    # above is __main__ when running directly
    # only called when a script
