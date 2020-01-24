from core.Scripter import Repl
import sys

arg = sys.argv
repl = Repl()
if len(arg) <= 1:
    repl.main_loop()
else:
    repl.load_file(arg[1])
