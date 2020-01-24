import itertools
import re
from core.Automata import Automata


class Parser():
    def __init__(self):
        self.__org = []
        self.__scrtpt = []
        self.__eve = ([], [])

    def parse(self, target: str):
        self.__readfile(target)
        (x, y) = self.__sep(map((lambda x: x.strip()),
                                filter((lambda x: x[0] != '#' and x[0] != '\n'),
                                       filter((lambda x: len(x) != 0), self.__org))))
        return (list(x) + ['start'] + list(y) + ['finish'])

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


class Interpreter():
    def __init__(self, sft=(0, 0)):
        self.automata = Automata("", "", sft)
        self.act = [lambda path: self.automata.select_checkpoint(path),
                    lambda path: self.automata.advance_support(path),
                    lambda x: self.automata.select_servant_skill(x),
                    lambda x, y: self.automata.select_servant_skill(x, y),
                    lambda x: self.automata.select_master_skill(x),
                    lambda x, y: self.automata.select_master_skill(x, y),
                    lambda x, y, z: self.automata.select_master_skill(x, y, z),
                    lambda: self.automata.start_battle(),
                    lambda: self.automata.finish_battle()]

    def evaluate(self, cmd: str):
        pass

    def _eval(self, cmd: str):
        if cmd == 'start':
            return 7
        if cmd == 'finish':
            return 8
        matches = [lambda x: re.match('ckp', x),
                   lambda x: re.match('spt', x),
                   lambda x: re.match('sft', x),
                   lambda x: re.match('s', x),
                   lambda x: re.match('m', x)
                   ]


def main():
    sc = Parser()
    print(sc.parse("battle.txt"))
    it = Interpreter()
