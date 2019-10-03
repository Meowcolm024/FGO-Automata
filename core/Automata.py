import time, random
from core import util, crds

class Automata():
    def __init__(self, ckp : str, spt : str = None, sft = (0, 0)):
        self.shifts = sft
        self.checkpoint = ckp
        self.support = spt

    # battle related
    def select_cards(self, cards : [int]):
        while not util.standby(util.get_sh(self.shifts), "assets/attack.png"):
            time.sleep(0.2)
        # tap ATTACK
        self.tap(crds.ATTACK, 100, 100)
        time.sleep(1)
        while len(cards) < 3:
            x = random.randrange(1, 6)
            if x in cards:
                continue
            cards.append(x)
        # tap CARDS
        for card in cards:
            self.tap(crds.CARDS[card-1], 50, 100)
            time.sleep(0.2)

    # new: self, skill, tar
    # combine select servant
    def select_servant_skill(self, skill : int, tar :int = 0):
        while not util.standby(util.get_sh(self.shifts), "assets/attack.png"):
            time.sleep(0.2)
        self.tap(crds.SERVANT_SKILLS[skill-1], 8, 8)
        time.sleep(1)
        if tar != 0:
            self.select_servant(tar)

    def select_servant(self, servant : int):
        while not util.standby(util.get_sh(self.shifts), "assets/select.png"):
            time.sleep(0.2)
        self.tap(crds.TARGETS[servant-1], 150, 150)

    def change_servant(self, org : int, tar : int):
        while not util.standby(util.get_sh(self.shifts), "assets/order_change.png"):
            time.sleep(0.2)
        self.tap(crds.SERVANTS[org-1], 90, 90)
        time.sleep(0.1)
        self.tap(crds.SERVANTS[tar-1], 90, 90)
        time.sleep(0.1)
        self.tap((950, 950), 100) # confirm btn

    def show_master_skill(self):
        while not util.standby(util.get_sh(self.shifts), "assets/attack.png"):
            time.sleep(0.2)
        self.tap(crds.MASTER)

    # new: self, skill, org, tar
    # combine select servant
    def select_master_skill(self, skill : int, org : int = 0, tar : int = 0):
        self.tap(crds.MASTER_SKILLS[skill-1], 8, 8)
        if org != 0 and tar == 0:
            self.select_servant(org)
        elif org != 0 and tar != 0:
            self.change_servant(org, tar)

    # pre-battle related
    def select_checkpoint(self, ckp : str = None):
        if ckp is None:
            ckp = self.checkpoint
        crds = util.get_crd(util.get_sh(self.shifts), self.checkpoint)
        self.tap(crds[0], 100)
        time.sleep(0.5)

    def select_support(self, spt : str = None):
        if spt is None:
            spt = self.support
        x = util.get_crd(util.get_sh(self.shifts), spt)
        print(x)
        if len(x) == 0:
            self.tap((860, 430), 300, 100)
        else:
            self.tap(x[0])

    # after-battle related
    def finish_battle(self):
        while not util.standby(util.get_sh(self.shifts), "assets/item.png"):
            xs = util.get_crd(util.get_sh(self.shifts), "assets/close.png")
            if len(xs) != 0:
                self.tap(xs[0])
            self.tap((960, 540), 400, 200)
            time.sleep(0.2)
        time.sleep(0.2)
        x = util.get_crd(util.get_sh(self.shifts), "assets/item.png")
        self.tap(x[0])

    # others
    def start_battle(self):
        while not util.standby(util.get_sh(self.shifts), "assets/start.png"):
            time.sleep(0.2)
        x = util.get_crd(util.get_sh(self.shifts), "assets/start.png")
        self.tap(x[0])

    def quick_start(self):
        self.select_checkpoint()
        self.select_support()
        self.start_battle()

    def tap(self, crd : (int, int), i : int = 10, j : int = 10):
        x = crd[0] + self.shifts[0]
        y = crd[1] + self.shifts[1]
        util.tap(util.shifter((x, y), i, j))
