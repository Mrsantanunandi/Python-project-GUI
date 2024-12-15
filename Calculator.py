from tkinter import*
root=Tk()
root.geometry("500x670")
root.title("Santanu's Calculator")
def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                expression = scvalue.get().replace("√", "**0.5").replace("^", "**")
                value=eval(expression)
            except Exception as e:
                value="Math Error"
        scvalue.set(value)
        screen.update
    elif text=="c":
        scvalue.set("")
        screen.update
    else:
        scvalue.set(scvalue.get()+text)
        screen.update
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 43 bold",bg="pink")
screen.pack(padx=10,pady=15,fill="x")
f=Frame(root,bg="blue")
b=Button(f,text="7",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=27)
b.bind("<Button-1>",click)

b=Button(f,text="8",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=22)
b.bind("<Button-1>",click)

b=Button(f,text="9",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=22)
b.bind("<Button-1>",click)

b=Button(f,text="+",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=24,pady=18)
b.bind("<Button-1>",click)
f.pack(fill="x")

f1=Frame(root,bg="blue")
b=Button(f1,text="4",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=27)
b.bind("<Button-1>",click)

b=Button(f1,text="5",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=22)
b.bind("<Button-1>",click)

b=Button(f1,text="6",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=22)
b.bind("<Button-1>",click)

b=Button(f1,text="-",font="lucida 27 bold",padx=15,bg="grey")
b.pack(side=LEFT,padx=24,pady=18)
b.bind("<Button-1>",click)
f1.pack(fill="x")

f3=Frame(root,bg="blue")
b=Button(f3,text="1",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=27)
b.bind("<Button-1>",click)
b=Button(f3,text="2",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=22)
b.bind("<Button-1>",click)
b=Button(f3,text="3",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=22)
b.bind("<Button-1>",click)
b=Button(f3,text="*",font="lucida 27 bold",padx=15,bg="grey")
b.pack(side=LEFT,padx=24,pady=18)
b.bind("<Button-1>",click)
f3.pack(fill="x")

f4=Frame(root,bg="blue")
b=Button(f4,text="0",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=27)
b.bind("<Button-1>",click)
b=Button(f4,text="c",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=22)
b.bind("<Button-1>",click)
b=Button(f4,text="=",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=22)
b.bind("<Button-1>",click)
b=Button(f4,text="/",font="lucida 27 bold",padx=15,bg="grey")
b.pack(side=LEFT,padx=24,pady=18)
b.bind("<Button-1>",click)
f4.pack(fill="x")

f5=Frame(root,bg="blue")
b=Button(f5,text=".",font="lucida 27 bold",padx=14,bg="grey")
b.pack(side=LEFT,padx=27)
b.bind("<Button-1>",click)
b=Button(f5,text="%",font="lucida 27 bold",padx=6,bg="grey")
b.pack(side=LEFT,padx=22)
b.bind("<Button-1>",click)
b=Button(f5,text="√",font="lucida 27 bold",padx=10,bg="grey")
b.pack(side=LEFT,padx=22)
b.bind("<Button-1>",click)
b=Button(f5,text="^",font="lucida 27 bold",padx=11,bg="grey")
b.pack(side=LEFT,padx=24,pady=18)
b.bind("<Button-1>",click)
f5.pack(fill="x")

root.mainloop()