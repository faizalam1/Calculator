from functools import reduce  # The reduce() function in Python
# takes in a function and a list as argument.
# The function is called with a lambda function and a list
#  and a new reduced result is returned.
import math
# To use log function


class Calculator():
    """Calculator version # 1.1, Minor upgrades added exponent, I have plans
       to add a help menu and did little changes in backend, I was using lot
       of if elif statement, so I mimiced switch statement with python
       dictionary. """
    # I have plan to include other modes.
    def __init__(self, mode="calculate"):
        self.mode = mode

    def input_numbers(self, n):  # This function takes input numbers
        input_numbers = []
        for i in range(n):
            try:
                input_numbers.append(
                    int(input("Enter {} number:\n>>>> ".format(i+1))))
            except ValueError as VE:
                print("Please only enter number.")
        return input_numbers

    # It is both addition and substraction,
    #  just input negative number to subtract
    def summation(self, n):
        input_numbers = self.input_numbers(n)
        return(sum(input_numbers))

    def multiplication(self, n):  # It takes input and multiply them
        input_numbers = self.input_numbers(n)
        # Lambdas are one line functions.
        return(reduce((lambda x, y: x*y), input_numbers))

    def division(self, n):  # It takes input and divide them
        input_numbers = self.input_numbers(n)
        try:
            result = reduce((lambda x, y: x/y), input_numbers)
        except ZeroDivisionError as ZDE:
            print("You can not divide by zero,It is undefined in mathematics.")
        else:
            return(result)

    def exponent(self, n):
        input_numbers = self.input_numbers(n)
        return(reduce((lambda x, y: x**y), input_numbers))

    def logarithm(self, n):
        try:
            base = float(input("Input a float base:\n>>>"))
            base = base if base is not None or base.isfloat() else 2.0
            number = float(input("Input the number:\n>>>"))
        except Exception as e:
            print(e)
            print("Enter a number only.")
        return(math.log(number, base))

    def symbol_to_operation(self, symbol, number):
        symbols = {"+": self.summation,
                   "*": self.multiplication,
                   "/": self.division,
                   "-": self.summation,
                   "^": self.exponent,
                   "log".casefold(): self.logarithm}
        if symbol in symbols.keys():
            if symbol == "-":
                print("To subtract, input negative number.")
            result = symbols[symbol.lower()](number)
            print(result)
        else:
            print(f"You can only do following operations now. {symbols.keys()}")

if __name__ == "__main__":
    # It excute if this file is directly called not imported
    # Creating an instance of my calculator class
    calculator = Calculator()
    print("To exit, type \"q\"")
    # print("To get help type help.")
    while True:
        symbol = input("Type the symbol of operation:\n>>>")
        if symbol.lower() == "q":
            break
        elif symbol.lower() == "help":
            pass
        else:
            number = input(
                           "Type the numbers of numbers that u want to perform your operation on:\n>>>")
            if number == "":
                number = 2
            try:
                number = int(number)
            except (TypeError, ValueError) as TE:
                print("This should be a number which represent on how many numbers you want to perform operation on.")
                continue
        calculator.symbol_to_operation(symbol, number)
