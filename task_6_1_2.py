# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
# ('141.138.90.60', 'GET', '/downloads/product_2'),

my_list = []
my_dict = {}
with open('nginx.txt', 'r', encoding='utf-8') as f1:
    for line in f1:
        remote_addr = "".join(line.split(' - - ')[:1])
        if remote_addr in my_dict:
            my_dict[remote_addr] += 1
        else:
            my_dict[remote_addr] = 1
        request_type1 = line.split('] "')[1]
        request_type2 = "".join(request_type1.split(' /')[:1])
        requested_resource1 = request_type1.split(' ')[1]
        tupl = (remote_addr, request_type2, requested_resource1)
        my_list.append(tupl)
print('(<remote_addr>, <request_type>, <requested_resource>', my_list)
s_dict = sorted(my_dict.items(), key=lambda x: x[1])
print('Спамер: ', s_dict[-1][0])
print('Отправлено запросов спамером: ', s_dict[-1][1])
