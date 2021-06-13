import os

photo_folder = r"C:\Work\_PythonSuli\pycore-210612\photos"
file_list = os.listdir(photo_folder)

photo_list = [i for i in file_list if ".jpg" in i.lower()]

# for i in file_list:
#     if ".jpg" not in i.lower():
#         print(f"{i} skipped")
#         continue
#
#     photo_list.append(i)

print(photo_list)