# # task 1
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
#
# print(num1 + num2 + num3)
# print(num1 - num2 - num3)
# print(num1 * num2 * num3)
# print(num1 - num2 + num3)
# print(num1 * num2 / num3)
# print((num1 + num2) % num3)


# # task 2
# cat_a = int(input("Enter first leg: "))
# cat_b = int(input("Enter second leg: "))
#
# print("Square =", (cat_a * cat_b)/2 )
# print("Hypotenuse =", (cat_a ** 2 + cat_b ** 2)**0.5)


# # task 3
# text = input("Write your text: ")
# space = text.count(" ")
# if space > 0:
#     print("Your text consists of", space + 1, "words")
# else:
#     print("Your text consists of", space + 1, "word")


# # task 4
# string = input("Write your word: ")
# print(string[0] + string[1:-1].replace("h","H") + string[-1])


# # task 5
# string = input("Write string: ")
#
# print(string[2])
# print(string[-2])
# print(string[:5])
# print(string[:-2])
# print(string[::2])
# print(string[1::2])
# print(string[::-1])
# print(string[::-2])
# print(len(string))


# # task 6
# number = int(input("Enter number: "))
# print("Last numeral:", number % 10)


# # task 7
# num = int(input("Enter three-digit number: "))
# print("Count of decade:", (num % 100)// 10)

#
# # task 8
# num = int(input("Enter three-digit number: "))
# print("Summ of numerals:", (num // 100) + ((num % 100)// 10) + (num % 10))