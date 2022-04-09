# Написать функцию email_parse(<email_address>), которая при помощи регулярного
# выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
# виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
import re

PAT = re.compile(r'(?P<name>[a-z]+)[@](?P<domen>[a-z]+\.[a-z]+)')


def email_parse(text):
    result_iter = PAT.finditer(text)
    # print(*result_iter)
    if re.fullmatch(PAT, text):
        print("Valid email")
        for res in result_iter:
            a = res.groupdict()
            return a
    else:
        print("Invalid email")
        raise ValueError(f'wrong format {text}')


if __name__ == "__main__":
    print(email_parse('somename@mail.ru'))
    print(email_parse('somename@mailru'))
    # print(email_parse(input('Введите адрес эл. почты: ')))
