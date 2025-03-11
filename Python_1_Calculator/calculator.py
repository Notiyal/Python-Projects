import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")


entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
  entry.insert(tk.END, number)

def evaluate():
  try:
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))
  except:
    entry.delete(0, tk.END)
    entry.insert(tk.END, "Error")

def clear():
  entry.delete(0, tk.END)


buttons = [
  ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
  ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
  ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
  ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=evaluate, bg="lightblue")
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=clear, bg="lightcoral")
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda t=text: button_click(t))

    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()