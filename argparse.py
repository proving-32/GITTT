import tkinter as tk
from tkinter import messagebox

# Define the main application class
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Project - System Calculator")
        self.root.geometry("300x400")

        self.expression = ""

        # Create the display frame
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.create_display_labels()
        self.create_buttons()

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=50, bg="grey")
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        self.total_label = tk.Label(self.display_frame, text=self.expression, anchor=tk.E, bg="grey", fg="white", padx=24, font=("Arial", 24))
        self.total_label.pack(expand=True, fill='both')

    def create_buttons(self):
        buttons = [
            ['%', 'CE', 'C', '←'],
            ['1/x', 'x²', '√x', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]

        for row_index, row in enumerate(buttons):
            for col_index, button in enumerate(row):
                button_frame = tk.Frame(self.buttons_frame, height=60, width=60)
                button_frame.grid(row=row_index, column=col_index, padx=5, pady=5)
                button_frame.pack_propagate(False)

                button = tk.Button(button_frame, text=button, font=("Arial", 18), command=lambda button=button: self.on_button_click(button))
                button.pack(expand=True, fill='both')

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
        elif button == 'CE':
            self.expression = self.expression[:-1]
        elif button == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
        elif button in ['%', '1/x', 'x²', '√x', '÷', '×', '-', '+', '±']:
            if button == '÷':
                self.expression += '/'
            elif button == '×':
                self.expression += '*'
            elif button == '±':
                self.expression += '-'
            elif button == '1/x':
                self.expression = str(1 / eval(self.expression))
            elif button == 'x²':
                self.expression = str(eval(self.expression) ** 2)
            elif button == '√x':
                self.expression = str(eval(self.expression) ** 0.5)
            elif button == '%':
                self.expression += '/100'
        else:
            self.expression += button

        self.update_display()

    def update_display(self):
        self.total_label.config(text=self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = CalculatorApp(root)
    root.mainloop()



