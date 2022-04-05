import os

ROOT = os.path.dirname(__file__)

def get_num(dir_path):
    files_dic = {}
    for root, dors, files in os.walk(dir_path):
        # print(files)
        for file in files:
            it_size = os.stat(os.path.join(root, file)).st_size
            key = get_key(it_size)
            if key not in files_dic:
                files_dic[key] = 1
            files_dic[key] += 1
    if not files_dic:
        raise Exception('Нет файлов')
    return(files_dic)

def get_key(size):
    num_digits = 1
    while True:
        if size // 10:
            num_digits += 1
        else:
            break
        size //= 10
    return 10 ** num_digits

if __name__ == "__main__":
    dir_path = os.path.join(ROOT, 'some_data')
    print(get_num(dir_path))
