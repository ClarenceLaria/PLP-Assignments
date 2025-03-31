import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        else:
            messagebox.showerror("Error", "Invalid operation selected")
            return

        result_label.config(text=f"Result: {num1} {operation} {num2} = {result}", fg="green")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Function to clear inputs
def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create main window
root = tk.Tk()
root.title("PLP Calculator")
root.geometry("350x400")
root.configure(bg="#2C3E50")

# Styling
font_style = ("Arial", 14, "bold")
button_style = {"font": ("Arial", 12, "bold"), "bg": "#2980B9", "fg": "white", "width": 10, "height": 1}
entry_style = {"font": ("Arial", 14), "width": 12, "justify": "center"}

# Labels and Entry Fields
tk.Label(root, text="Enter First Number:", font=font_style, bg="#2C3E50", fg="white").pack(pady=5)
entry1 = tk.Entry(root, **entry_style)
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number:", font=font_style, bg="#2C3E50", fg="white").pack(pady=5)
entry2 = tk.Entry(root, **entry_style)
entry2.pack(pady=5)

tk.Label(root, text="Select Operation:", font=font_style, bg="#2C3E50", fg="white").pack(pady=5)
operator = tk.StringVar()
operator.set("+")  # Default selection
tk.OptionMenu(root, operator, "+", "-", "*", "/").pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Calculate", command=calculate, **button_style).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Clear", command=clear_fields, font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", width=10, height=1).grid(row=0, column=1, padx=5)

# Result Label
result_label = tk.Label(root, text="Result: ", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white")
result_label.pack(pady=20)

# Run the main event loop
root.mainloop()
