import addition
import subtraction
import multiplication
import division

print("Select a function")
print("1. Add")
print("2. Minus")
print("3. Times")
print("4. Divide")

userSelect = input("Select 1 or 2 or 3 or 4 : ")
if userSelect in ('1', '2', '3', '4' ):
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    if userSelect == '1':
        print(number1 + number2)
    elif userSelect == '2':
        print(number1 - number2)
    elif userSelect == '3':
        print(number1 * number2)
    elif userSelect == '4':
        print(number1 / number2)