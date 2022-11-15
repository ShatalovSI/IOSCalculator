import tkinter as tk
import tkinter.messagebox
from math import modf

is_result = False


class SmallScreenApp(object):
    def __init__(self, master, **kwargs):
        self.window = master
        self.window.geometry('240x370+500+200')
        self.window.title('Калькулятор')
        self.window['bg'] = '#000000'

        self.window.bind('<Key>', self.press_key)

        self.calc = tk.Entry(
            self.window,
            disabledbackground='#000000',
            disabledforeground='#FFFFFF',
            justify=tk.RIGHT,
            font=('Arial', 20),
            width=15,
            relief=tk.FLAT
        )
        self.calc.insert(0, '0')
        self.calc['state'] = tk.DISABLED
        self.calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5, ipady=15)

        self.create_button('1').grid(row=2, column=0, stick='wens', padx=5, pady=5)
        self.create_button('2').grid(row=2, column=1, stick='wens', padx=5, pady=5)
        self.create_button('3').grid(row=2, column=2, stick='wens', padx=5, pady=5)
        self.create_button('4').grid(row=3, column=0, stick='wens', padx=5, pady=5)
        self.create_button('5').grid(row=3, column=1, stick='wens', padx=5, pady=5)
        self.create_button('6').grid(row=3, column=2, stick='wens', padx=5, pady=5)
        self.create_button('7').grid(row=4, column=0, stick='wens', padx=5, pady=5)
        self.create_button('8').grid(row=4, column=1, stick='wens', padx=5, pady=5)
        self.create_button('9').grid(row=4, column=2, stick='wens', padx=5, pady=5)
        self.create_button('0').grid(row=5, column=0, stick='wens', padx=5, pady=5, columnspan=2)

        self.create_operation_button('+').grid(row=4, column=3, stick='wens', padx=5, pady=5)
        self.create_operation_button('-').grid(row=3, column=3, stick='wens', padx=5, pady=5)
        self.create_operation_button('/').grid(row=1, column=3, stick='wens', padx=5, pady=5)
        self.create_operation_button('*').grid(row=2, column=3, stick='wens', padx=5, pady=5)

        self.create_calc_button('=').grid(row=5, column=3, stick='wens', padx=5, pady=5)
        self.create_clear_button('c').grid(row=1, column=0, stick='wens', padx=5, pady=5)
        self.create_procent_button('%').grid(row=1, column=2, stick='wens', padx=5, pady=5)
        self.create_point_button('.').grid(row=5, column=2, stick='wens', padx=5, pady=5)
        self.create_plus_minus_button('±').grid(row=1, column=1, stick='wens', padx=5, pady=5)

        self.window.grid_columnconfigure(0, minsize=60)
        self.window.grid_columnconfigure(1, minsize=60)
        self.window.grid_columnconfigure(2, minsize=60)
        self.window.grid_columnconfigure(3, minsize=60)

        self.window.grid_rowconfigure(1, minsize=60)
        self.window.grid_rowconfigure(2, minsize=60)
        self.window.grid_rowconfigure(3, minsize=60)
        self.window.grid_rowconfigure(4, minsize=60)
        self.window.grid_rowconfigure(5, minsize=60)

        self.window.columnconfigure(0, weight=1, minsize=60)
        self.window.columnconfigure(1, weight=1, minsize=60)
        self.window.columnconfigure(2, weight=1, minsize=60)
        self.window.columnconfigure(3, weight=1, minsize=60)

        self.window.rowconfigure(0, weight=1, minsize=60)
        self.window.rowconfigure(1, weight=1, minsize=60)
        self.window.rowconfigure(2, weight=1, minsize=60)
        self.window.rowconfigure(3, weight=1, minsize=60)
        self.window.rowconfigure(4, weight=1, minsize=60)
        self.window.rowconfigure(5, weight=1, minsize=60)

    # ------------------------------------------ enf of __init
    # ------------------------------------------ add functions

    def add_digit(self, digit):
        global is_result
        self.calc['state'] = tk.NORMAL
        value = self.calc.get()
        if is_result:
            self.calc.delete(0, tk.END)
            self.calc.insert(0, digit)
            self.calc['state'] = tk.DISABLED
            is_result = False
            return
        if value[0] == '0' and len(value) == 1:
            value = value[1:]
        self.calc.delete(0, tk.END)
        self.calc.insert(0, value + digit)
        is_result = False
        self.calc['state'] = tk.DISABLED

    def add_operation(self, operation):
        global is_result
        self.calc['state'] = tk.NORMAL
        value = self.calc.get()
        if value[-1] == '.':
            value = value[:-1]
            self.calc.delete(0, tk.END)
            self.calc.insert(tk.END, value)
        if value[-1] in '-+/*':
            value = value[:-1]
        elif '+' in value or '-' in value or '*' in value or '/' in value:
            self.calculate()
            self.calc['state'] = tk.NORMAL
            value = self.calc.get()
        self.calc.delete(0, tk.END)
        self.calc.insert(tk.END, value + operation)
        is_result = False
        self.calc['state'] = tk.DISABLED

    def calculate(self):
        self.calc['state'] = tk.NORMAL
        global is_result
        value = self.calc.get()
        if value[-1] in '+-*/':
            value = value + value[:-1]
        self.calc.delete(0, tk.END)
        try:
            e_val = eval(value)
            if modf(e_val)[0] == 0.0:
                self.calc.insert(tk.END, int(eval(value)))
                is_result = True
            else:
                self.calc.insert(tk.END, eval(value))
                is_result = True
        except (NameError, SyntaxError):
            tk.messagebox.showinfo('Внимание', 'Нужно вводить только цифры!')
            self.calc.insert(0, '0')
        except ZeroDivisionError:
            tk.messagebox.showinfo('Внимание, на ноль делить нельзя!')
            self.calc.insert(0, '0')
        self.calc['state'] = tk.DISABLED

    def clear(self):
        self.calc['state'] = tk.NORMAL
        self.calc.delete(0, tk.END)
        self.calc.insert(0, '0')
        self.calc['state'] = tk.DISABLED

    def add_procent(self):
        self.calc['state'] = tk.NORMAL
        value = self.calc.get()
        if value[-1] in '+-*/%':
            value = value[:-1]
        self.calc.delete(0, tk.END)
        self.calc.insert(0, str(float(value) / 100))
        self.calc['state'] = tk.DISABLED

    def add_point(self):
        self.calc['state'] = tk.NORMAL
        value = self.calc.get()
        if value[-1] in '+-*/%':
            value = value[:-1]
        self.calc.delete(0, tk.END)
        if '.' not in value:
            self.calc.insert(0, value + '.')
        elif ('+' in value or '-' in value or '*' in value or '/' in value) and value.count('.') <= 1:
            self.calc.insert(0, value + '.')
        else:
            self.calc.insert(0, value)
        self.calc['state'] = tk.DISABLED

    def add_plus_minus(self):
        self.calc['state'] = tk.NORMAL
        value = self.calc.get()
        if value[-1] in '+-*/%':
            value = value[:-1]
        self.calc.delete(0, tk.END)
        n_val = -1 * float(value)
        if modf(n_val)[0] == 0.0:
            self.calc.insert(0, str(int(n_val)))
        else:
            self.calc.insert(0, str(n_val))
        self.calc['state'] = tk.DISABLED

    # ------------------------------------------ end of add functions
    # ------------------------------------------ create functions

    def create_button(self, digit):
        return tk.Button(
            text=digit,
            command=lambda: self.add_digit(digit),
            font=('Arial', 13),
            bg='#333333',
            fg='#FFFFFF',
            relief=tk.FLAT
        )

    def create_operation_button(self, operation):
        return tk.Button(
            text=operation,
            command=lambda: self.add_operation(operation),
            font=('Arial', 13),
            bg='#FF9F0A',
            fg='#FFFFFF',
            relief=tk.FLAT
        )

    def create_calc_button(self, operation):
        return tk.Button(
            text=operation,
            command=self.calculate,
            font=('Arial', 13),
            bg='#FF9F0A',
            fg='#FFFFFF',
            relief=tk.FLAT
        )

    def create_clear_button(self, operation):
        return tk.Button(
            text=operation,
            command=self.clear,
            font=('Arial', 13),
            bg='#A5A5A5',
            fg='#000000',
            relief=tk.FLAT
        )

    def create_procent_button(self,operation):
        return tk.Button(
            text=operation,
            command=self.add_procent,
            font=('Arial', 13),
            bg='#A5A5A5',
            fg='#000000',
            relief=tk.FLAT
        )

    def create_point_button(self, operation):
        return tk.Button(
            text=operation,
            command=self.add_point,
            font=('Arial', 13),
            bg='#333333',
            fg='#FFFFFF',
            relief=tk.FLAT
        )

    def create_plus_minus_button(self, operation):
        return tk.Button(
            text=operation,
            command=self.add_plus_minus,
            font=('Arial', 13),
            bg='#A5A5A5',
            fg='#000000',
            relief=tk.FLAT
        )

    # ------------------------------------------ end of create functions
    # ------------------------------------------ event

    def press_key(self, event):
        # print(repr(event.char))
        if event.char.isdigit():
            self.add_digit(event.char)
        elif event.char in '+-*/':
            self.add_operation(event.char)
        elif event.char == '\r' or event.char == '=':
            self.calculate()
        elif event.char == '\x08':
            self.clear()
        elif event.char == '%':
            self.add_procent()
        elif event.char == '.':
            self.add_point()


root = tk.Tk()
app = SmallScreenApp(root)
root.mainloop()
