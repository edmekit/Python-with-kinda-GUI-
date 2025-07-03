import tkinter as tk
def add_task():
    task = entry.get()
    if task.strip() != "":
        lis.insert(tk.END, task)
        entry.delete(0, tk.END)
        with open(saver, "a") as f:
            f.write(task + "\n")

def delete_task():
    try:
        selected_task = lis.curselection()[0]
        task = lis.get(selected_task)
        lis.delete(selected_task)
        with open(saver, "r") as f:
            tasks = f.readlines()
        with open(saver, "w") as f:
            for t in tasks:
                if t.strip() != task:
                    f.write(t)
    except IndexError:
        pass

saver = "todoer.txt"
app = tk.Tk()
app.title("DO THIS")
app.geometry("300x400")
framer = tk.Frame(app)
framer.pack(fill=tk.X, padx=5, pady=5)
entry = tk.Entry(framer)
entry.pack(side=tk.LEFT, fill=tk.X, anchor="ne", padx=5, pady=5)
but = tk.Button(framer, text="Add Task", command=add_task)
but.pack(side=tk.LEFT, anchor="ne", padx=5, pady=5)
delete_but = tk.Button(framer, text="Delete Task", command=delete_task)
delete_but.pack(side=tk.LEFT, anchor="ne", pady=5)
lis = tk.Listbox(app)
lis.pack(expand=True, fill=tk.BOTH)

def load_tasks():
    try:
        with open(saver, "r") as f:
            tasks = f.readlines()
            for task in tasks:
                lis.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

load_tasks()
app.mainloop()
