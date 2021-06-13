import os

              # raw string
folder_path = r"C:\Work\_PythonSuli\pycore-210612\alapok_01"

file_list = os.listdir(folder_path)

for file in file_list:
    print(file.upper())