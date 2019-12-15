import time
import random
from core import util, crds


class Automata():
    def __init__(self, ckp: str, spt: str = None, sft=(0, 0)):
        """
        Parameters
        ----------
            ckp: str
        Path to the checkpoint image
        
            spt: str
        Path to the support image

            sft: (int, int), optional
        Coordinate shifts in (x, y). When there are blues straps at the edges.
        """
        self.shifts = sft
        self.checkpoint = ckp
        self.support = spt
        self.counts = 0 # apple counts
        self.apple = ""

    # battle related
    def select_cards(self, cards: [int]):
        """ Select Order Cards
        Parameters
        ----------
            cards: [int]
        A list of numbers of the card id (1~5 -> normal cards, 6,7,8 -> NP cards). 
        It should have maximum 3 number.   

        Examples
        --------
        Here are examples::

            select_cards([6]) # left the rest 2 randomly choosen
            select_cards([6,2]) # left the last 1 randomly choosen
            select_cards([1,2,3])
        """
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
    def select_servant_skill(self, skill: int, tar: int = 0):
        """ Select Servant Skill
        Parameters
        ----------
            skill: int
        The id of the skill. 1~9 counted from left.

            tar: int, optional
        The id of target servant. 1~3 counted from left.
        (If the skill has target servant)
        
        Examples
        --------
        Here are examples::

            select_servant_skill(1) # skill w/o target servants
            select_servant_skill(3, 2) # skill w/ target servants
        """
        while not util.standby(util.get_sh(self.shifts), "assets/attack.png"):
            time.sleep(0.2)
        self.tap(crds.SERVANT_SKILLS[skill-1], 5, 5)
        time.sleep(1)
        if tar != 0:
            self.select_servant(tar)

    def select_servant(self, servant: int):
        """ Select Servant
        Parameters
        ----------
            servant: int
        The id of the servant. 1~3 counted from left.
        """
        while not util.standby(util.get_sh(self.shifts), "assets/select.png"):
            time.sleep(0.2)
        self.tap(crds.TARGETS[servant-1], 150, 150)

    def change_servant(self, org: int, tar: int):
        """ Change Servant
        Parameters
        ----------
            org: int
        Servant id on the left side(1~3) 

            tar: int
        Servant id on the right side(1~3)
        """
        while not util.standby(util.get_sh(self.shifts), "assets/order_change.png"):
            time.sleep(0.2)
        self.tap(crds.SERVANTS[org-1], 90, 90)
        time.sleep(0.1)
        self.tap(crds.SERVANTS[tar+2], 90, 90)
        time.sleep(0.1)
        self.tap((950, 950), 100)  # confirm btn

    def toggle_master_skill(self):
        while not util.standby(util.get_sh(self.shifts), "assets/attack.png"):
            time.sleep(0.2)
        self.tap(crds.MASTER)

    def select_master_skill(self, skill: int, org: int = 0, tar: int = 0):
        """ Servant Master Skill
        Parameters
        ----------
            skill: int
        Skill id 1~3, counted from left.

            org: int, optional
        Target servant id 1~3, counted from left.(When only 2 args)
        When implemented the 3rd arg, it is the id of the servants on the left side(1~3)

            tar: int, optional
        Servant id on the right side(1~3)

        Examples
        --------
        Here are examples::

            select_master_skill(1) # skill w/o target servants
            select_master_skill(2, 2) # skill w/ target servants
            select_master_skill(3, 1, 1) # Order Change

        """
        self.toggle_master_skill()
        self.tap(crds.MASTER_SKILLS[skill-1], 8, 8)
        if org != 0 and tar == 0:
            self.select_servant(org)
        elif org != 0 and tar != 0:
            self.change_servant(org, tar)

    # pre-battle related
    def select_checkpoint(self, ckp: str = None):
        """ Select Checkpoint
        Parameters
        ----------
            ckp: str, optional
        Override the initially set checkpoint.

        Raises
        ------
            Exception("Out of AP!")
        When out of AP.
        """
        self.wait(self.checkpoint)
        if ckp is None:
            ckp = self.checkpoint
        crds = util.get_crd(util.get_sh(self.shifts), self.checkpoint)
        self.tap(crds[0], 100)
        time.sleep(0.2)
        # check whether out of AP
        # Not tested
        if util.standby(util.get_sh(self.shifts), "assets/noap.png"):  # in progress
            if self.counts > 0:
                self.eat_apple()
            else:
                raise Exception("Out of AP!")

    def select_support(self, spt: str = None):
        """ Select Support
        Parameters
        ----------
            spt: str, optional
        Override the initially set support.
        """
        time.sleep(0.3)
        if spt is None:
            spt = self.support
        x = util.get_crd(util.get_sh(self.shifts), spt)
        if len(x) == 0:
            self.tap((860, 430), 300, 100)
        else:
            self.tap(x[0])

    # advance support
    def advance_suppoet(self, spt: str = None):
        """
        NOT TESTED!
        """
        time.sleep(0.3)
        if spt is None:
            spt = self.support
        x = util.get_crd(util.get_sh(self.shifts), spt)
        counter = False
        times = 0
        while len(x) == 0:
            if not counter:
                self.swipe((1000, 800), (1000, 300), 0.5 +
                           0.1 * random.randrange(1, 10))
                counter = True
            else:
                update = self.update_support()
                if update:
                    counter = False
                    if times > 5: 
                        raise Exception("Desired support not found!")
                else:
                    time.sleep(3)
            time.sleep(0.5)
            x = util.get_crd(util.get_sh(self.shifts), spt)
            times += 1
        self.tap(x[0])

    def update_support(self) -> bool:
        """ Update Support List
        Returns
        -------
            bool
        `True` if successfully updated, otherwise is `False`.
        """
        btn = util.get_crd(util.get_sh(self.shifts), "assets/update.png")
        self.tap(btn[0], 1, 1)
        time.sleep(0.1)
        if util.standby(util.get_sh(self.shifts), "assets/uplist.png"):
            self.tap((1240, 840), 10, 5)
            return True
        else:
            self.tap((950, 840))
            return False

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

    # FLAWED
    def is_finished(self) -> bool:
        time.sleep(0.2)
        return util.standby(util.get_sh(self.shifts), "assets/finish.png", 0.7)

    # AP related
    # Not tested
    def set_apples(self, cnt: int, apl: str):
        """ Set Apples
        Parameters
        ----------
            cnt: int
        Number of the apples willl be used.

            apl: str
        Path to the image of the apple.
        """
        self.counts = cnt
        self.apple = apl

    def eat_apple(self):
        x = util.get_crd(util.get_sh(self.shifts), self.apple)
        self.tap(x[0])
        self.counts -= 1
        time.sleep(0.2)
        y = util.get_crd(util.get_sh(self.shifts), "assets/decide.png")
        self.tap(y[0])

    # others
    def start_battle(self):
        while not util.standby(util.get_sh(self.shifts), "assets/start.png"):
            time.sleep(0.2)
        x = util.get_crd(util.get_sh(self.shifts), "assets/start.png")
        self.tap(x[0])

    def quick_start(self):
        """ Quick Start
        Select the default `checkpoint`, `support` and start the battle.
        """
        self.select_checkpoint()
        self.select_support()
        self.start_battle()

    def tap(self, crd: (int, int), i: int = 10, j: int = 10):
        x = crd[0] + self.shifts[0]
        y = crd[1] + self.shifts[1]
        util.tap(util.shifter((x, y), i, j))

    def swipe(self, org: (int, int), tar: (int, int), delay, sfts: (int, int) = (10, 10),):
        original = (org[0] + self.shifts[0], org[1] + self.shifts[1])
        target = (tar[0] + self.shifts[0], tar[1] + self.shifts[1])
        util.swipe(
            util.shifter(original, sfts[0], sfts[1]),
            util.shifter(target, sfts[0], sfts[1]),
            delay)

    def wait(self, pic: str):
        while not util.standby(util.get_sh(self.shifts), pic):
            time.sleep(0.2)
