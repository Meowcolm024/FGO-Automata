import time, random
from core import util, crds

class Automata():
    def __init__(self, ckp : str, spt : str = None, sft = (0, 0)):
        self.shifts = sft
        self.checkpoint = ckp
        self.support = spt

    # battle related
    def select_cards(self, cards : [int]):
        if not util.standby(util.get_sh(self.shifts), "assets/attack.png"):
            time.sleep(0.2)
        # tap ATTACK
        self.tap(crds.ATTACK, 100, 100)
        time.sleep(0.5)
        while len(cards) < 3:
            x = random.randrange(1, 6)
            if x in cards:
                continue
            cards.append(x)
        # tap CARDS
        for card in cards:
            self.tap(crds.CARDS[card-1], 50, 100)
            time.sleep(0.2)

    def select_servant_skill(self, skill : int):
        if not util.standby(util.get_sh(self.shifts), "assets/attack.png"):
            time.sleep(0.2)
        self.tap(crds.SERVANT_SKILLS[skill-1])

    def select_servant(self, servant : int):
        pass

    def change_servant(self, org : int, tar : int):
        pass

    def show_master_skill(self):
        if not util.standby(util.get_sh(self.shifts), "assets/attack.png"):
            time.sleep(0.2)
        self.tap(crds.MASTER)

    def select_master_skill(self, skill : int):
        self.tap(crds.MASTER_SKILLS[skill-1])

    # pre-battle related
    def select_checkpoint(self, ckp : str = None):
        if ckp is None:
            ckp = self.checkpoint
        pass

    def select_support(self, spt : str = None):
        if spt is None:
            spt = self.support
        pass

    # after-battle related
    def finish_battle(self):
        pass

    # others
    def next_step(self):
        pass

    def tap(self, crd : (int, int), i : int = 10, j : int = 10):
        x = crd[0] + self.shifts[0]
        y = crd[1] + self.shifts[1]
        util.tap(util.shifter((x, y), i, j))
