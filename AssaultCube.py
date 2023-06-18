import tkinter as tk
from tkinter import font
from ReadWriteMemory import ReadWriteMemory
import time
import threading
from colorama import Fore
import os

rwm = ReadWriteMemory()
process = rwm.get_process_by_name("ac_client.exe")

def main():

    print(Fore.GREEN + "Injected!\n")

    root = tk.Tk()
    root.configure(bg="black")
    root.title("Memory Hacker For AssaultCube v1")
    root.geometry("600x600")
    boldFont = font.Font(weight="bold")
    normalFont = font.Font(weight="normal")

    switch_var1 = tk.IntVar()
    switch_label1 = tk.Label(root, text="OFF", fg="red", bg="black", font=("Arial", 12))
    switch_label1.place(x=200, y=50)

    switch_var2 = tk.IntVar()
    switch_label2 = tk.Label(root, text="OFF", fg="red", bg="black", font=("Arial", 12))
    switch_label2.place(x=200, y=75)

    switch_var3 = tk.IntVar()
    switch_label3 = tk.Label(root, text="OFF", fg="red", bg="black", font=("Arial", 12))
    switch_label3.place(x=200, y=100)


    stop_hack1 = threading.Event()
    stop_hack2 = threading.Event()
    stop_hack3 = threading.Event()

    def noReload():
        def hack_thread():
            process.open()
            baseaddress = 0x400000 + 0x1A3344
            pointer = process.get_pointer(baseaddress, offsets=[0x4, 0x64, 0x98, 0x30, 0x1B8])
            while not stop_hack1.is_set():
                process.write(pointer, 20)
                time.sleep(0.1)

        if switch_var1.get() == 1:
            switch_label1.config(text="ON", fg="green")
            os.system("cls")
            print(Fore.GREEN + "No Reload is ON\n")
            stop_hack1.clear()
            threading.Thread(target=hack_thread).start()
        else:
            switch_label1.config(text="OFF", fg="red")
            os.system("cls")
            print(Fore.RED + "No Reload is OFF\n")
            stop_hack1.set()

    def unlimitedAmmo():
        def hack_thread():
            process.open()
            baseaddress = 0x400000 + 0x183828
            pointer = process.get_pointer(baseaddress, offsets=[0x8, 0x668, 0x30, 0x64, 0x30, 0xA08])
            while not stop_hack2.is_set():
                process.write(pointer, 20)
                time.sleep(0.1)

        if switch_var2.get() == 1:
            switch_label2.config(text="ON", fg="green")
            os.system("cls")
            print(Fore.GREEN + "Unlimited Ammo is ON\n")
            stop_hack2.clear()
            threading.Thread(target=hack_thread).start()
        else:
            os.system("cls")
            switch_label2.config(text="OFF", fg="red")
            print(Fore.RED + "Unlimited Ammo is OFF\n")
            stop_hack2.set()

    def unlimitedHealth():
        def hack_thread():
            process.open()
            baseaddress2 = 0x400000+0x074504
            pointer2 = process.get_pointer(baseaddress2, offsets=[0x34, 0x14, 0x80, 0x34, 0x20, 0x4C, 0xEC])
            while not stop_hack2.is_set():
                process.write(pointer2, 100)
                time.sleep(0.1)

        if switch_var3.get() == 1:
            switch_label3.config(text="ON", fg="green")
            os.system("cls")
            print(Fore.GREEN + "Unlimited Health is ON\n")
            stop_hack3.clear()
            threading.Thread(target=hack_thread).start()
        else:
            switch_label3.config(text="OFF", fg="red")
            os.system("cls")
            print(Fore.RED + "Unlimited Health is OFF\n")
            stop_hack2.set()

    menuName = tk.Label(text="Memory Hacker", fg="red", bg="black", font=boldFont)
    menuName.pack()

    gameName = tk.Label(text="AssaultCube Version", fg="red", bg="black", font=boldFont)
    gameName.pack()

    module1 = tk.Label(text="No Reload", fg="green", bg="black", font=normalFont)
    module1.place(x=0, y=50)

    module2 = tk.Label(text="Unlimited Ammo", fg="green", bg="black", font=normalFont)
    module2.place(x=0, y=75)

    module3 = tk.Label(text="Unlimited Health", fg="green", bg="black", font=normalFont)
    module3.place(x=0, y=100)

    switch1 = tk.Checkbutton(root, bg="black", variable=switch_var1, command=noReload, onvalue=1, offvalue=0)
    switch1.place(x=160, y=50)

    switch2 = tk.Checkbutton(root, bg="black", variable=switch_var2, command=unlimitedAmmo, onvalue=1, offvalue=0)
    switch2.place(x=160, y=75)

    switch3 = tk.Checkbutton(root, bg="black", variable=switch_var3, command=unlimitedHealth, onvalue=1, offvalue=0)
    switch3.place(x=160, y=100)

    root.mainloop()


if __name__ == "__main__":
    main()
