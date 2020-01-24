import itertools


class Scripter():
    def __init__(self):
        self.__org = []
        self.__scrtpt = []
        self.__eve = ([], [])

    def parse(self, target: str):
        self.__readfile(target)
        self.__eve = self.__sep(map((lambda x: x.strip()),
                                    filter((lambda x: x[0] != '#' and x[0] != '\n'),
                                           filter((lambda x: len(x) != 0), self.__org))))

    def __readfile(self, target: str):
        file = open(target, 'r')
        try:
            lines = file.readlines()
            self.__org = lines
        finally:
            file.close()

    def __sep(self, raw: list) -> (list, list):
        prep = itertools.takewhile((lambda x: x != 'start'), raw)
        ctrl = itertools.takewhile((lambda x: x != 'finish'), itertools.dropwhile(
            (lambda x: x == 'start'), raw))
        return (prep, ctrl)

    def show(self):
        for i in self.__eve:
            print("eve: ", list(i))


if __name__ == "__main__":
    sc = Scripter()
    sc.parse("battle.txt")
    sc.show()
