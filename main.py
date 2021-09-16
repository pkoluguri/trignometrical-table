import tkinter as tk
from tkinter.constants import CENTER, DISABLED, GROOVE, PIESLICE, SUNKEN, TOP
import random

window = tk.Tk()
sin0 = "0"
sin30 = "1/2"
sin45 = "1/root2"
sin60 = "root3/2"
sin90 = "1"

cos0="1"
cos30="root3/2"
cos45="1/root2"
cos60="1/2"
cos90="0"

tan0="0"
tan30="1/root3"
tan45="1"
tan60="root3"
tan90="not defined"

cosec0="Not defined"
cosec30="2"
cosec45="root2"
cosec60="2/root3"
cosec90="1"

sec0="1"
sec30="2/root3"
sec45="root2"
sec60="2"
sec90="Not defined"

cot0="Not defined"
cot30="root3"
cot45="1"
cot60="1/root3"
cot90="0"

values_w = []

class Table:
    def __init__(self,root):
        for i in range(total_rows):
            if i >0:
                values_w.append(values)
            values=[]
            for j in range(total_columns):
                text = tk.StringVar()
                self.e = tk.Entry(root, width=20, fg='black',
                               font=('Arial',16,'bold'),textvariable=text)
                self.e.grid(row=i+1, column=j)
                values.append(text)
                if i == 0 or j == 0:
                   self.e.insert(tk.END, lst[i][j])
                   self.e.configure(state='readonly')
                self.e.insert(tk.END, lst[i][j])
        self.btn = tk.Button(root,width=20,text="Submit",relief=SUNKEN,background="tomato",foreground="white",command=submit)
        self.btn.grid(row=total_rows+1,column=2)
        self.btn = tk.Button(root,width=20,text="Refresh",relief=SUNKEN,background="tomato",foreground="white",command=refresh)
        self.btn.grid(row=total_rows+1,column=4)

def refresh():
    global t
    global lst
    t.e.grid_remove()
    lst = load_random_values()
    t=Table(window)

def submit():
    global values_w
    global total_rows
    global total_columns
    correct_values= [[sin0,sin30,sin45,sin60,sin90],
                     [cos0,cos30,cos45,cos60,cos90],
                     [tan0,tan30,tan45,tan60,tan90],
                     [cosec0,cosec30,cosec45,cosec60,cosec90],
                     [sec0,sec30,sec45,sec60,sec90],
                     [cot0,cot30,cot45,cot60,cot90] ]
    not_correct = False
    for i in range(total_rows-1):
      for j in range(total_columns):
          if j > 0 and i > 0:
               if values_w[i][j].get() != "":
                   if values_w[i][j].get().lower().replace(" ","") == correct_values[i-1][j-1].lower().replace(" ",""):
                       pass
                   else:
                       text.configure(text="Some of the values are incorrect",foreground="red")
                       not_correct = True
                       return
               else:
                   text.configure(text="Please Fill all the values",foreground="red")
                   not_correct = True
                   return
               print(not_correct)
    if not not_correct: 
                print("correct!")
                text.configure(text="Every Value is Correct!",foreground="green")
                refresh()  

def load_random_values():
   lst = [('ratios',0,30,45,60,90)]
   lst.append(('sin',random.choice(['',sin0]),random.choice(['',sin30]),random.choice(['',sin45]),random.choice(['',sin60]),random.choice(['',sin90])))
   lst.append(('cos',random.choice(['',cos0]),random.choice(['',cos30]),random.choice(['',cos45]),random.choice(['',cos60]),random.choice(['',cos90])))
   lst.append(('tan',random.choice(['',tan0]),random.choice(['',tan30]),random.choice(['',tan45]),random.choice(['',tan60]),random.choice(['',tan90])))
   lst.append(('cosec',random.choice(['',cosec0]),random.choice(['',cosec30]),random.choice(['',cosec45]),random.choice(['',cosec60]),random.choice(['',cosec90])))
   lst.append(('sec',random.choice(['',sec0]),random.choice(['',sec30]),random.choice(['',sec45]),random.choice(['',sec60]),random.choice(['',sec90])))
   lst.append(('cot',random.choice(['',cot0]),random.choice(['',cot30]),random.choice(['',cot45]),random.choice(['',cot60]),random.choice(['',cot90])))
   return lst

lst = load_random_values()

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

text=tk.Label(window,text="")
text.grid(column=3,row=total_rows+1)
   
# create root window
t = Table(window)

window.mainloop()