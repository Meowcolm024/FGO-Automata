class BB():
    def __init__(self):
        self.script = ["from core.Automata import Automata"]
        self.battle = 1

    def init_sc(self):  # checkpoint, support, shifts
        ckp = input("Enter the name of the Checkpoint (template image name, WITHOUT extension name): ")
        spt = input("Enter the name of the Support (template image name, WITHOUT extension name): ")
        sft_x = input("Enter shifts of X coordinate (Enter 0 if your res is 1920x1080): ")
        sft_y = input("Enter shifts of Y coordinate (Enter 0 if your res is 1920x1080): ")
        sc = f"bb = Automata(assets/{ckp}.png, assets/{spt}.png, ({sft_x}, {sft_y}))" # class name: bb
        self.script.append(sc)

    def menu(self) -> bool: 
        # menu
        print("----------")
        print("BATTLE:", self.battle)
        print("----------")
        print("1 = select Servant skill(optional)")
        print("2 = select Master sill(optional)")
        print("3 = select Card order")
        print("4 = fininsh current battle setting")
        print("----------")
        # select
        n = input("Select a number: ")
        if n == 1:
            self.sv_skill()
            return False
        elif n == 2:
            self.ms_skill()
            return False
        elif n == 3:
            self.crd_order()
            return False
        elif n == 4:
            return True
        return False

    def sv_skill(self):
        print("----------")
        print("Servant skill types:")
        print("1 = skill w/o target servant")
        print("2 = skill w/ target servant")
        print("----------")
        n = input("Select the type of the Servant skill: ")
        if n == 1:
            x = input("Enter skill id (1~9 count from left): ")
            self.script.append(f"bb.select_servant_skill({x})")
        if n == 2:
            x = input("Enter skill id (1~9 count from left): ")
            y = input("Enter target id(1~3 count from left): ")
            self.script.append(f"bb.select_servant_skill({x}, {y})")

    def ms_skill(self):
        pass

    def crd_order(self):
        pass

    def main(self):
        self.init_sc()
        print(self.script)
        pass


if __name__ == "__main__":
    demon = BB()
    demon.main()
