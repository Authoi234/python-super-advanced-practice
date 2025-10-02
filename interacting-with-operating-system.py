import os
import glob
import shutil
import platform

# uname_info = platform.uname()
# print(f"System: {uname_info.system}")
# print(f"Node Name: {uname_info.node}")
# print(f"Release: {uname_info.release}")
# print(f"Version: {uname_info.version}")
# print(f"Machine: {uname_info.machine}")
# print(f"Processor: {uname_info.processor}")

# print(f"absolute path of this file: {os.getcwd()}")

# image_directory="files/images"
# if not os.path.exists(image_directory):
#     os.makedirs(image_directory) # make a folder name files then make another folder inside it named images if not exist

# def get_files_and_directories(path):
#     files = []
#     dirs = []
#     with os.scandir(path) as it:
#         for entry in it:
#             if entry.name.startswith("."):
#                 continue
#             if entry.is_dir():
#                 dirs.append(entry.path)
#             elif entry.is_file():
#                 files.append(entry.path)
#     print(files, dirs)
#     return files, dirs

# def traverse_dir(path):
#     all_files=[]
#     all_dirs=[path]
#     while len(all_dirs) > 0:
#         d=all_dirs.pop(0)
#         # print(d, "traversing")
#         files, dirs = get_files_and_directories(d)
#         all_files.extend(files)
#         all_dirs.extend(dirs)

# traverse_dir("C:\Projects")


# file_list = glob.glob("./**/Counter.py", recursive=True)
# print(file_list)
# print("total", len(file_list), "files found")

# source_directory = "E:\\Project (old)\\PythonSuperAdvancedPractice\\hudahui"
# destination_directory = "E:\\Project (old)\\PythonSuperAdvancedPractice\\files\\images"

# try:
#     shutil.copytree(source_directory, destination_directory)
# except FileExistsError as err:
#     print(err)
# except:
#     print("Unknown error - terminating program!")
#     raise


# base_dir = "E:\\Project (old)\\PythonSuperAdvancedPractice"
# file_name = "multiproccessing-multithreading.py"
# file_path = os.path.join(base_dir, file_name)
# print("file path:", file_path)

# directory_name = os.path.dirname(file_path)
# print("directory:", directory_name)

# directory_name, file_name = os.path.split(file_path)
# print("Directory:", directory_name)
# print("file:", file_name)

# First set api key like this in a bash or bash-like terminal $ export APIKey="abcd1234"  
print(os.getenv("APIKey", default="Default value if no api key found"))