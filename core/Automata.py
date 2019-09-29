from core import util

class Automata():
    def __init__(self, wds = (0, 0), hgs = (0, 0), spt : str = None):
        self.widthShift = wds[0]
        self.heightShift = hgs[0]
        self.support = spt

    # battle related
    def select_cards(self, cards : [int]):
        pass

    def select_skill(self, skill : int):
        pass

    def select_servant(self, servant : int):
        pass

    def change_servant(self, org : int, tar : int):
        pass

    def master_skill(self, skill : int):
        pass

    # pre-battle related
    def select_checkpoint(self, checkpoint):
        pass

    def select_support(self):
        pass

    # after-battle related
    def finish_battle(self):
        pass

    # others
    def next_step(self):
        pass
