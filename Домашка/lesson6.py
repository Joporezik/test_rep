# # task 1
# def binary_search(some_list, target, low, high):
#     if low > high:
#         return "Number if not found"
#     else:
#         mid = (high + low) // 2
#         if some_list[mid] == target:
#             return mid
#         elif target < some_list[mid]:
#             return binary_search(some_list, target, low, high - 1)
#         else:
#             return binary_search(some_list, target, mid + 1, high)
#
# some_list = [1, 9, 11, 34, 46, 59, 123, 241]
# print("Index:", binary_search(some_list, int(input("Enter number: ")), 0, len(some_list)))



# # task 2
# def bi_num_sys(ten_num_sys):
#     bi_str = ""
#
#     while ten_num_sys > 0:
#         bi_str = str(ten_num_sys % 2) + bi_str
#         ten_num_sys //= 2
#     return bi_str
#
# print(bi_num_sys(int(input("Enter number: "))))



# # task 3
# def prime_num(num):
#     check_num = 0
#     for el in range(1, num):
#         if num % el == 0:
#             check_num += 1
#         else:
#             pass
#     if check_num <= 1:
#         print("Your number is prime")
#     else:
#         print("You number is not prime")
# prime_num(int(input("Enter number: ")))



# # task 4
# def greatest_common_divisor(num1, num2):
#     remainder = 1
#     while remainder != 0:
#         if num1 > num2:
#             remainder = num1 % num2
#             num1 = num2
#             num2 = remainder
#         else:
#             remainder = num2 % num1
#             num2 = num1
#             num1 = remainder
#     if num1 > num2:
#         return num1
#     else:
#         return num2
# in_num1 = int(input("Enter first number: "))
# in_num2 = int(input("Enter second number: "))
# print(greatest_common_divisor(in_num1, in_num2))



# # task 5
#
# def encrypt(sent):
#     chiper = ""
#     for i in sent:
#         symb_num = ord(i)
#         if symb_num in [55, 56, 57]:
#             symb_num -= 7
#         elif symb_num in [88, 89, 90]:
#             symb_num -= 23
#         elif symb_num in [120, 121, 122]:
#             symb_num -= 23
#         elif symb_num in [1101, 1102, 1103]:
#             symb_num -= 29
#         elif symb_num in [1069, 1070, 1071]:
#             symb_num -= 29
#         elif symb_num in [45, 46, 47]:
#             symb_num += 13
#         elif symb_num in [62, 63, 64]:
#             symb_num += 29
#         elif symb_num in [94, 95, 96]:
#             symb_num -= 60
#         else:
#             symb_num += 3
#         chiper += chr(symb_num)
#     print(chiper)
#
#
# def decrypt(desent):
#     dechiper = ""
#     for i in desent:
#         desymb_num = ord(i)
#         if desymb_num in [48, 49, 50]:
#             desymb_num += 7
#         elif desymb_num in [65, 66, 67]:
#             desymb_num += 23
#         elif desymb_num in [97, 98, 99]:
#             desymb_num += 23
#         elif desymb_num in [1172, 1173, 1174]:
#             desymb_num += 29
#         elif desymb_num in [1040, 1041, 1042]:
#             desymb_num += 29
#         elif desymb_num in [33, 34, 35]:
#             desymb_num += 60
#         elif desymb_num in [58, 59, 60]:
#             desymb_num += 13
#         elif desymb_num in [91, 92, 93]:
#             desymb_num -= 31
#         else:
#             desymb_num -= 3
#         dechiper += chr(desymb_num)
#     print(dechiper)
#
# sentense = input("Enter yout sentense: ")
# choise = int(input("If you want to encrypt press 1, decrypt - press 2: "))
#
# if choise == 1:
#     encrypt(sentense)
# elif choise == 2:
#     decrypt(sentense)
# else:
#     print("You have crooked hands")



# # task 6
# def encrypt_vigenere(sent, keys):
#     if len(sent) > len(keys):
#         keys_len = (len(sent) // len(keys)) + 1
#         keys = keys * keys_len
#         keys = keys[:len(sent)]
#     encrypt_word = ""
#     for symb, key in zip(sent, keys):
#         encrypt_symb = (ord(symb) + (ord(key) - 65))
#         if encrypt_symb > 90:
#             encrypt_symb -= 26
#         encrypt_word += chr(encrypt_symb)
#     return encrypt_word
#
# def decrypt_vigenere(sent, keys):
#     if len(sent) > len(keys):
#         keys_len = (len(sent) // len(keys)) + 1
#         keys = keys * keys_len
#         keys = keys[:len(sent)]
#     decrypt_word = ""
#     for symb, key in zip(sent, keys):
#         decrypt_symb = (ord(symb) - (ord(key) - 65))
#         if decrypt_symb < 65:
#             decrypt_symb += 26
#         decrypt_word += chr(decrypt_symb)
#     return decrypt_word
#
# sentense = input("Enter your sentense: ")
# key = input("Enter your key: ")
# choise = int(input("If you want to encrypt press 1, decrypt - press 2: "))
#
# if choise == 1:
#     print(encrypt_vigenere(sentense, key))
# elif choise == 2:
#     print(decrypt_vigenere(sentense, key))
# else:
#      print("You have crooked hands")


