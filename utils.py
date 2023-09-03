import os

def get_image_filenames(folder_path):
    return [f for f in sorted(os.listdir(folder_path)) if f.endswith('.jpeg')]

folder_path = "/Users/a.j.llano/Desktop/randomsoftware/Council/images"  # Replace this with the path to your image folder
image_filenames = get_image_filenames(folder_path)
print(image_filenames)  