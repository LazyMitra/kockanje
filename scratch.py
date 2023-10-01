import os
import random
import tkinter as tk

root = tk.Tk()
nes = int(input("pogodi broj 1 - 10: "))
broj = random.randint(1,10)
if broj != nes :
    print("oh ne falio si, bio je broj ",broj)
    os.system("shutdown /s")
else:
    print("gg uspio si pogoditi nazalost")

root.protocol("WM_DELETE_WINDOW")