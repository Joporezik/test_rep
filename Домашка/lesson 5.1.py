number1 = int(input("Enter first number"))
number2 = (input("Enter second number"))
print(f"""{number1}
*
{number2}
___________""")
for el in number2[::-1]:
    product = int(el) * number1
    if el == number2[-1]:
        print(product)
    else:
        print(f'+ \n{product}')
    number1 *= 10
print("__________")
print((number1 * int(number2))/ (10 ** len((number2))))

