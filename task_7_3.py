import os
from shutil import copy

ROOT = os.path.dirname(__file__)
main_folder = "my_project"
main_path = os.path.join(ROOT, main_folder)
new_folder = "all_templates"
new_path = os.path.join(main_folder, new_folder)

if not os.path.exists(new_path):
    os.makedirs(new_path)

for root, dirs, files in os.walk(main_folder):
    if root.count('templates'):
        for dir_ in dirs:
            if not os.path.exists(os.path.join(new_path, dir_)):
                os.makedirs(os.path.join(new_path, dir_))
        for file in files:
            src = os.path.join(root, file)
            dst = os.path.join(new_path, os.path.basename(root))
            if not os.path.exists(os.path.join(new_path, dir_, file)):
                copy(src, dst)