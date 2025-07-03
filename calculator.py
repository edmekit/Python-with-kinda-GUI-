import tkinter as tk

def click(value):
    window.insert(tk.END, value)

def equate():
    res = eval(window.get())
    window.delete(0, tk.END)
    window.insert(tk.END, str(res))

def dele():
    window.delete(0,tk.END)

calc = tk.Tk()
calc.title("Calculator")
calc.geometry("300x400")
window = tk.Entry(calc, width=30, relief="ridge", borderwidth=2)
window.grid(row=0, column=0, columnspan=4, pady=20, padx=10)

num1 = tk.Button(calc, text="1", width=4, height=2, command= lambda: click("1"))
num1.grid(row=1, column=0, padx=5, pady=5)
num2 = tk.Button(calc, text="2", width=4, height=2, command= lambda: click("2"))
num2.grid(row=1, column=1, padx=5, pady=5)
num3 = tk.Button(calc, text="3", width=4, height=2, command= lambda: click("3"))
num3.grid(row=1, column=2, padx=5, pady=5)
plus = tk.Button(calc, text="+", width=4, height=2, command= lambda: click("+"))
plus.grid(row=1, column=3, padx=5, pady=5)
num4 = tk.Button(calc, text="4", width=4, height=2, command= lambda: click("4"))
num4.grid(row=2, column=0, padx=5, pady=5)
num5 = tk.Button(calc, text="5", width=4, height=2, command= lambda: click("5"))
num5.grid(row=2, column=1, padx=5, pady=5)
num6 = tk.Button(calc, text="6", width=4, height=2, command= lambda: click("6"))
num6.grid(row=2, column=2, padx=5, pady=5)
minus = tk.Button(calc, text="-", width=4, height=2, command= lambda: click("-"))
minus.grid(row=2, column=3, padx=5, pady=5)
num7 = tk.Button(calc, text="7", width=4, height=2, command= lambda: click("7"))
num7.grid(row=3, column=0, padx=5, pady=5)
num8 = tk.Button(calc, text="8", width=4, height=2, command= lambda: click("8"))
num8.grid(row=3, column=1, padx=5, pady=5)
num9 = tk.Button(calc, text="9", width=4, height=2, command= lambda: click("9"))
num9.grid(row=3, column=2, padx=5, pady=5)
times = tk.Button(calc, text="*", width=4, height=2, command= lambda: click("*"))
times.grid(row=3, column=3, padx=5, pady=5)
num0 = tk.Button(calc, text="0", width=4, height=2, command= lambda: click("0"))
num0.grid(row=4, column=1, padx=5, pady=5)
div = tk.Button(calc, text="/", width=4, height=2, command= lambda: click("/"))
div.grid(row=4, column=3, padx=5, pady=5)
eq = tk.Button(calc, text="=", width=4, height=2, command=equate)
eq.grid(row=4, column=2, padx=5, pady=5)
clear = tk.Button(calc, text="del", width=4, height=2, command=dele)
clear.grid(row=4, column=0, padx=5, pady=5)

calc.mainloop()