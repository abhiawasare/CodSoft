from tkinter import *
from tkinter import messagebox

tasklist = []

def load_tasks():
    global tasklist
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        tasklist = [task.strip() for task in tasks if task.strip()]
        listbox.delete(0, END)
        for task in tasklist:
            listbox.insert(END, task)
    except FileNotFoundError:
        open("tasks.txt", "w").close()

def add_new_task():
    global tasklist
    task = new_task.get().strip()
    if task:
        if task not in tasklist:
            listbox.insert(END, task)
            tasklist.append(task)
            new_task.delete(0, END)
            with open('tasks.txt', 'a') as file:
                file.write(task + '\n')
        else:
            messagebox.showwarning("Warning", "Task already exists.")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    global tasklist
    try:
        selected_task = listbox.get(ANCHOR)
        if selected_task:
            tasklist.remove(selected_task)
            listbox.delete(ANCHOR)
            with open('tasks.txt', 'w') as file:
                for task in tasklist:
                    file.write(task + '\n')
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")
    except ValueError:
        messagebox.showwarning("Warning", "Error removing task.")

def on_hover(btn, color):
    btn.bind("<Enter>", lambda e: btn.config(bg=color))
    btn.bind("<Leave>", lambda e: btn.config(bg=btn.default_color))

root = Tk()
root.geometry("400x500")
root.resizable(False, False)
root.config(bg="#1e272e")
root.title("To-Do List")

Label(root, text="TO-DO LIST ✅", bg="#1e272e", fg="white", font=('Arial', 20, 'bold')).pack(pady=10)

frame = Frame(root, bg="#1e272e")
frame.pack(pady=10)

listbox = Listbox(frame, width=35, height=12, font=("Arial", 12), bd=0, fg="white",
                  bg="#485460", highlightthickness=0, cursor="hand2", selectbackground="#ff4757", activestyle="none")
listbox.pack(side=LEFT, fill=BOTH, pady=4, padx=10)

scroll = Scrollbar(frame, command=listbox.yview, bg="#1e272e")
scroll.pack(side=LEFT, fill=BOTH)
listbox.config(yscrollcommand=scroll.set)

Label(root, text="Enter a Task:", font="Arial 12", bg="#1e272e", fg="white").pack(pady=5)
new_task = Entry(root, font="Arial 12", width=30, bd=2, bg="#d2dae2", fg="black", justify=CENTER)
new_task.pack(pady=5)

button_frame = Frame(root, bg="#1e272e")
button_frame.pack(pady=10)

add_button = Button(button_frame, text="➕ Add Task", bg="#2ed573", fg="white", width=20, height=2, font="Arial 10 bold",
                    relief=FLAT, command=add_new_task, cursor="hand2")
add_button.pack(pady=5)
add_button.default_color = "#2ed573"
on_hover(add_button, "#26a65b")

remove_button = Button(button_frame, text="❌ Remove Task", bg="#ff4757", fg="white", width=20, height=2, font="Arial 10 bold",
                       relief=FLAT, command=remove_task, cursor="hand2")
remove_button.pack(pady=5)
remove_button.default_color = "#ff4757"
on_hover(remove_button, "#d63031")

Label(root, text="📌 Stay organized & productive!", bg="#1e272e", fg="white", font=('Arial', 10)).pack(pady=10)

load_tasks()

root.mainloop()
