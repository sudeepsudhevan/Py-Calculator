from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry('570x600')
window.resizable(False, False)
window.configure(bg="#1a1a1a")

equal = ""


def clear():
    global equal
    equal = ""
    display.config(text=equal)

def click(number):
    global equal
    equal=equal+str(number)
    display.config(text=equal)

def calculate():
    global equal
    result=""
    if equal !="":
        try:
            result = str(eval(equal))
        except:
           result="error"
           equal=""
    display.config(text=result)







display = Label(window, width=25, height=2, text="", font=("arial", 30))
display.pack()

butC = Button(window, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda:clear())
butC.place(x=10,y=100)

butDiv=Button(window, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click('/'))
butDiv.place(x=150,y=100)

butp=Button(window, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click('%'))
butp.place(x=290,y=100)

butMul=Button(window, text="x", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click('*'))
butMul.place(x=430, y=100)


but7=Button(window, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click(7))
but7.place(x=10,y=200)

but8=Button(window, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click(8))
but8.place(x=150,y=200)

but9=Button(window, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click(9))
but9.place(x=290,y=200)

butMinus=Button(window, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click('-'))
butMinus.place(x=430,y=200)


but4=Button(window, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click(4))
but4.place(x=10,y=300)

but5=Button(window, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click(5))
but5.place(x=150,y=300)

but6=Button(window, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click(6))
but6.place(x=290,y=300)

butPlus=Button(window, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click('+'))
butPlus.place(x=430,y=300)


but1=Button(window, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click(1))
but1.place(x=10,y=400)

but2=Button(window, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click(2))
but2.place(x=150,y=400)

but3=Button(window, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click(3))
but3.place(x=290,y=400)

butEqual=Button(window, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=3, fg="#fff", bg="#fe9037",command=lambda :calculate())
butEqual.place(x=430,y=400)


butDot=Button(window, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click('.'))
butDot.place(x=10,y=500)

but0=Button(window, text="0", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click(0))
but0.place(x=150,y=500)

butComma=Button(window, text=",", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#404040",command=lambda : click(','))
butComma.place(x=290,y=500)


window.mainloop()
