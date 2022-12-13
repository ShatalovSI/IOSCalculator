import tkinter as tk
import IOS_Calculator


def main():
    root = tk.Tk()
    app = IOS_Calculator.SmallScreenApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
