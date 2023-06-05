# # task 1
# lst = [1, 2, 3]
# print(list(map(lambda x: f"{x}", lst)))


# # task 2
# lst = [1, 5, 7, 19, -2, -1, -15, 4, 6, 0]
# print(list(filter(lambda x: x > 0, lst)))


# # task 3
# lst = ["aboba", "notaboba", "level", "Artem"]
# print(list(filter(lambda x: x == x[::-1], lst)))


# # task 4
# import time
# def timer(input_func):
#     def output_func():
#         befor = float(time.time())
#         input_func()
#         after = float(time.time())
#         print(after - befor)
#     return output_func
#
#
# @timer
# def hello():
#     print("Hello")
#
# hello()


# # task 5
# from functools import reduce
# rooms = [
# 	{"name" : "Kitchen", "length": 6, "width": 4},
# 	{"name" : "Room 1", "length": 5.5, "width": 4.5},
# 	{"name" : "Room 2", "length": 5, "width": 4},
# 	{"name" : "Room 3", "length": 7, "width": 6.3},
# ]
# room_area = list(map(lambda x: x["length"] * x["width"] , rooms))
# print("Rooms area:", reduce(lambda x, y: x + y, room_area))