import random
# task 7
def random_matrix(M, N, min_num, max_num):
    matrix = [[random.randint(min_num, max_num) for i in range(N)] for j in range(M)]
    matr = []
    for el in matrix:
        matr.append(el)
    return matr
for row in random_matrix(4, 5, 0, 10):
    print(row)
print("")


# # task 8
# def max_min_elem_in_matrix(matrix, M, N):
#     min_elem = matrix[0][0]
#     max_elem = matrix[0][0]
#     min_index = {'i': None, 'j': None}
#     max_index = {'i': None, 'j': None}
#     for i in range(M):
#         for j in range(N):
#             if matrix[i][j] > max_elem:
#                 max_elem = matrix[i][j]
#                 max_index['i'] = i
#                 max_index['j'] = j
#
#             elif matrix[i][j] <= min_elem:
#                 min_elem = matrix[i][j]
#                 min_index['i'] = i
#                 min_index['j'] = j
#     max_ind = []
#     min_ind = []
#     for key, value in max_index.items():
#         max_ind.append(value)
#     for key, value in min_index.items():
#         min_ind.append(value)
#
#     print("Max index:", max_ind)
#     print("Min index:", min_ind)
#
# matr = random_matrix(4, 5, 0, 10)
# for row in matr:
#     print(row)
# max_min_elem_in_matrix(matr, 4, 5)
# print("")
#
#
#
# # task 9
# def sum_el_matrix(matr, M, N):
#     sum = 0
#     for i in range(M):
#         for j in range(N):
#             sum += matr[i][j]
#     print("Sum elements of matrix:", sum)
#
#     for i in range(M):
#         sum_column = 0
#         for j in range(N):
#             sum_column += matr[i][j]
#         print("Column percent:", sum_column / sum * 100)
#
# matr = random_matrix(4, 5, 0, 10)
# for row in matr:
#     print(row)
#
# print(sum_el_matrix(matr, 4, 5))
#
#
# # task 10
# def mul_k_column_el(matr, M, N, K):
#     for i in range(M):
#         elem = matr[i][K]
#         for j in range(N):
#             matr[i][j] *= elem
#
#     for row in matr:
#         print(row)
#
# matr = random_matrix(4, 5, 0, 10)
# for row in matr:
#     print(row)
#
# K = int(input("Enter K column from 0 to 4: "))
# print("Matrix after multiplication by K column:")
# mul_k_column_el(matr, 4, 5, K)


# # task 11
# def sum_l_line_el(matr, M, N, L):
#     for i in range(M):
#         for j in range(N):
#             elem = matr[L][j]
#             matr[i][j] += elem
#
#
#     for row in matr:
#         print(row)
#
# matr = random_matrix(4, 5, 0, 10)
# for row in matr:
#     print(row)
#
# L = int(input("Enter L line from 0 to 3: "))
# print("Matrix after sum by L line:")
# sum_l_line_el(matr, 4, 5, L)


# #task 12
# def search_num_in_matrix(matr, M, N, H):
#
#     for i in range(M):
#         for j in range(N):
#             if matr[i][j] == H:
#                 print(f"{range(N).index(j)} column has {H} ")
#
# matr = random_matrix(4, 5, 0, 10)
# for row in matr:
#     print(row)
# H = int(input("Enter the desired number: "))
# search_num_in_matrix(matr, 4, 5, H)


# # task 13
# def sum_dia_el(matr, M, N):
#     main_sum = 0
#     sec_sum = 0
#     for i in range(M):
#         for j in range(N):
#             main_sum += matr[i][i]
#             sec_sum += matr[i][N - i - 1]
#             break
#     print("The sum of the elements of the main diagonal:", main_sum)
#     print("The sum of the elements of the secondary diagonal", sec_sum)
#
# matr = random_matrix(4, 5, 0, 10)
# for row in matr:
#     print(row)
#
# sum_dia_el(matr, 4, 5)


# task 14
def even_count_1_in_matrix(matr, M):
    for i in range(M):
        if matr[i].count(1) % 2 == 0:
            matr[i].append(0)
        else:
            matr[i].append(1)
    for row in matr:
        print(row)

matr = random_matrix(4, 5, 0, 1)
for row in matr:
    print(row)
print("")
even_count_1_in_matrix(matr, 4)