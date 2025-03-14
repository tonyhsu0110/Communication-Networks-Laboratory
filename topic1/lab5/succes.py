# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 04:57:52 2023

@author: Tony
"""

import tkinter as tk
import pickle as pk
from PIL import Image, ImageTk

window1 = tk.Tk()
# 第一個視窗（登入介面）
window1.title('Lab5')
f1 = tk.Frame(window1)
f2 = tk.Frame(window1)
# f1放檔名為'photo.jpg'的圖片，並重新規劃圖片大小
image1 = ImageTk.PhotoImage(Image.open('photo.jpg').resize((320, 240)))
im = tk.Label(f1, image = image1)
    
# build up variation for the program
userName = tk.StringVar()
pwd = tk.StringVar()
inputName = tk.StringVar()
inputPwd = tk.StringVar()
var5 = tk.StringVar()
entry1 = tk.Entry(f2, textvariable=userName).grid(row=0, column=1)
# 密碼要用*遮
entry2 = tk.Entry(f2, textvariable=pwd, show='*').grid(row=1, column=1)
Label1 = tk.Label(f2, text="User:").grid(row=0, column=0)
Label2 = tk.Label(f2, text="Password:").grid(row=1, column=0)

def login():
    entry_usr = entry1.get()
    entry_pwd = entry2.get()

    try:
        try:
            # 讀取檔案中的data
            with open('user_info.pickle', 'rb') as f:
                user_info = pk.load(f)
        except EOFError:
            user_info = {}
    except FileNotFoundError:
        user_info = {}

    if entry_usr in user_info:  # user name exists
        if entry_pwd == user_info[entry_usr]:  #password correct
            tk.messagebox.showinfo(message="sucessful")
        else:  # password wrong
            tk.messagebox.showerror(message="password incorrect")
    else:  # user name does not exist
        # ask the user if he/she wants to create an account 
        sign_up = tk.messagebox.askyesno(
                  message="Do you want to create an account by your input?")

        if sign_up:
            with open('user_info.pickle', 'wb') as f:
                #user_info={entry_usr, entry_pwd}
                user_info[entry_usr] = entry_pwd
                pk.dump(user_info, f)

# set up location and size of the buttons for 'Log In' and 'Sign Up'
Btnlog = tk.Button(f2, text="Log In", borderwidth=3, width=8,
                   height=1, command=lambda: login()).grid(row=2, column=0)
Btnsign = tk.Button(f2, text="Sign Up", borderwidth=3, width=9,
                    height=1, command=lambda: signup1()).grid(row=2, column=1)


def signup1():
    window2 = tk.Toplevel()
    #window大小
    window2.geometry('300x300')
    f3 = tk.Frame(window2)
    Label3 = tk.Label(f3, text="User Name:").grid(row=0, column=0)
    Label4 = tk.Label(f3, text="Password:").grid(row=1, column=0)
    Label5 = tk.Label(f3, text="Confirm Password:").grid(row=2, column=0)
    BtnsignUp = tk.Button(f3, text="Sign Up", borderwidth=5, width=10,
                         height=1, command=lambda: signup2()).grid(row=3, column=0)
    entry3 = tk.Entry(f3, textvariable=inputName).grid(row=0, column=1)
    # 密碼用*遮
    entry4 = tk.Entry(f3, textvariable=inputPwd, show='*').grid(row=1, column=1)
    entry5 = tk.Entry(f3, textvariable=var5, show='*')
    #assign location (another method to set up)
    entry5.grid(row=2, column=1)
    f3.pack()  #這行還是要打，才能讓視窗正常出現

    def signup2():  #申請帳號後，當按下Sign Up會到這裡
        sign_usr = entry3.get()
        sign_pwd = entry4.get()
        sign_pwd_again = entry5.get()

        try:
            try:
                with open('user_info.pickle', 'rb') as f:
                    user_info = pk.load(f)
                    print(user_info)
            except EOFError:
                user_info = {}
        except FileNotFoundError:
            user_info = {}

        # check if the username has been adopted
        if sign_usr in user_info:
            tk.messagebox.showerror(message="User name exists!")
        else:
            if sign_pwd == sign_pwd_again:
                with open('user_info.pickle', 'wb') as f:
                    user_info[sign_usr] = sign_pwd
                    pk.dump(user_info, f)
                tk.messagebox.showinfo(message="Sucessful!")
                window2.destroy()
            else:
                tk.messagebox.showerror(message="Password incorrect!")

im.pack()
f1.pack()
f2.pack()
window1.mainloop()