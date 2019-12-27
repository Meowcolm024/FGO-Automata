class Card():
    def __init__(self, mrk: float, clr: int, prt: int, eb: bool):
        """
        Parameters
        ----------
            mrk: float
        Resist: 0.5, Normal: 1, Weak: 2

            clr: int
        Quick: 1, Arts:2, Buster: 3

            prt: int
        Card priority 1 -> 1, 2 -> 1.2, 3 -> 1.4

            eb: bool
        Buster first -> atk+0.5
        """
        self.mark = mrk
        self.color = clr
        self.priority = prt
        self.exbuster = eb
        self.atk = 1

    def get_atk(self):
        pass
