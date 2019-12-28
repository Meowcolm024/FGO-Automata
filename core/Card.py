class Card():
    def __init__(self, idt: int, mrk: float, color: int):
        """
        Parameters
        ----------
            mrk: float
        Resist: 0.5, Normal: 1, Weak: 2

            color: int
        Quick: 0.8, Arts:1, Buster: 2
        """
        self.identity = idt
        self.mark = mrk
        self.atk = color

    def get_atk(self, priority: int, exbuster: bool):
        """
        Parameters
        ----------
            prt: int
        Card priority 0 -> 1, 1 -> 1.2, 2 -> 1.4

            eb: bool
        Buster first -> atk+0.5
        """
        dmg = self.atk

        if priority == 1:
            dmg *= 1.2
        elif priority == 2:
            dmg *= 1.4

        if exbuster:
            dmg += 0.5

        dmg *= self.mark

        return dmg

    def __eq__(self, value):
        return True if self.identity == value.identity else False

    def __str__(self):
        return f"ID: {self.identity}, Mark: {self.mark}, Color: {self.atk}"


if __name__ == "__main__":
    t = Card(1, 2, 0.8)
    q = Card(1, 0.5, 0.8)
    s = Card(2, 1, 1)
    print(t.get_atk(2, True))
    print(t == s)
    print(t)
