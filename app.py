

print("Welcome to the simple calculator, please select from the following options:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. division")

userSelect = input("Please enter your selection: ")
if userSelect in ('1', '2', '3', '4' ):
    if userSelect == '1':
        import addition
    if userSelect == '2':
        import subtraction
    if userSelect == '3':
        import multiplication
    if userSelect == '4':
        import division