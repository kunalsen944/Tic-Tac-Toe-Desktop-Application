from tkinter import *
import random
from tkinter import messagebox
root = Tk()
root.title("Tic Tac Toe")
c=1
p=None
flag=0
def show(bt):
    global c
    global rand_list
    global p
    global flag
    if flag == 0:
        if bt["text"] not in ["X","O"]:
            c=c+1
            if c%2==0:
                bt["text"]="X"
                bt.configure(background="Cyan")
                rand_list.remove(bt)
                p=True
                show(random.choice(rand_list))
            else:
                if len(rand_list) is not 0:
                    bt = random.choice(rand_list)
                    bt["text"]="O"
                    rand_list.remove(bt)
                    bt.configure(background="Green")
                    p=False


            if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O") or (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):
                print("Player Two Is winner")
                messagebox.showinfo("","Player Two Is Winner")
                flag=1
            elif (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X") or (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
                print("Player One Is winner")
                messagebox.showinfo("","Player One Is Winner")
                flag=1
        if len(rand_list)==0:
                print("Game Is Draw")
                messagebox.showinfo("", "Game Is Draw")
                flag=2

    elif flag==1:
        print("Already Win")
        messagebox.showinfo("", "Already Win ")
    elif flag==2:
        print("Game Is Draw")
        messagebox.showinfo("", "Game Is Already Draw")





b1 = Button(root,text='',height=5,width=10,command=lambda : show(b1))
b2 = Button(root,text='',height=5,width=10,command=lambda : show(b2))
b3 = Button(root,text='',height=5,width=10,command=lambda : show(b3))
b4 = Button(root,text='',height=5,width=10,command=lambda : show(b4))
b5 = Button(root,text='',height=5,width=10,command=lambda : show(b5))
b6 = Button(root,text='',height=5,width=10,command=lambda : show(b6))
b7 = Button(root,text='',height=5,width=10,command=lambda : show(b7))
b8 = Button(root,text='',height=5,width=10,command=lambda : show(b8))
b9 = Button(root,text='',height=5,width=10,command=lambda : show(b9))

b1.grid(row=5,column=0,sticky=S)
b2.grid(row=5,column=1,sticky=S+E)
b3.grid(row=5,column=2,sticky=W)
b4.grid(row=6,column=0,sticky=W)
b5.grid(row=6,column=1,sticky=W+E)
b6.grid(row=6,column=2,sticky=S)
b7.grid(row=7,column=0,sticky=W)
b8.grid(row=7,column=1,sticky=W+E)
b9.grid(row=7,column=2,sticky=S)

rand_list = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
root.mainloop()
