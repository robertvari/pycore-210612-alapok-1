from PIL import Image, ExifTags
from openpyxl import Workbook
import os


photo_folder = r"C:\Work\_PythonSuli\pycore-210612\photos"
file_list = os.listdir(photo_folder)

photo_list = [i for i in file_list if ".jpg" in i.lower()]

data_file = os.path.join(photo_folder, "photo_data.xlsx")

# create workbook
workbook = Workbook()
sheet = workbook.active

# create columns
sheet["A1"] = "Name"
sheet["B1"] = "Path"
sheet["C1"] = "Size"

for image_name in photo_list:

    # PIL opens photo
    img = Image.open( os.path.join(photo_folder, image_name) )


sheet["A3"] = os.path.basename(my_photo)
sheet["B3"] = my_photo
sheet["C3"] = str(img.size)


# save file
workbook.save(data_file)