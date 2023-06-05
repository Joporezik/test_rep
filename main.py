# import json
#
#
# data = {
#     "employers":
#         [
#             {
#                 "name": "John",
#                 "salary": 1000
#             },
#             {
#                 "name": "John",
#                 "salary": 900
#             },
#             {
#                 "name": "John",
#                 "salary": 1500
#             }
#
#         ]
# }
#
# with open("employers.json", "w") as j_file:
#     json.dump(data, j_file, indent=4)


# import csv
#
# with open("employers.csv", "r", encoding="utf-8") as r_file:
#     file_reader = csv.DictReader(r_file, delimiter=',')
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {','.join(row)}")
#         else:
#             print(f"    {row['Имя']} - {row['Профессия']} - {row['Год рождения']}")
#         count += 1
#     print(f"Total: {count} lines")





