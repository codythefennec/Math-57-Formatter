from tkinter import *
import tkinter as tk
from tkinter import ttk
import pyperclip

root = Tk()
root.title('Math 57 Formatter')
frm = ttk.Frame(root, padding=10)
frm.grid()

#variables to fill
firstName = tk.StringVar(root)
lastName = tk.StringVar(root)
questionNum = tk.StringVar(root)
homeworkTitle = tk.StringVar(root)

def copy2clip(txt):
    pyperclip.copy(txt)
    return

def openNewWindow():
     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("600x100")
 
    # A Label widget to show in toplevel
    Label(newWindow, text ="You cannot have letters for # of questions goofy.").pack()
    Button(newWindow, text="Damn..", command=lambda:newWindow.destroy(),justify=CENTER).pack()

def submit():
    docQuestionNum = questionNum.get()
    try:
        docQuestionNum = int(docQuestionNum)
    except:
        if (not isinstance(docQuestionNum, int)):
            openNewWindow()
            return
    
    print(docQuestionNum)
    docFirstName = firstName.get()
    docLastName = lastName.get()
    docHomeworkTitle = homeworkTitle.get()
    create_formatting(docFirstName, docLastName, docHomeworkTitle, docQuestionNum)
    return

def create_formatting(docFirstName, docLastName, docHomeworkTitle, docQuestionNum):
    out = r"""
\documentclass[12pt,reqno]{article}
\usepackage{amsmath,amssymb,amsthm,graphicx,xspace}
\newcommand{\matlab}{\textsc{Matlab}\xspace}
\graphicspath{{graphics/}}
\begin{document}

\title{MATH 57}
\author{""" + docFirstName + ' ' + docLastName + r"""}
\date{Spring 2024}

\maketitle

\newpage

\section{""" + docHomeworkTitle + r"""}
\label{s:""" + docHomeworkTitle + r"""}"""
    
    for x in range(docQuestionNum):
        out = out + '\n'
        out = out + ("\subsection{Problem %s [NOT DONE]}"%(x + 1))
        out = out + ('\label{ss:problem %s}'%(x + 1))
    
    out = out + '\n'
    out = out + r"\end{document}"

    print(out)
    copy2clip(out)
    return

ttk.Label(frm, text="Math 57 Auto Formatter !!!").grid(column=0, row=0, columnspan=3)
#ttk.Label(frm, text="This will create a document named with the convention: [yourName]_Math_57_[homeworkName]").grid(column=0, row=1, columnspan=10)
ttk.Label(frm, text = 'Number of questions:').grid(column=0,row=3)
questionEntry = ttk.Entry(frm, text = "1 - 14", textvariable=questionNum).grid(column=1, row=3)
ttk.Label(frm, text="First name: ").grid(column=0, row=4)
firstNameEntry = ttk.Entry(frm, text = "John",textvariable=firstName).grid(column=1, row=4)
ttk.Label(frm, text="Last name: ").grid(column=0, row=5)
lastNameEntry = ttk.Entry(frm, text = "Doe", textvariable=lastName).grid(column=1, row=5)
ttk.Label(frm, text="Homework Title: ").grid(column=0, row=6)
homeworkTitleEntry = ttk.Entry(frm, text = "Math 57", textvariable=homeworkTitle).grid(column=1, row=6)
ttk.Button(frm, text='Submit', command=submit).grid(column=0, row=7,pady=20)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=7, pady=20, padx=20)
root.mainloop()

