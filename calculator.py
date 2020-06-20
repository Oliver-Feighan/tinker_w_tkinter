import sys
from enum import Enum
from math import *

if sys.version_info[0] != 3 or sys.version_info[1] != 5 or sys.version_info[2] != 5:
	print("not the right version! This is version %s %s %s" % (sys.version[0], sys.version[1], sys.version[2]) )
	quit() 

import tkinter as tk

class Operators(Enum):
	add		 = 1
	minus	 = 2
	multiply = 3
	divide	 = 4

operator_symbols = {Operators.add: "+",
					Operators.minus: "-",
					Operators.multiply: "*",
					Operators.divide: "/"}

operator = None

global_text = ""

def number(value):
	global global_text
	global_text += str(value)
	result.insert("end", str(value))

def set_operator(symbol):
	operator = Operators(symbol)
	global global_text
	global_text += str(operator_symbols[Operators(symbol)])
	result.insert("end", str(operator_symbols[Operators(symbol)]))

def do_operation():
	global global_text
	result_number = eval(global_text)
	result.delete(0, "end")
	global_text = str(result_number)
	result.insert(0, str(result_number))

def clear():
	global global_text
	global_text = ""
	result.delete(0, "end")


master = tk.Tk()

result = tk.Entry(master)
result.grid(row = 0, columnspan = 5)

for i in range(9):
	tk.Button(master, text="%s" % str(i+1), command = lambda i=i: number(i+1)).grid(row=2+round(i/4), column = (i%3))

tk.Button(master, text="0", command = lambda : number(0)).grid(row=5, column = 1)

tk.Button(master, text="+", command = lambda : set_operator(1)).grid(row=2, column = 4)
tk.Button(master, text="-", command = lambda : set_operator(2)).grid(row=3, column = 4)
tk.Button(master, text="*", command = lambda : set_operator(3)).grid(row=4, column = 4)
tk.Button(master, text="/", command = lambda : set_operator(4)).grid(row=5, column = 4)

tk.Button(master, text="=", command = do_operation).grid(row=6, column = 4)

tk.Button(master, text="AC", command = clear).grid(row = 6, column = 2)
tk.Button(master, text='Quit', command=master.quit).grid(row=6, column=0, sticky=tk.W, pady=4)

tk.mainloop()