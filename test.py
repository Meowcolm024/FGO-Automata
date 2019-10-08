from core.util import screenshot, split, get_crd, get_sh
from core.Automata import Automata

# screenshot()
# left 248 right 172
# split(screenshot(), (248, 0))

# x = get_crd(get_sh((248, 0)), "assets/qp2.png")
#print(x)

tester = Automata("", "", (248, 0))
# tester.set_apples(0, "assets/silver.png")
# tester.select_checkpoint()
# tester.select_cards([6])
tester.show_master_skill()
tester.select_master_skill(3, 3, 1)
