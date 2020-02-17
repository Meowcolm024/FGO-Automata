import itertools
import re
from core.Automata import Automata


class Parser():
    def __init__(self):
        self.__org = []

    def parse(self, target: str) -> [str]:
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
    def __init__(self):
        self.automata = Automata("", "")
        self.__help = \
        """
    Commands:

        help                -- show help
        show                -- show info
        shot                -- get screenshot

    Settings:

        sft=(,)             -- set shifts [eg: sft=(248,0)]
        ckp=""              -- set checkpoint [eg: ckp="assets/Qp4.png"]
        spt=""              -- set support [eg: spt="assets/eg-sp1.png"]

    Actions:

        start               -- start battle
        finish              -- finish battle
        s[1-9]              -- servant skill [eg: s1]
        s[1-9]t[1-3]        -- seravnt skill w/ target [eg: s5t3]
        m[1-3]              -- master skill [eg: m1]
        m[1-3]t[1-3]        -- master skill w/ target [eg: m2t1]
        m3o[1-3]t[1-3]      -- Order Change [eg: m3o1t2]
        c[1-8]+             -- select cards [eg: c1] [eg: c723] 
        """

    def evaluate(self, cmd: str):
        return self._eval(cmd)

    def _eval(self, cmd: str):
        if cmd == 'shot':
            s = self.automata.aquire_screenshot()
            return 'Get screenshot: ' + s

        if cmd == 'show':
            return self.automata

        if cmd == 'help':
            return self.__help

        if cmd == 'finish':
            self.automata.finish_battle()
            return 'Finish battle'

        if cmd == 'start':
            self.automata.quick_start()
            return 'Quick start'

        if re.match(r'sft=\([0-9]+,[0-9]+\)', cmd) != None:
            out0 = cmd.split('(')[1].split(',')
            out = [out0[0], out0[1].split(')')[0]]
            self.automata.reset_shifts((int(out[0]), int(out[1])))
            return ('Reset shifts to ' + str(out))

        if re.match(r'spt="[^\s]*"', cmd) != None:
            out = cmd.split('\"')[1]
            self.automata.reset_support(str(out))
            return ('Reset support to ' + out)

        if re.match(r'ckp="[^\s]*"', cmd) != None:
            out = cmd.split('\"')[1]
            self.automata.reset_checkpoint(out)
            return ('Reset checkpoint to ' + out)

        if re.match(r's[1-9]t[1-3]', cmd) != None:
            out = [cmd[1], cmd[3]]
            self.automata.select_servant_skill(int(out[0]), int(out[1]))

            return ('Servant skill: ' + out)
        if re.match(r'^s[1-9]$', cmd) != None:
            out = cmd[1]
            self.automata.select_servant_skill(int(out))
            return ('Servant skill: ' + out)

        if re.match(r'm3o[1-3]t[1-3]', cmd) != None:
            out = [cmd[3], cmd[5]]
            self.automata.select_master_skill(3, int(out[0]), int(out[1]))
            return ('Master skill: ' + out)

        if re.match(r'm[1-3]t[1-3]', cmd) != None:
            out = [cmd[1], cmd[3]]
            self.automata.select_master_skill(int(out[0]), int(out[1]))
            return ('Master skill: ' + str(out))

        if re.match(r'^m[1-3]$', cmd) != None:
            out = cmd[1]
            self.automata.select_master_skill(int(out))
            return ('Master skill: ' + out)

        if re.match(r'c[1-8]+', cmd) != None:
            out0 = cmd.split('c')[1]
            out = map(lambda x: int(x), out0)
            self.automata.select_cards(list(out))
            return ('Select cards: ', out0)

        return "ERROR: Invalid Input"


class Repl():
    def __init__(self):
        self.itp = Interpreter()

    def main_loop(self):
        print("FGO-Automata REPL")
        while True:
            cmd = input("*> ")
            print(self.itp.evaluate(cmd.replace(' ', '')))

    def load_file(self, raw: str):
        par = Parser()
        out = par.parse(raw)
        print("FGO-Automata REPL")
        print("Executing:", raw)
        for i in out:
            self.itp.evaluate(i)
