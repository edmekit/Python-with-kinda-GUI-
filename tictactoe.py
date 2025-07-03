import tkinter as tk

app = tk.Tk()
app.title("Tic Tac Toe")
app.geometry("300x300")

#buttons
for i in range (3):
    for j in range(3):
        button = tk.Button(app, text="", width=5, height=3, font=("Arial", 24))
        button.grid(row=i, column=j, padx=5, pady=5)

current_player = "X"  

#what happens whenn button clicked
def button_click(button):
    global current_player
    if button["text"] == "":
        button["text"] = current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    else:
        button["text"] = ""  

#applies the func to each button
for widget in app.winfo_children():
    if isinstance(widget, tk.Button):
        widget.config(command=lambda b=widget: button_click(b))
          
app.mainloop()
import tkinter as tk

app = tk.Tk()
app.title("Tic Tac Toe")
app.geometry("300x300")

#buttons
for i in range (3):
    for j in range(3):
        button = tk.Button(app, text="", width=5, height=3, font=("Arial", 24))
        button.grid(row=i, column=j, padx=5, pady=5)

current_player = "X"  

#what happens whenn button clicked
def button_click(button):
    global current_player
    if button["text"] == "":
        button["text"] = current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    else:
        button["text"] = ""  

#applies the func to each button
for widget in app.winfo_children():
    if isinstance(widget, tk.Button):
        widget.config(command=lambda b=widget: button_click(b))
          
app.mainloop()