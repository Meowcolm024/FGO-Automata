class BB():
    def __init__(self):
        self.script = [
            "from core.Automata import Automata",
            "import logging",
            "logging.basicConfig(filename='automata.log',filemode='w',level=logging.INFO,format='%(asctime)s %("
            "levelname)s %(message)s',datefmt='%y/%m/%d %I:%M:%S %p') "
        ]
        self.battle = 1

    def init_sc(self):  # checkpoint, support, shifts
        def sw(file, old, new):
            file_data = ""
            with open(file, "r") as f:
                for line in f:
                    if old in line:
                        line = line.replace(old, new)
                    file_data += line
            with open(file,"w") as f:
                f.write(file_data)
        print("------------------------------------------------------------")
        print("Select Game Version")
        print("If you select JPclient, you must use device with 1920x1080")
        print("1 = JPclient")
        print("2 = CNclient")
        ver = input("Select a number: ")
        if ver == "1":
            cli = "jp/"
            sw("core/crds.py", "cn", "jp")
        if ver == "2":
            cli = "cn/"
            sw("core/crds.py", "jp", "cn")
        print("------------------------------------------------------------")
        print("Select the Checkpoint or Customize it")
        print("1 = Ember     2 = Training     3 = Qp     4 = Customization")
        selckp = input("Select a number: ")
        if selckp == "1" or selckp == "2" or selckp == "3":
            print("------------------------------------------------------------")
            print("Select the Level")
            print("1 = Novice    2 = Intermediate    3 = Advanced    4 = Expert")
            sellv = input("Select a number: ")
            if selckp == "1":
                ckp = "Ember" + sellv
            if selckp == "2":
                ckp = "Training" + sellv
            if selckp == "3":
                ckp = "Qp" + sellv
        if selckp == "4":
            print("------------------------------------------------------------")
            print("Enter the name of the Checkpoint image (PNG in /assets) (WITHOUT extension name)")
            cli = ""
            ckp = input("Checkpoint: ")

        print("------------------------------------------------------------")
        print("Enter the name of the Support image (PNG in /assets) (WITHOUT extension name)")
        spt = input("Suppport: ")

        print("------------------------------------------------------------")
        print("Enter shifts of X coordinate (Enter 0 if your res is 1920x1080)")
        sft_x = input("X shift: ")

        print("Enter shifts of Y coordinate (Enter 0 if your res is 1920x1080)")
        sft_y = input("Y shift: ")

        sc = f"bb = Automata(\"assets/{cli}{ckp}.png\", \"assets/{spt}.png\", ({sft_x}, {sft_y}))"  # class name: bb
        self.script.append(sc)
        print("------------------------------------------------------------")
        print("Auto Recovery AP")
        print("1 = No  2 = Gold Apple  3 = Silver Apple  4 = Santa Quartz  5 = Bronze Apple")
        ap = input("Select a number: ")
        if ap == "2" or ap == "3" or ap == "4" or ap == "5":
            print("------------------------------------------------------------")
            apamt = input("Enter the amount: ")
            if ap == "2":
                self.script.append(f"bb.set_apples({apamt}, \"gold\")")
            elif ap == "3":
                self.script.append(f"bb.set_apples({apamt}, \"silver\")")
            elif ap == "4":
                self.script.append(f"bb.set_apples({apamt}, \"quartz\")")
            elif ap == "5":
                self.script.append(f"bb.set_apples({apamt}, \"bronze\")")
        self.script.append("bb.quick_start()")

    def menu(self) -> bool:
        # menu
        print("------------------------------------------------------------")
        print("BATTLE", self.battle)
        print("------------------------------------------------------------")
        print("1 = select Servant skill(optional)")
        print("2 = select Master skill(optional)")
        print("3 = select Card order and finish current battle setting")
        print("------------------------------------------------------------")
        # select
        n = input("Select a number: ")
        if n == "1":
            self.sv_skill()
            return False
        elif n == "2":
            self.ms_skill()
            return False
        elif n == "3":
            self.crd_order()
            return True
        return False
        
    def sv_skill(self):
        print("------------------------------------------------------------")
        print("Servant skill types:")
        print("1 = skill w/o target servant")
        print("2 = skill w/ target servant")
        print("------------------------------------------------------------")
        n = input("Select the type of the Servant skill: ")
        if n == "1":
            x = input("Enter skill id (1~9 count from left): ")
            self.script.append(f"bb.select_servant_skill({x})")
        if n == "2":
            x = input("Enter skill id (1~9 count from left): ")
            y = input("Enter target id (1~3 count from left): ")
            self.script.append(f"bb.select_servant_skill({x}, {y})")

    def ms_skill(self):
        print("------------------------------------------------------------")
        print("Master skill types:")
        print("1 = skill w/o target servant")
        print("2 = skill w/ target servant")
        print("3 = Order Change")
        print("------------------------------------------------------------")
        n = input("Select the type of the Master skill: ")
        if n == "1":
            x = input("Enter skill id (1~3 count from left): ")
            self.script.append(f"bb.select_master_skill({x})")
        if n == "2":
            x = input("Enter skill id (1~3 count from left): ")
            y = input("Enter target id (1~3 count from left): ")
            self.script.append(f"bb.select_master_skill({x}, {y})")
        if n == "3":
            x = input("ID of Servant on the Left (1~3 count from left): ")
            y = input("ID of Servant on the Right (1~3 count from left): ")
            self.script.append(f"bb.select_master_skill(3, {x}, {y})")

    def crd_order(self):
        print("------------------------------------------------------------")
        print("Card Order:")
        print("Card id: 1~5 -> normal card, 6,7,8 -> NP card")
        print("if you only want to select 1 card, enter ONE number")
        print("for multiple cards, separate each digits like: 1,2,3")
        print("------------------------------------------------------------")
        n = input("Enter Card order: ")
        self.script.append(f"bb.select_cards([{n}])")

    def start(self) -> str:
        print("***********************")
        print("* FGO-Automata Daemon *")
        print("***********************")
        print("------------------------------------------------------------")
        print("This script will help you create your FGO-Automat Script")
        print("------------------------------------------------------------")
        input("Press any key to continue: ")
        print("------------------------------------------------------------")
        name = input("Enter script name (WITHOUT extension name): ")
        print("------------------------------------------------------------")
        return name

    def setup_battle(self):
        btl = [False, False, False]
        # init
        self.init_sc()
        # battles
        for i in range(3):
            self.script.append("# BATTLE " + str(self.battle))
            while not btl[i]:
                btl[i] = self.menu()
            self.battle += 1
        # end'
        self.script.append("# FINISH")
        self.script.append("bb.finish_battle()")
        
    def main(self):
        name = self.start()
        self.setup_battle()
        print("------------------------------------------------------------")
        print("Setup finished!")
        print(f"Run {name}.py to start the script")
        file = open(name + ".py", "w+")
        content = '\n'.join(self.script)
        file.write(content)

if __name__ == "__main__":
    demon = BB()
    demon.main()
