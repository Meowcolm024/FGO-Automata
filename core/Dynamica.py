from core.Card import Card

class Dynamica():
    def __init__(self, crd: [Card]):
        self.cards = crd

    def read_cards(self):
        pass

    def arrange_cards(self) -> [Card]:
        max_atk = 0
        max_comb = []
        for fst in self.cards:
            for sec in self.cards:
                if fst == sec: continue
                for trd in self.cards:
                    if sec == trd or fst == trd: continue
                    ex = False
                    if fst.atk == 2: ex = True
                    cur_atk = sum([fst.get_atk(1, ex), sec.get_atk(1.2, ex), trd.get_atk(1.4, ex)])
                    if cur_atk > max_atk:
                        max_atk = cur_atk
                        max_comb = [fst, sec, trd]
        print(max_atk)
        return max_comb
