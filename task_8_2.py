import re

pattern = re.compile(
    r'(?P<addr>\d+\.\d+\.\d+\.\d+)\s[-]\s[-]\s[\[](?P<datetime>\d+[/]\w+[/]\d{4}[:]\d{2}[:]\d{2}[:]\d{2}[ ][+]\d{4})[]]\s["](?P<type>[A-Z]{2,})\s(?P<res>[/][a-z]+[/]\w+\d)\s\w{4}[/]\d\.\d["]\s(?P<code>\d+)\s(?P<size>\d+)')
with open('nginx.txt', 'r', encoding='utf-8') as f:
    for line in f:
        result = pattern.finditer(line)
        for res in result:
            print(res.groups())
#
