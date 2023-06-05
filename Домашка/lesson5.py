from math import radians, factorial

# #task 1 point a
# x = radians(int(input("Enter the sine angle: ")))
# n = 0
# summa = 0
# eps = 0.0001
# next_part = 1
#
# while abs(next_part) > eps:
#     next_part = (-1) ** n * (x ** (2 * n + 1)) / factorial(2 * n + 1)
#     summa += next_part
#     n += 1
#
# print(summa)

# # task 1 point b
# x = radians(int(input("Enter cosine angle: ")))
# n = 0
# summa = 0
# eps = 0.0001
# next_part = 1
#
# while abs(next_part) > eps:
#     next_part = (-1) ** n * (x ** (2 * n)) / factorial(2 * n)
#     summa += next_part
#     n += 1
#
# print(round(summa, 2))


# # task 2
# N = int(input("Enter summ: "))
# k = int(input("Enter payment: "))
# initial_capital = 0
# days = 0
# while initial_capital < N:
#     days += 1
#     if days % 7 == 0:
#         pass
#     else:
#         initial_capital += k
# print(f'You need {days} days, or {round(days / 7, 2)} weeks, or {round(days / 365, 2)} years.')


# # task 3
# fibonacci = [1, 1]
# lenght = int(input("Enter the length of the fibonacci series: "))
# if lenght == 1:
#     print("1")
# else:
#     for el in range(lenght - 2):
#         number = fibonacci[el] + fibonacci[el + 1]
#         fibonacci.append(number)
#     print(*fibonacci)



# # task 4
# list_ = list(map(int, input("Enter numbers separated by spaces: ").split()))
# summ = 0
# maxi = list_[0]
# mini = list_[0]
# for el in list_:
#     summ += el
#     if el > maxi:
#         maxi = el
#     elif el < mini:
#         mini = el
# print(f'Summ = {summ}, max = {maxi}, min = {mini}')



# # task 5
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# count_elements = 0
# for el in numbers:
#     count_numbers = numbers.count(el)
#     if numbers.count(el) > 1:
#         for elem in range(count_numbers):
#             numbers.remove(el)
#         print(f'Number {el} occurs {count_numbers} times')
#     else:
#         count_elements += 1
# if count_elements == len(numbers):
#     print("All numbers are unique")



# # task 6
# list_ = list(map(int, input("Enter numbers in ascending order separated by a space: ").split()))
# value = int(input("Enter the desired number: "))
#
# mid = len(list_) // 2
# low = 0
# high = len(list_) - 1
#
# while list_[mid] != value and low <= high:
#     if value > list_[mid]:
#         low = mid + 1
#     else:
#         high = mid - 1
#     mid = (low + high) // 2
#
# if low > high:
#     print("No value")
# else:
#     print("Index =", mid)



# # task 7
# def shifted_binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         if arr[mid] == target:
#             return mid
#         # Если левая половина отсортирована
#         if arr[low] <= arr[mid]:
#             # Если цель в левой половине
#             if arr[low] <= target < arr[mid]:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         else:
#             # Если цель в правой половине
#             if arr[mid] < target <= arr[high]:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#     return None
#
#
# my_list = [4, 0, 1, 2, 3]
# print(shifted_binary_search(my_list, 0))  # Вывод: 1
# print(shifted_binary_search(my_list, 3))  # Вывод: None

