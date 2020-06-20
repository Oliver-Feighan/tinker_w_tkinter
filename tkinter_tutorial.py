import sys
from enum import Enum

if sys.version_info[0] != 3 or sys.version_info[1] != 5 or sys.version_info[2] != 5:
	print("not the right version! This is version %s %s %s" % (sys.version[0], sys.version[1], sys.version[2]) )
	quit() 

import tkinter as tk

class Operators(Enum):
	add		 = 1
	minus	 = 2
	multiply = 3
	divide	 = 4

operator = None

def number(value):
	return 0;
	#print(value)

def set_operator(symbol):
	operator = Operators(symbol)

def do_operation

master = tk.Tk()

e1 = tk.Entry(master)

e1.grid(row=0, column = 0, columnspan = 5)

result = tk.Entry(master)

for i in range(9):
	tk.Button(master, text="%s" % str(i+1), command = number(i+1)).grid(row=2+round(i/4), column = (i%3))

tk.Button(master, text="0", command = number(0)).grid(row=5, column = 1)

tk.Button(master, text="+", command = set_operator(1)).grid(row=2, column = 4)
tk.Button(master, text="-", command = set_operator(2)).grid(row=3, column = 4)
tk.Button(master, text="x", command = set_operator(3)).grid(row=4, column = 4)
tk.Button(master, text="/", command = set_operator(4)).grid(row=5, column = 4)

tk.Button(master, text="=", command = add).grid(row=6, column = 4)

tk.Button(master, text='Quit', command=master.quit).grid(row=6, column=0, sticky=tk.W, pady=4)

tk.mainloop()