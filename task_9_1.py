import time


class TrafficLIght:
    def __init__(self, colour):
        self.__colour = 'black'

    def running(self):
        self.__colour = 'RED'
        print(f'\033[3m\033[30m\033[41m{self.__colour}\033[0m')
        time.sleep(7)
        self.__colour = 'YELLOW'
        print(f'\033[3m\033[30m\033[43m{self.__colour}\033[0m')
        time.sleep(2)
        self.__colour = 'GREEN'
        print(f'\033[3m\033[30m\033[42m{self.__colour}\033[0m')
        time.sleep(2)
        # print(f'\033[42m"END"')


lights = TrafficLIght('red')
lights.running()
