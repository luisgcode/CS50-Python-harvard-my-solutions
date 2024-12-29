str = input("expression: ")
integerOne, operator, integerTwo = str.split(" ")

first_value = int(integerOne)
second_value = int(integerTwo)

if operator == '+':
    final = int(first_value + second_value)
elif operator == '-':
    final = first_value - second_value
elif operator == '*':
    final = first_value * second_value
elif operator == '/':
    final = first_value / second_value
else:
    print("Insert right information")


print(float(final))
