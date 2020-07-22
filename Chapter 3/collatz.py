"""
The Collatz Sequence Write a function named collatz() that has one parameter named number. If number is even,
then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and
return 3 * number + 1.
"""


# Recursion-based version
def collatz(number):
    """
    Collatz the input number recursively until it reaches 1.
    """
    if number == 1:
        print('Collatz Complete. Amazing isn\'t it!')
    elif number % 2 == 0:
        print(int(number / 2))
        collatz(number / 2)
    else:
        print(int(number * 3 + 1))
        collatz(number * 3 + 1)


try:
    collatz(int(input('Choose any integer greater than 1: ')))
except ValueError:
    print('Non-Integer entered, program will exit')


# Version with extended functionality
def collatz(number):
    """
    Collatz the number and print each step and tracks the number of them.
    """
    if number > 1:
        steps = 0
        while number != 1:
            if number % 2 == 0:
                print(int(number / 2))
                number = number / 2
                steps += 1
            else:
                print(int(number * 3 + 1))
                number = number * 3 + 1
                steps += 1
        print('Collatz sequence finished in ' + str(steps) + ' steps')
    else:
        print("You entered 1. You clearly can't read"
              "so I'm shutting down before I catch your idiocy.")


try:
    collatz(int(input('Choose any integer greater than 1: ')))
except ValueError:
    print('Non-Integer entered, program will exit')
