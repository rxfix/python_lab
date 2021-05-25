<<<<<<<<< Temporary merge branch 1
ццц
=========
import os

root_dir = './'

__step__ = 1
# # for file in os.listdir(root_dir):

# #     print(type(file))
# #     print(file, os.path.isdir(file))
# #     print(file, os.path.isfile(file))
#
# for item in os.scandir(root_dir):
#     print(type(item))
#     # print(dir(item))
#     print(item.name, item.is_file())
#     print(item.name, item.is_dir())
#     print(item.name, item.stat())

__step__ = 2
# for root, dirs, files in os.walk(root_dir):
#     # print(files)
#     # print(type(root))
#     for file in files:
#         # print(root, file)
#         f_path = os.path.join(root, file)
#         print(f_path, os.path.exists(f_path))
#         print(os.stat(f_path).st_size)
#         print(os.path.abspath(f_path))
#         print(os.path.split(f_path))

__step__ = 3
ROOT = os.path.abspath(os.path.join(__file__, '..'))
print(ROOT)
print(os.listdir(ROOT))
>>>>>>>>> Temporary merge branch 2
