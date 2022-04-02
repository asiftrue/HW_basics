from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as f:
    pars = argv
    if len(pars) == 1:
        print(f.read())
    elif len(pars) == 2:
        for line in f.readlines()[int(argv[1]) - 1:]:
            print(line, end='')
    elif len(pars) == 3:
        i = 0
        for line in f:
            i += 1
            if i >= int(argv[1]):
                if i > int(argv[2]):
                    break
                print(line, end='')
