from PIL import Image, ExifTags
from openpyxl import Workbook
import os

my_photo = r"C:\Work\_PythonSuli\pycore-210612\photos\IMG_1069.JPG"
data_file = os.path.join(  os.path.dirname(my_photo), "photo_data.xlsx"  )

# PIL opens photo
img = Image.open(my_photo)

# create workbook
workbook = Workbook()
sheet = workbook.active

# create columns
sheet["A1"] = "Name"
sheet["B1"] = "Path"
sheet["C1"] = "Size"

sheet["A3"] = os.path.basename(my_photo)
sheet["B3"] = my_photo
sheet["C3"] = str(img.size)


# save file
workbook.save(data_file)

# show image
# img.show()