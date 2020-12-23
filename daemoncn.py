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
        print("选择游戏版本")
        print("如果在日服使用, 请使用1920x1080设备")
        print("1 = 日服")
        print("2 = 国服")
        ver = input("输入数字: ")
        if ver == "1":
            cli = "jp/"
            sw("core/crds.py", "cn", "jp")
        if ver == "2":
            cli = "cn/"
            sw("core/crds.py", "jp", "cn")
        print("------------------------------------------------------------")
        print("选择关卡或自定义")
        print("1 = 狗粮     2 = 修炼场     3 = QP     4 = 自定义")
        selckp = input("输入数字: ")
        if selckp == "1" or selckp == "2" or selckp == "3":
            print("------------------------------------------------------------")
            print("选择等级")
            print("1 = 初级    2 = 中级    3 = 上级    4 = 超级")
            sellv = input("输入数字: ")
            if selckp == "1":
                ckp = "Ember" + sellv
            if selckp == "2":
                ckp = "Training" + sellv
            if selckp == "3":
                ckp = "Qp" + sellv
        if selckp == "4":
            print("------------------------------------------------------------")
            print("输入自定义关卡图片名 (PNG格式 位于 assets) (不需要输入后缀.png)")
            cli = ""
            ckp = input("关卡图片: ")

        print("------------------------------------------------------------")
        print("输入助战图片名 (PNG格式 位于 assets) (不需要输入后缀.png)")
        spt = input("助战图片: ")

        print("------------------------------------------------------------")
        print("请设置游戏画面偏移X坐标 (1920x1080请填写0)")
        sft_x = input("X: ")

        print("请设置游戏画面偏移Y坐标 (1920x1080请填写0)")
        sft_y = input("Y: ")

        sc = f"bb = Automata(\"assets/{cli}{ckp}.png\", \"assets/{spt}.png\", ({sft_x}, {sft_y}))"  # class name: bb
        self.script.append(sc)
        print("------------------------------------------------------------")
        print("是否启用AP恢复")
        print("1 = 不启用  2 = 金苹果  3 = 银苹果  4 = 圣晶石")    
        ap = input("输入数字: ")
        if ap == "2" or ap == "3" or ap == "4":
            print("------------------------------------------------------------")
            apamt = input("输入使用个数: ")
            if ap == "2":
                self.script.append(f"bb.set_apples({apamt}, \"assets/gold.png\")")
            elif ap == "3":
                self.script.append(f"bb.set_apples({apamt}, \"assets/silver.png\")")
            elif ap == "4":
                self.script.append(f"bb.set_apples({apamt}, \"assets/quartz.png\")")
        self.script.append("bb.quick_start()")

    def menu(self) -> bool:
        # menu
        print("------------------------------------------------------------")
        print("BATTLE", self.battle)
        print("------------------------------------------------------------")
        print("[注意] 请在设置出卡顺序前进行添加技能等设定")
        print("1 = 添加从者技能(可选)")
        print("2 = 添加御主技能(可选)")
        print("3 = 设置出卡顺序并结束本回合设置(必须)")
        print("------------------------------------------------------------")
        # select
        n = input("输入数字: ")
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
        print("从者技能类型:")
        print("1 = 无目标从者")
        print("2 = 有目标从者")
        print("------------------------------------------------------------")
        n = input("输入数字: ")
        if n == "1":
            x = input("输入技能ID 1~9 [从左往右数]: ")
            self.script.append(f"bb.select_servant_skill({x})")
        if n == "2":
            x = input("输入技能ID 1~9 [从左往右数]: ")
            y = input("输入从者ID 1~3 [从左往右数]: ")
            self.script.append(f"bb.select_servant_skill({x}, {y})")

    def ms_skill(self):
        print("------------------------------------------------------------")
        print("御主技能类型:")
        print("1 = 无目标从者")
        print("2 = 有目标从者")
        print("3 = Order Change")
        print("------------------------------------------------------------")
        n = input("输入数字: ")
        if n == "1":
            x = input("输入技能ID 1~3 [从左往右数]: ")
            self.script.append(f"bb.select_master_skill({x})")
        if n == "2":
            x = input("输入技能ID 1~3 [从左往右数]: ")
            y = input("输入从者ID 1~3 [从左往右数]: ")
            self.script.append(f"bb.select_master_skill({x}, {y})")
        if n == "3":
            x = input("被替换的从者ID 1~3 [从左往右数]: ")
            y = input("将上场的从者ID 1~3 [从左往右数]: ")
            self.script.append(f"bb.select_master_skill(3, {x}, {y})")

    def crd_order(self):
        print("------------------------------------------------------------")
        print("设置出卡顺序:")
        print("数字1~5为从左到右的五张普通指令卡, 6~8为从左到右的3张宝具卡")
        print("您也可以不选满, 比如只输入一个数字")
        print("对于多张卡请用半角英文符号[ , ]分隔 如 1, 2, 3")
        print("------------------------------------------------------------")
        n = input("输入顺序: ")
        self.script.append(f"bb.select_cards([{n}])")

    def start(self) -> str:
        print("***********************")
        print("* FGO-Automata Daemon *")
        print("***********************")
        print("------------------------------------------------------------")
        print("This script will help you create your FGO-Automat Script")
        print("------------------------------------------------------------")
        input("按下任意键开始配置: ")
        print("------------------------------------------------------------")
        name = input("输入脚本名 (无需添加后缀.py): ")
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
