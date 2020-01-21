from tkinter import*

app=Tk()
app.geometry("260x380")
app.title("CALCULADORA")

app.config(background='Gray')

expression=StringVar()
operator=""

def clickbut(number):  
     global operator
     operator=operator+str(number)
     expression.set(operator)

def equlbut():
     global operator
     add=str(eval(operator))
     expression.set(add)
     operator=''
def equlbut():
     global operator
     sub=str(eval(operator))
     expression.set(sub)
     operator=''     
def equlbut():
     global operator
     mul=str(eval(operator))
     expression.set(mul)
     operator=''
def equlbut():
     global operator
     div=str(eval(operator))
     expression.set(div)
     operator=''    

def clrbut():
     expression.set('')

     
apptext=Entry(app,font=("Courier New",22,'bold'),textvar=expression,width=25,bd=1,bg='powder blue')
apptext.pack()

but1=Button(app,padx=14,pady=14,bd=0,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=2,y=43)

but2=Button(app,padx=14,pady=14,bd=0,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=2,y=112)

but3=Button(app,padx=14,pady=14,bd=0,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=2,y=182)

but4=Button(app,padx=14,pady=14,bd=0,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=50,y=43)

but5=Button(app,padx=14,pady=14,bd=0,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=50,y=112)

but6=Button(app,padx=14,pady=14,bd=0,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=50,y=182)

but7=Button(app,padx=14,pady=14,bd=0,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=98,y=43)

but8=Button(app,padx=14,pady=14,bd=0,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=98,y=112)

but9=Button(app,padx=14,pady=14,bd=0,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=98,y=182)

but0=Button(app,padx=14,pady=14,bd=0,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=2,y=252)

butdot=Button(app,padx=38,pady=14,bd=0,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=50,y=252)

butpl=Button(app,padx=14,pady=14,bd=0,bg='white',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
butpl.place(x=147,y=43)

butsub=Button(app,padx=14,pady=14,bd=0,bg='white',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
butsub.place(x=147,y=112)

butml=Button(app,padx=14,pady=14,bd=0,bg='white',text="*",command=lambda:clickbut("*"),font=("Courier New",16,'bold'))
butml.place(x=147,y=182)

butdiv=Button(app,padx=14,pady=14,bd=0,bg='white',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
butdiv.place(x=147,y=252)

butclear=Button(app,padx=14,pady=119,bd=0,bg='white',text="CE",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=200,y=43)

butequal=Button(app,padx=118,pady=14,bd=0,bg='white',command=equlbut,text="=",font=("Courier New",16,'bold'))
butequal.place(x=2,y=318)
app.mainloop()