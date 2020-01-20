#####Dependencies######(1,7,19)
from tkinter import *
from tkinter import messagebox
import math #needef for fruther improvements


#####window creation##########
window=Tk()
window.title("Simple-Calculator")
window.geometry("450x540")
window.resizable(height=False,width=False) #window cannot be expanded
frame=Frame(window)#converting into frame format
frame.pack(side=TOP)
'''frame2=Frame(window)
frame2.pack(side=BOTTOM)'''
equ=StringVar()
#declaring a string variable
entry=Entry(frame,font=("Coureier",40,),textvariable=equ,justify=RIGHT,relief=FLAT)
#getting input	tile like theme
entry.pack(ipadx=450,ipady=30)
# frame l X b


#######Function of the calculator#########
global eq,fact
eq="";fact=""
def clks(x):
    global eq,fact
    #no need of entry.get() ---> used to get from keyboard,but here we are clicking with known number(x)
    entry.insert(END,x)
	#appear on the entry field,end means insert from last
    eq=eq+str(x)
    if "!" in eq:
        fact=eq
def answer():
    try:
        t=1
        global eq,fact
        if "!" in fact:
            fact=fact.replace("!","")
            for i in range(1,int(fact)+1):
                t*=i
            entry.delete(0,END)
			#removing all the characters form entry field
            entry.insert(END,str(t))
        else:
            ans=eval(eq)
            entry.delete(0,END)
            entry.insert(END,ans)
    except:
        entry.delete(0,END)
        entry.insert(END,"SYNTAX-ERR")
def clear():
    global eq
    entry.delete(0,END)
    eq=""

	
	
	###########Buttons#############################
b1=Button(window,text="7",height=6,width=12,relief=FLAT,bg="pink",fg="red",bd=5,
          command=lambda:clks("7")).place(x=0,y=130)
b2=Button(window,text="8",height=6,width=12,relief=FLAT,bg="pink",fg="red",bd=5
          ,command=lambda:clks("8")).place(
    x=95,y=130)
b3=Button(window,text="9",height=6,width=12,relief=FLAT,bg="pink",fg="red",bd=5
          ,command=lambda:clks("9")).place(
    x=190,y=130)
b4=Button(window,text="4",height=6,width=12,relief=FLAT,bg="pink",fg="red",bd=5
         ,command=lambda:clks("4") ).place(x=0,y=240)
b5=Button(window,text="5",height=6,width=12,relief=FLAT,bg="pink",fg="red",bd=5
          ,command=lambda:clks("5")).place( x=95,y=240)
b6=Button(window,text="6",height=6,width=12,relief=FLAT,bg="pink",fg="red",bd=5
         ,command=lambda:clks("6") ).place(x=190,y=240)
b7=Button(window,text="1",height=6,width=12,relief=FLAT,bg="pink",fg="red",bd=5
         ,command=lambda:clks("1") ).place(x=0,y=350)
b8=Button(window,text="2",height=6,width=12,relief=FLAT,bg="pink",fg="red",bd=5
         ,command=lambda:clks("2") ).place(x=95,y=350)
b9=Button(window,text="3",height=6,width=12,relief=FLAT,bg="pink",fg="red",bd=5
         ,command=lambda:clks("3") ).place(x=190,y=350)
b0=Button(window,text="0",height=4,width=24,relief=FLAT,bg="pink",fg="red",bd=5
         ,command=lambda:clks("0") ).place( x=0,y=460)
bdot=Button(window,text=".",height=4,width=12,relief=FLAT,bg="pink",fg="red",bd=5
            ,command=lambda:clks(".")).place(x=184,y=460)
clr=Button(window,text="←",height=6,width=12,relief=FLAT,bg="powder blue",fg="green",bd=5
           ,command=clear).place(
    x=280,y=130)
div=Button(window,text="÷",height=6,width=12,relief=FLAT,bg="orange",fg="black",bd=5
           ,command=lambda:clks("/")).place(x=281,y=240)
mul=Button(window,text="*",height=6,width=12,relief=FLAT,bg="green",fg="yellow",bd=5
          ,command=lambda:clks("*") ).place( x=281,y=350)
equ=Button(window,text="=",height=4,width=24,relief=FLAT,bg="red",fg="white",bd=5
         ,command=answer ).place(
              x=281,y=460)
plu=Button(window,text="+",height=6,width=9,relief=FLAT,bg="purple",fg="powder blue",bd=5
          ,command=lambda:clks("+") ).place(x=372,y=240)
fa=Button(window,text="!(..)",height=6,width=9,relief=FLAT,bg="black",fg="yellow",bd=5
         ,command=lambda:clks("!") ).place(x=372,y=130)
mul=Button(window,text="-",height=6,width=9,relief=FLAT,bg="blue",fg="yellow",bd=5
          ,command=lambda:clks("-") ).place( x=371,y=350)

window.mainloop()
