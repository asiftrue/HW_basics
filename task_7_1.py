import os

ROOT = os.path.dirname(__file__)

project = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for item in range(len(folders)):
    dir_name = f'{project}/{folders[item]}'
    print(dir_name)
    dir_path = os.path.join(ROOT, dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

