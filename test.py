from core.util import screenshot, split, get_crd, get_sh
from core.Automata import Automata

# screenshot()
# left 248 right 172
# split(screenshot(), (248, 0))

x = get_crd(get_sh((248, 0)), "assets/qp2.png")

print(x)

# tester = Automata("", "")
# tester.select_cards([6])