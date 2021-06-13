import os, shutil

my_folders = ["photos", "movies", "games"]
destination_folder = r"C:\Work\_PythonSuli\pycore-210612\test_folder"

for i in my_folders:
    print(f"Creating folder: {i} in {destination_folder}")

    # create empty folders
    os.makedirs( os.path.join(destination_folder, i.upper()) )

    # !!!remove directories with files!!!
    #shutil.rmtree(os.path.join(destination_folder, i))