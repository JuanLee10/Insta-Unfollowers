from Web_automation import InstaAnalyzer
from App import GUI
import tkinter as tk


def main():
    tkWindow = tk.Tk()
    Screen = GUI(tkWindow)
    print("made it")
    tkWindow.mainloop()

if __name__ == "__main__":
    main()