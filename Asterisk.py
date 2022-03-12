from tkinter import *
import win32gui, win32con

def main():
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
    main_window = Tk()
    Label(main_window, text="Hello World").pack()
    main_window.mainloop()

if __name__ == '__main__':
    main()