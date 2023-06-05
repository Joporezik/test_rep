# # task 1
# # point a
import math
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# y1 = ((a ** 2) / 3) + (((a ** 2) + 4) / b) + (math.sqrt((a ** 2) + 4) / 4) + ((math.sqrt(((a ** 2) + 4) ** 3)) / 4)
# print(y1)


# # point b
# sin_x = int(input("Enter sinus x: "))
# cos_x = int(input("Enter cosinus x: "))
# y2 = math.cos(math.radians(cos_x)) + math.sin(math.radians(sin_x))
# print(y2)


# # point c
# x3 = int(input("Enter x for point c: "))
# y3 = (((math.cos(math.radians(x1) ** 2)) ** 2) + ((math.sin(2 * math.radians(x1) - 1)) ** 2)) ** 1/3
# print(y3)


# # point d
# x4 = int(input("Enter x for point d: "))
# y4 = 5 * x4 + (3 * x4 ** 2) * (math.sqrt(1 + math.sin(math.radians(x4) ** 2)))
# print(y4)


# task 2
i = float(input("Annual interest rate: "))
s = int(input("Loan amount in rubles: "))
n = int(input("Count of months: "))
# p - monthly interest rate
p = i / 12 / 100
# m - monthly payment
m = (s * p * (1 + p) ** n) / (((1 + p) ** n) - 1)
total_payout = m * n
print("Monthly payment =", round(m, 2))
print("Total payout = ", round(total_payout))
print("Overpayment amount =", round(total_payout) - s)




# # task 3
# R1 = int(input("Enter the radius of the first planet: "))
# R2 = int(input("Enter the radius of the second planet: "))
# v1 = float(input("Enter the orbital velocity of the first planet: "))
# v2 = float(input("Enter the orbital velocity of the second planet: "))
#
# L1 = (2 * R1 * math.pi) / v1
# L2 = (2 * R2 * math.pi) / v2
#
# print("The length of the year on the first planet:", L1, "hours")
# print("The length of the year on the second planet:", L2, "hours")
# print("Is it true that the length of the year on the first planet is longer than on the second:", L1 > L2)



