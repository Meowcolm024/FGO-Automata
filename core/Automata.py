import time
from core import util

class Automata():
    def __init__(self, ckp : str, spt : str = None, sft = (0, 0)):
        self.shifts = sft
        self.checkpoint = ckp
        self.support = spt

    # battle related
    def select_cards(self, cards : [int]):
        pass

    def select_servant_skill(self, skill : int):
        pass

    def select_servant(self, servant : int):
        pass

    def change_servant(self, org : int, tar : int):
        pass

    def show_master_skill(self):
        pass

    def select_master_skill(self, skill : int):
        pass

    # pre-battle related
    def select_checkpoint(self, ckp = self.checkpoint):
        pass

    def select_support(self, spt = self.support):
        pass

    # after-battle related
    def finish_battle(self):
        pass

    # others
    def next_step(self):
        pass

    def tap(self, crd : (int, int), shift : int = 10):
        x = crd[0] + self.widthShift
        y = crd[1] + self.heightShift
        util.tap(util.shifter((x, y), shift))
