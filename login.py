from tkinter import *
import tkinter as tk
from tkinter import messagebox
import subprocess
root=tk.Tk()
root.title("Aditya's Quiz")
root.configure(bg="Cyan")
root.minsize(200,200)
root.maxsize(2000,2000)
d1={"Hinal Shah":"hinalshah","Parshwa Shah":"parshwashah","Aditya Shah":"adityashah","Taneesh Dasgupta":"taneeshdasgupta"}
def login():
    username=b1_entry.get()
    password=b2_entry.get()
    if username in d1 and d1[username]==password:
         tk.messagebox.showinfo("Successful")
         print("Login Successful")
         execute()
    else:
        tk.messagebox.showerror("Invalid Content")
        print("Invalid Username or Password")

def execute():
    try:
        subprocess.run(['python','InteractiveQuiz.py'])
    except:
        print("Exception Error")

p1=tk.PhotoImage(file="Indus 2.png")
p2=tk.Label(image=p1,bg="Cyan")
p2.pack(pady=20,side=TOP)
b1 = tk.Label(root,text="Enter username: " ,font="Arial 14 bold",bg="Cyan" )
b1.pack(pady=10)
b1_entry = tk.Entry(root)
b1_entry.pack(pady=10)
b2=tk.Label(root,text="Enter Password: ", font="Arial 14 bold",bg="Cyan")
b2.pack()
b2_entry = tk.Entry(root)
b2_entry.pack(pady=10)

button=tk.Button(root,text="Login",font="Arial 10 bold",command=login,bg="yellow")
button.pack()
root.mainloop()



