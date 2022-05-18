from tkinter import *

s=''
w=Tk()


def press(n):
    global s
    
    if n=="B":
        n1=len(s)
        s=s[:n1-1]
    elif n=='C':
        s=""
        
    else:    
        s=s+str(n)
     
    x.set(s)
    
   
def result():
    try:
        global s
        t=str(eval(s))
        s=t
        x.set(t)
        
    except:
        x.set("error")
        x.set("")


#buttons on window screen
b1=Button(w,text="1",command=lambda:press(1))
b1.grid(row=0,column=1)
b2=Button(w,text="2",command=lambda:press(2))
b2.grid(row=0,column=2)
b3=Button(w,text="3",command=lambda:press(3))
b3.grid(row=0,column=3)
b4=Button(w,text="4",command=lambda:press(4))
b4.grid(row=1,column=1)
b5=Button(w,text="5",command=lambda:press(5))
b5.grid(row=1,column=2)
b6=Button(w,text="6",command=lambda:press(6))
b6.grid(row=1,column=3)
b7=Button(w,text="7",command=lambda:press(7))
b7.grid(row=2,column=1)
b8=Button(w,text="8",command=lambda:press(8))
b8.grid(row=2,column=2)
b9=Button(w,text="9",command=lambda:press(9))
b9.grid(row=2,column=3)
b0=Button(w,text="0",command=lambda:press(0))
b0.grid(row=3,column=1)

a1=Button(w,text="+",command=lambda:press("+"))
a1.grid(row=3,column=2)
a2=Button(w,text="-",command=lambda:press("-"))
a2.grid(row=3,column=3)
a3=Button(w,text="*",command=lambda:press("*"))
a3.grid(row=4,column=1)
a4=Button(w,text="/",command=lambda:press("/"))
a4.grid(row=4,column=2)
a5=Button(w,text="%",command=lambda:press("%"))
a5.grid(row=4,column=3)
a6=Button(w,text="=",command=result)
a6.grid(row=2,column=0)
a7=Button(w,text="C",command=lambda:press('C'))
a7.grid(row=3,column=0)
a9=Button(w,text=".",command=lambda:press("."))
a9.grid(row=5,column=1)
a9=Button(w,text="backspace",command=lambda:press("B"))
a9.grid(row=4,column=0)





x=StringVar()
e=Entry(w,textvariable=x)
e.grid(row=0,column=0)





w.mainloop()
