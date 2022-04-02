from itertools import zip_longest
import json

new_dict = {}

with open('users.csv', 'r+', encoding='utf-8') as f1:
    with open('hobby.csv', 'r+', encoding='utf-8') as f2:
        with open('users_hobbies.json', 'w', encoding='utf-8') as f3:
            users = f1.readlines()
            hobbies = f2.readlines()
            new_dict = dict(zip_longest(users, hobbies[:len(users)], fillvalue='None'))
            print(new_dict)
            new_dict_as_str = json.dumps(new_dict)
            f3.write(new_dict_as_str)

with open('users_hobbies.json', 'r', encoding='utf-8') as f:
    check = json.load(f)
    print('Проверка загрузки из json: ', check)
