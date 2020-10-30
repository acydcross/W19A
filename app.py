import addition
import subtraction
import multiplication
import division

print("Welcome to the simple calculator, please select from the following options:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

userSelect = input("Please enter your selection: ")
if userSelect in ('1', '2', '3', '4' ):
    number1 = int(input("Please enter your first number: "))
    number2 = int(input("Please enter your second number: "))
    if userSelect == '1':
        print("Your result: ", (number1 + number2))
    elif userSelect == '2':
        print("Your result: ", (number1 - number2))
    elif userSelect == '3':
        print("Your result: ", (number1 * number2))
    elif userSelect == '4':
        print("Your result: ", (number1 / number2))