import os
import json

ROOT = os.path.dirname(__file__)

with open('config.json', 'r', encoding='utf-8') as f:
    dir_dict = json.load(f)

print(dir_dict)

for d_path in dir_dict:
    ab_path = os.path.join(ROOT, d_path)
    if not os.path.exists(ab_path):
        os.makedirs(ab_path)
        for name in dir_dict[d_path]:
            with open(os.path.join(ab_path, name), 'x', encoding= 'utf-8'):
                pass




