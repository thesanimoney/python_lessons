number1 = int(input('Please enter first number'))
number2 = int(input('Please enter second number'))
operator = input('Please enter operator')

if '/' in operator:
    x = number1 / number2
    print('your result ', x)

elif '*' in operator:
    x = number1 * number2
    print('your result ', x)

elif '+' in operator:
    x = number1 + number2
    print('your result ', x)

elif '-' in operator:
    x = number1 - number2
    print('your result ', x)