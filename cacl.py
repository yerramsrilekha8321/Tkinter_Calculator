import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("380x420")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_display()
        self.create_buttons()

    def create_display(self):
        entry = tk.Entry(self.root,textvariable=self.input_text, font=("Arial", 18),justify="right")
        entry.pack()

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('sqrt',1,4),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('^',2,4),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('(',3,4),
            ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3), (')',4,4),
            ('sin',5,0), ('cos',5,1), ('tan',5,2), ('log',5,3), ('pi',5,4)
        ]

        for text, row, col in buttons:
            if text == '=':
                btn = tk.Button(frame, text=text, width=6, height=2,
                                command=self.calculate)
            else:
                btn = tk.Button(frame, text=text, width=6, height=2,
                                command=lambda t=text: self.press(t))
            btn.grid(row=row, column=col)

        tk.Button(
            frame, text="Clear", width=32, height=2, command=self.clear
        ).grid(row=6, column=0, columnspan=5)


    def press(self, value):
        if value == '^':
            self.expression += '**'
        elif value == 'pi':
            self.expression += str(math.pi)
        elif value in ['sin', 'cos', 'tan', 'log', 'sqrt']:
            self.expression += f"math.{value}("
        else:
            self.expression += value

        self.input_text.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
            self.input_text.set(result)
        except:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")

root = tk.Tk()
ScientificCalculator(root)
root.mainloop()
