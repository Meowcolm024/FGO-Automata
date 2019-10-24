from core.Automata import Automata
# st
shiki = Automata("assets/event.png", "assets/sp2.png", (248, 0))
shiki.quick_start()
# t1
shiki.select_servant_skill(6)
shiki.select_cards([7])
# t2
shiki.show_master_skill()
shiki.select_master_skill(3)
shiki.change_servant(2, 1)
for i in [4,6,8,9]:
    shiki.select_servant_skill(i)
shiki.select_cards([7])
# t3
shiki.show_master_skill()
shiki.select_master_skill(1)
for i in [1,2,5]:
    shiki.select_servant_skill(i)
shiki.select_servant_skill(7, 1)
shiki.select_cards([6])
# while not shiki.is_finished():
# shiki.select_cards([])
# fin
shiki.finish_battle()
