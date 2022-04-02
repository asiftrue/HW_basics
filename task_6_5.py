from itertools import zip_longest
import sys

new_dict = {}
users = []
hobbies = []
name1 = sys.argv[1]
name2 = sys.argv[2]
name3 = sys.argv[3]
with open(name1, 'r+', encoding='utf-8') as f1:
    with open(name2, 'r+', encoding='utf-8') as f2:
        with open(name3, 'w', encoding='utf-8') as f3:
            for line in f1:
                # line = line.replace('\n', '')
                x = line.strip('\n')
                users.append(x)
            for row in f2:
                y = row
                hobbies.append(y)
            new_dict = dict(zip_longest(users, hobbies[:len(users)], fillvalue='None'))
            print(new_dict)
            for key, val in new_dict.items():
                f3.write('{}: {}\n'.format(key, val))
                # print('{}: {}\n'.format(key, val))
