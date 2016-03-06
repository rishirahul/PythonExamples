#tutorial link : http://www.python-course.eu/tkinter_labels.php
#AIM: make a quiz_box

#from tkinter import *
import tkinter as tk

question = "Question: This is question"
hint = "Hint: This is hint"
title = "Quiz"

root = tk.Tk()
v = tk.IntVar()

def postSubmitFn():
    print(v.get())
    if(v.get() is 1):
        tk.Label(root,justify=tk.LEFT, padx = 10, pady = 10, text= "correct",font="bold").pack()
        root.destroy
    else:
        tk.Label(root,justify=tk.LEFT, padx = 10, pady = 10, text= "wrong",font="bold").pack()
        root.destroy


root.title(title)
tk.Label(root,justify=tk.LEFT, padx = 10, pady = 10, text= question,fg="green").pack()
tk.Label(root,justify=tk.LEFT, padx = 10, pady = 10, text= hint,font="bold").pack()
tk.Radiobutton(root, text="option1", padx = 30, variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="option2", padx = 30, variable=v, value=2).pack(anchor=tk.W)
tk.Radiobutton(root, text="option3", padx = 30, variable=v, value=3).pack(anchor=tk.W)
tk.Radiobutton(root, text="option4", padx = 30, variable=v, value=4).pack(anchor=tk.W)
tk.Label(root,justify=tk.LEFT, padx = 10, pady = 20, text= "",font="bold").pack()
tk.Button(root, text='Submit', width=25, command=postSubmitFn).pack()
root.mainloop()
