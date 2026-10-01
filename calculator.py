import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Красивый Калькулятор")
app.geometry("300x420")


display = ctk.CTkEntry(app, font=("Helvetica", 40), justify="right", height=60)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")

expression = ""

def add_to_expression(symbol):
    expression = expression + str(symbol)
    display.delete(0, 'end')
    display.insert(0, expression)

def clear_display():
    global expression
    expression = ""
    display.delete(0, 'end')

def calculate():
    global expression
    try:
        result = str(eval(excpression))
        display.delete(0, 'end')
        display.insert(0, result)
        expression = result
    except Exception as e:
        display.delete(0, 'end')
        display.insert(0, "Ошибка")
        expression = ""

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        btn = ctk.CTkButton(app, text=button, command=calculate, width=65, height=65, 
                            font=("Arial", 24), fg_color="#2E8B57", hover_color="#3CB371")
    elif button == "C":
        btn = ctk.CTkButton(app, text=button, command=clear_display, width=65, height=65, 
                            font=("Arial", 24), fg_color="#B22222", hover_color="#CD5C5C")
    else:
        btn = ctk.CTkButton(app, text=button, command=lambda: add_to_expression(button), 
                            width=65, height=65, font=("Arial", 24))

    btn.grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

app.mainloop()