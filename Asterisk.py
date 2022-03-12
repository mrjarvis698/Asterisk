from tkinter import *
import win32gui, win32con

def main():
    #win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
    main_window = Tk()
    main_window.geometry("1024x768")
    main_window.state('zoomed')
    main_window.overrideredirect(True)
    Label(main_window, text="Hello World").pack()
    main_window.mainloop()

if __name__ == '__main__':
    main()