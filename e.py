import tkinter as tk
from tkinter import *
import os

def regUser():
    usernameInfo = username.get()
    passwordInfo = password.get()
    
    file=open(usernameInfo, "w")
    file.write(usernameInfo+"\n")
    file.write(passwordInfo)
    file.close()
    
    usEntry.delete(0, END)
    psEntry.delete(0, END)
    
    successLabel = tk.Label(screen1, text="Registration successful :)", fg="green", font=("calibri",11)).pack()
def register():
    global username, password, psEntry, usEntry
    screen1.configure(bg='#4D4DFF')
    
    username = StringVar()
    password = StringVar()
    
    title  = tk.Label(screen1, text="Please enter details below .u.", font=("Calibri, 20"), bg="#4D4DFF").pack(pady=30)
    usLabel = tk.Label(screen1, text = "Username * ", font=("Calibri, 15"), bg="#4D4DFF", fg="#000033").pack(pady=5)
    usEntry = tk.Entry(screen1, textvariable = username, width= 30)
    usEntry.pack()
    psLabel = tk.Label(screen1, text = "Password * ", font=("Calibri, 15"), bg="#4D4DFF", fg="#000033").pack(pady=5)
    psEntry = tk.Entry(screen1, textvariable = password, width= 30)
    psEntry.pack()
    regButton = tk.Button(screen1, text = "Register", width = 10, height = 1, command = regUser, font=("Calibri, 15"), bg="#4D4DFF", fg="#000033").pack(pady=20)
    
def loginVerify():
    global correctUser
    usernameVerify = userVerify.get()
    passwordVerify = passVerify.get()
    
    userEntryLog.delete(0,END)
    passEntryLog.delete(0,END)
    
    listOfFiles = os.listdir()
    if usernameVerify in listOfFiles:
        currentUser = open(usernameVerify, "r")
        verify = currentUser.read().splitlines()
        if passwordVerify in verify:
            correctUser = verify[0]
            loginSuccess()
        else:
            passwordWrong()
    else:
        userNotFound()
        
def loginSuccess():
    print(correctUser)
    appScreen = Toplevel(root)
    appScreen.title("Success")
    appScreen.geometry("500x500")
    successNotif = tk.Label(appScreen,text="Hi "+correctUser, fg="green").pack()
    Button(appScreen, text = "Hi", command = appScreen.destroy).pack()

def passwordWrong():
    passWrong = Toplevel(root)
    passWrong.title("Password Incorrect")
    passWrong.geometry("500x500")
    successNotif = tk.Label(passWrong,text="YOU WERE WRONG XDDDDD POINT AND LAUGH HAHHAHAHAHAHAHAHAHA", fg="red").pack()
    Button(passWrong, text = ":(", command = passWrong.destroy).pack()
def userNotFound():
    userWrong = Toplevel(root)
    userWrong.title("Username Not Found")
    userWrong.geometry("500x500")
    successNotif = tk.Label(userWrong,text="I searched everywhere and couldn't find the username").pack()
    Button(userWrong, text = "huh", command = userWrong.destroy).pack()
    
def login():
    global userVerify, passVerify, userEntryLog, passEntryLog
    screen2.configure(bg="#333333")
    
    userVerify = StringVar()
    passVerify = StringVar()
    
    enterDetailsLabel = tk.Label(screen2, text="Please enter login details", font=("Calibri, 20"), bg="#333333", fg="#FF3399").pack(pady=30)
    usLabel = tk.Label(screen2, text="Username * ", font=("Calibri, 15"), bg="#333333", fg="#FFFFFF").pack()
    userEntryLog = tk.Entry(screen2, textvariable = userVerify)
    userEntryLog.pack()
    psLabel = tk.Label(screen2, text="Password * ", font=("Calibri, 15"), bg="#333333", fg="#FFFFFF").pack()
    passEntryLog = tk.Entry(screen2, textvariable = passVerify, show="*")
    passEntryLog.pack()
    loginButton = tk.Button(screen2, text="Login", width=10, height=1, command=loginVerify, font=("Calibri, 15"), bg="#3B3B3B", fg="#FFFFFF").pack(pady=20)
    
def switchScreen(frame, name):
    frame.tkraise()
    frame.grid(row=0, column=0)
    
    if(name == "login"):
        login()
    elif(name == "reg"):
        register()
    
def mainStart():
    global root, screen2, screen1, screen0
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Login")
    root.configure(bg='#333333')
    root.resizable(False, False)
    
    parentFrame = tk.Frame(root, bg='#333333', highlightbackground="blue", highlightthickness=2)
    parentFrame.pack()
    
    
    screen0 = tk.Frame(parentFrame)
    screen1 = tk.Frame(parentFrame)
    screen2 = tk.Frame(parentFrame)
    
    title = tk.Label(screen0, text = "Goal Setter",bg ="#333333", fg="#FF3399", font=("Calibri, 23")).pack(pady=20)
    loginButton = tk.Button(screen0, text="Login", height="2", width="30",command=lambda:switchScreen(screen2, "login"), bg ="#3B3B3B", fg="#FFFFFF", font=("Calibri, 13")).pack()
    regButton = tk.Button(screen0, text="Register", height="2", width="30",command=lambda:switchScreen(screen1, "reg"), bg ="#3B3B3B", fg="#FFFFFF", font=("Calibri, 13")).pack()
    screen0.tkraise()
    screen0.grid(row=0, column=0)
    
    
    root.mainloop()

mainStart()
