from tkinter import *
home = Tk()
home.geometry("380x500")
text_Input = StringVar()
operator = "  "
f1 = Frame(home, width=0, height=0, relief=RAISED)
f1.pack(side=LEFT)
f2 = Frame(home, width=0, height=0, relief=RAISED)
f2.pack(side=LEFT)
def  btnclick (numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
def  btncleardisplay():
    global operator
    operator = " "
    text_Input.set(" ")
def  btnequals():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)

txtDisplay = Entry (f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=5,bg='powder blue',justify='right')
txtDisplay.grid(columnspan=4)
btn7=Button(f2,padx=15,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text='7',bg='powder blue',command=lambda:btnclick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'), text='8',bg='powder blue',command=lambda:btnclick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'), text='9',bg='powder blue',command=lambda:btnclick(9)).grid(row=2,column=2)
addition_btn=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold') ,text='+',bg='red',command=lambda:btnclick('+')).grid(row=2,column=3)
btn4=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='4',bg='powder blue',command=lambda:btnclick(4)).grid(row=3,column=0)
btn5=Button(f2,pady=16,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='5',bg='powder blue',command=lambda:btnclick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='6',bg='powder blue',command=lambda:btnclick(6)).grid(row=3,column=2)
subtract_btn=Button(f2,pady=16,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='-' ,bg='purple',command=lambda:btnclick('-') ).grid(row=3,column=3)
btn1=Button(f2,pady=16,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='1',bg='powder blue',command=lambda:btnclick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='2',bg='powder blue',command=lambda:btnclick(2)).grid(row=4,column=1)
btn3=Button(f2,pady=16,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='3',bg='powder blue',command=lambda:btnclick(3)).grid(row=4,column=2)
multiplication_btn=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='x',bg='green',command=lambda :btnclick('*')).grid(row=4,column=3)
btn0=Button(f2,pady=16,padx=16,bd=8,fg='black',font=('arial',20,'bold'),text='0',bg='powder blue',command=lambda :btnclick(0)).grid(row=5,column=0)
clear_btn=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='C',bg='powder blue',command=btncleardisplay).grid(row=5,column=1)
equal_btn=Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='=',bg='powder blue',command=btnequals).grid(row=5,column=2)
divide_btn=Button(f2,pady=16,padx=16,bd=16,fg='black',font=('arial',20,'bold'),text='/',bg='yellow',command=lambda:btnclick('/')).grid(row=5,column=3)
home.mainloop()