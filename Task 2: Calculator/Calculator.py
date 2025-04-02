from tkinter import *

root = Tk()
root.geometry("320x480")
root.resizable(False, False)
root.title("Calculator")
root.configure(bg="#1E1E1E")

content = StringVar()
equation = ""

def show(value):
    global equation
    equation += value
    content.set(equation)

def clear():
    global equation
    equation = ""
    content.set("")

def backspace():
    global equation
    equation = equation[:-1]
    content.set(equation)

def calculate():
    global equation
    try:
        result = eval(equation)
    except:
        result = "Error"
        equation = ""
    content.set(result)
    equation = str(result)

# Display
entry = Entry(root, textvariable=content, font=("Arial", 24), fg="white", bg="#2D2D2D", bd=10, relief=FLAT, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

btn_bg = "#333"
op_bg = "#ff9800"
btn_fg = "white"

def create_button(text, row, col, w=5, h=2, bg=btn_bg, cmd=None):
    Button(root, text=text, width=w, height=h, font=("Arial", 14), fg=btn_fg, bg=bg, relief=FLAT, command=cmd).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

buttons = [
    ('%', 1, 0, btn_bg),('C', 1, 2, btn_bg, clear),('⌫', 1, 3, btn_bg, backspace),
    ('1/x', 2, 0, btn_bg), ('x²', 2, 1, btn_bg), ('√', 2, 2, btn_bg), ('÷', 2, 3, op_bg, lambda: show('/')),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('×', 3, 3, op_bg, lambda: show('*')),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3, op_bg, lambda: show('-')),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3, op_bg, lambda: show('+')),
    ('+/-', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3, op_bg, calculate)
]

for btn in buttons:
    text, r, c = btn[:3]
    bg = btn[3] if len(btn) > 3 else btn_bg
    cmd = btn[4] if len(btn) > 4 else lambda t=text: show(t)
    create_button(text, r, c, bg=bg, cmd=cmd)

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
