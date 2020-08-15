from tkinter import*
import tkinter.font as font
import math
from mpmath import*



root = Tk()

root.title("Calculator")

root.configure(bg="black")
e=Entry(root,width=60,borderwidth=15,bg="WHite",fg="BlAck")

e.grid(row=0,column=0,columnspan=4)
def button_add(number):
    
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)

def button_task():
    first_number= e.get()
    global f_num
    global math_num
    math_num="addition"
    f_num= float(first_number)
    e.delete(0,END)
def button_equal():
    second_number = e.get()
    j_num= float(second_number)
    e.delete(0,END)
    if math_num=="addition":
       e.insert(0, f_num + j_num ) 
    if math_num=="subtraction":
       e.insert(0, f_num - j_num )
    if math_num=="multiply":
       e.insert(0, f_num * j_num )
    if math_num=="divide":
       e.insert(0, f_num / j_num )
    if math_num=="square":
       e.insert(0, f_num*f_num - j_num*j_num)
    if math_num=="square2":
       e.insert(0, f_num*f_num + j_num*j_num + 2*f_num*j_num)
    if math_num=="root":
       e.insert(0, f_num**1/2)
    if math_num=="?":
        e.insert(0,f_num**j_num)
  
    
    
    
def button_subtract():
    first_number= e.get()
    global f_num
    global math_num
    math_num="subtraction"
    f_num= float(first_number)
    e.delete(0,END)
def button_multiply():
    first_number= e.get()
    global f_num
    global math_num
    math_num="multiply"
    f_num= float(first_number)
    e.delete(0,END)
    
def button_division():
    first_number= e.get()
    global f_num
    global math_num
    math_num="divide"
    f_num= float(first_number)
    e.delete(0,END)

def button_square():
    first_number= e.get()
    global f_num
    global math_num
    math_num="square"
    f_num= float(first_number)
    e.delete(0,END)
def button_square2():
    first_number= e.get()
    global f_num
    global math_num
    math_num="square2"
    f_num= float(first_number)
    e.delete(0,END)
def button_root():
    first_number= e.get()
    global f_num
    global math_num
    math_num="root"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="root":
       e.insert(0, math.sqrt(f_num))
def button_square3():
    first_number= e.get()
    global f_num
    global math_num
    math_num="square3"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="square3":
       e.insert(0, f_num**2)
def button_cuberoot():
    first_number= e.get()
    global f_num
    global math_num
    math_num="cube"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="cube":
       e.insert(0, f_num**3)
def button_sin():
    first_number= e.get()
    global f_num
    global math_num
    math_num="sin"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="sin":
       e.insert(0, math.sin(f_num))
def button_cos():
    first_number= e.get()
    global f_num
    global math_num
    math_num="cos"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="cos":
       e.insert(0, math.cos(f_num))
def button_tan():
    first_number= e.get()
    global f_num
    global math_num
    math_num="tan"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="tan":
       e.insert(0, math.tan(f_num))
def button_tandeg():
    first_number= e.get()
    global f_num
    global math_num
    math_num="tandeg"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="tandeg":
       e.insert(0, math.tan(f_num*math.pi/180))
def button_sindeg():
    first_number= e.get()
    global f_num
    global math_num
    math_num="sindeg"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="sindeg":
       e.insert(0, math.sin(f_num*math.pi/180))
def button_cosdeg():
    first_number= e.get()
    global f_num
    global math_num
    math_num="cosdeg"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="cosdeg":
       e.insert(0, math.cos(f_num*math.pi/180))
def button_rootcube():
    first_number= e.get()
    global f_num
    global math_num
    math_num="cuberoot"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="cuberoot":
       e.insert(0, f_num**(1/3))
def button_factorial():
    first_number= e.get()
    global f_num
    global math_num
    math_num="fact"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="fact":
       e.insert(0, math.factorial(f_num))

def button_sec():
    first_number= e.get()
    global f_num
    global math_num
    math_num="sec"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="sec":
       e.insert(0, sec(f_num))
def button_cosec():
    first_number= e.get()
    global f_num
    global math_num
    math_num="cosec"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="cosec":
       e.insert(0, csc(f_num))
def button_cot():
    first_number= e.get()
    global f_num
    global math_num
    math_num="cot"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="cot":
       e.insert(0, cot(f_num))
def button_cotdeg():
    first_number= e.get()
    global f_num
    global math_num
    math_num="cotdeg"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="cotdeg":
       e.insert(0, cot(f_num)*math.pi/180)
def button_cosecdeg():
    first_number= e.get()
    global f_num
    global math_num
    math_num="cosecdeg"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="cosecdeg":
       e.insert(0, csc(f_num) * math.pi/180)
def button_secdeg():
    first_number= e.get()
    global f_num
    global math_num
    math_num="secdeg"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="secdeg":
       e.insert(0, sec(f_num)*math.pi/180)
def button_reci():
    first_number= e.get()
    global f_num
    global math_num
    math_num="reci"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="reci":
       e.insert(0, 1/f_num)

def button_e():
    first_number= e.get()
    global f_num
    global math_num
    math_num="e"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="e":
       e.insert(0,f_num*2.71828)

def button_pi():
    first_number= e.get()
    global f_num
    global math_num
    math_num="pi"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="pi":
       e.insert(0,f_num*3.14159)

def button_square3():
    first_number= e.get()
    global f_num
    global math_num
    math_num="?"
    f_num= float(first_number)
    
    e.delete(0,END)
    
def button_log():
    first_number= e.get()
    global f_num
    global math_num
    math_num="log"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="log":
       e.insert(0,math.log(f_num))

def button_power():
    first_number= e.get()
    global f_num
    global math_num
    math_num="power"
    f_num= float(first_number)
    e.delete(0,END)
    if math_num=="power":
       e.insert(0,10**f_num)
    


    
myFont = font.Font(size=12)



button1=Button(root,text="1",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",command=lambda:button_add(1))
button2=Button(root,text="2",borderwidth=5,padx=48,pady=20,bg="Black",fg="White",command=lambda:button_add(2))
button3=Button(root,text="3",borderwidth=5,padx=54,pady=20,bg="Black",fg="White",command=lambda:button_add(3))
button4=Button(root,text="4",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",command=lambda:button_add(4))
button5=Button(root,text="5",borderwidth=5,padx=48,pady=20,bg="Black",fg="White",command=lambda:button_add(5))
button6=Button(root,text="6",borderwidth=5,padx=54,pady=20,bg="Black",fg="White",command=lambda:button_add(6))
button7=Button(root,text="7",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",command=lambda:button_add(7))
button8=Button(root,text="8",borderwidth=5,padx=48,pady=20,bg="Black",fg="White",command=lambda:button_add(8))
button9=Button(root,text="9",borderwidth=5,padx=54,pady=20,bg="Black",fg="White",command=lambda:button_add(9))
button0=Button(root,text="0",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",command=lambda:button_add(0))
buttonadd=Button(root,text="+",borderwidth=5,padx=45,pady=20,bg="Black",fg="White",command=button_task)
buttonequal=Button(root,text="=",borderwidth=5,padx=115,pady=20,bg="Black",fg="White",command=button_equal)
buttonclear= Button(root,text="Clear",borderwidth=5,padx=103,bg="Black",fg="White",pady=20,command=button_clear)

buttonsubtract=Button(root,text="-",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",command=button_subtract)
buttonmultiply=Button(root,text="×",borderwidth=5,padx=43,pady=20,bg="Black",fg="White",command=button_multiply)
buttondivision=Button(root,text="÷",borderwidth=5,padx=50,pady=20,bg="Black",fg="White",command=button_division)
buttonsquare=Button(root,text="a²-b²",borderwidth=5,padx=102,pady=20,bg="Black",fg="White",command=button_square)
buttonsquare2=Button(root,text="(a+b)²",borderwidth=5,padx=102,pady=20,bg="Black",fg="White",command=button_square2)
buttonroot=Button(root,text="Square Root",borderwidth=5,padx=30,pady=101,bg="Black",fg="White",command=button_root)
buttonsquare3=Button(root,text="Square ",borderwidth=5,padx=45,pady=102,bg="Black",fg="White",command=button_square3)
buttonrootcube=Button(root,text="x³",borderwidth=5,padx=112,pady=20,bg="Black",fg="White",command=button_cuberoot)
buttonsin=Button(root,text="Sin(rad)",borderwidth=5,padx=90,pady=20,bg="Black",fg="White",command=button_sin)
buttoncos=Button(root,text="Cos(rad)",borderwidth=5,padx=90,pady=20,bg="Black",fg="White",command=button_cos)
buttontan=Button(root,text="Tan(rad)",borderwidth=5,padx=90,pady=20,bg="Black",fg="White",command=button_tan)
buttontandeg=Button(root,text="Tan(deg)",borderwidth=5,padx=68,pady=20,bg="Black",fg="White",command=button_tandeg)
buttonsindeg=Button(root,text="Sin(deg)",borderwidth=5,padx=68,pady=20,bg="Black",fg="White",command=button_sindeg)
buttoncosdeg=Button(root,text="Cos(deg)",borderwidth=5,padx=65,pady=20,bg="Black",fg="White",command=button_cosdeg)
buttoncuberoot=Button(root,text="∛x " ,borderwidth=5,padx=90,pady=20,bg="black",fg="White",command=button_rootcube)
buttonfactorial=Button(root,text="x! " ,borderwidth=5,padx=90,pady=25,bg="black",fg="White",command=button_factorial)
buttonsec=Button(root,text="Sec(rad )" ,borderwidth=5,padx=65,pady=25,bg="black",fg="White",command=button_sec)
buttoncosec=Button(root,text="Cosec(rad) " ,borderwidth=5,padx=60,pady=25,bg="black",fg="White",command=button_cosec)
buttoncot=Button(root,text="Cot(rad) " ,borderwidth=5,padx=70,pady=25,bg="black",fg="White",command=button_cot)
buttoncotdeg=Button(root,text="Cot(deg) " ,borderwidth=5,padx=70,pady=25,bg="black",fg="White",command=button_cotdeg)
buttoncosecdeg=Button(root,text="Cosec(deg) " ,borderwidth=5,padx=100,pady=25,bg="black",fg="White",command=button_cosecdeg)
buttonsecdeg=Button(root,text="sec(deg) " ,borderwidth=5,padx=70,pady=25,bg="black",fg="White",command=button_secdeg)
buttonreciprocal=Button(root,text="1/x " ,borderwidth=5,padx=90,pady=25,bg="black",fg="White",command=button_reci)
buttone=Button(root,text="e" ,borderwidth=5,padx=90,pady=25,bg="black",fg="White",command=button_e)
buttonpi=Button(root,text="π" ,borderwidth=5,padx=90,pady=25,bg="black",fg="White",command=button_pi)
buttonhello=Button(root,text="xⁿ" ,borderwidth=5,padx=90,pady=25,bg="black",fg="White",command=button_square3)
buttonlog=Button(root,text="log" ,borderwidth=5,padx=90,pady=25,bg="black",fg="White",command=button_log)
buttonpower=Button(root,text="10ⁿ" ,borderwidth=5,padx=90,pady=25,bg="black",fg="White",command=button_power)
                                            

button1['font'] = myFont
button2['font'] = myFont
button3['font'] = myFont
button4['font'] = myFont
button5['font'] = myFont
button6['font'] = myFont
button7['font'] = myFont
button8['font'] = myFont
button9['font'] = myFont
button0['font'] = myFont
buttonadd['font'] = myFont
buttonsquare['font'] = myFont
buttonsquare2['font'] = myFont
buttonequal['font'] = myFont
buttonclear['font'] = myFont
buttonsubtract['font'] = myFont
buttonmultiply['font'] = myFont
buttondivision['font'] = myFont
buttonroot['font'] = myFont
buttonrootcube['font'] = myFont
buttonsquare3['font'] = myFont
e['font'] = myFont
buttonsin['font'] = myFont
buttoncos['font'] = myFont
buttontan['font'] = myFont
buttonfactorial['font'] = myFont
buttoncosec['font'] = myFont
buttonsec['font'] = myFont
buttoncot['font'] = myFont
buttonsindeg['font'] = myFont
buttoncosdeg['font'] = myFont
buttontandeg['font'] = myFont
buttoncuberoot['font'] = myFont
buttoncotdeg['font'] = myFont
buttoncosecdeg['font'] = myFont
buttonsecdeg['font'] = myFont
buttonreciprocal['font'] = myFont
buttone['font'] = myFont
buttonpi['font'] = myFont
buttonhello['font'] = myFont
buttonlog['font'] = myFont
buttonpower['font'] = myFont





button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonclear.grid(row=4,column=1,columnspan=2)

buttonadd.grid(row=5,column=0)
buttonequal.grid(row=5,column=1,columnspan=2)

buttonsubtract.grid(row=6,column=0)
buttonmultiply.grid(row=6,column=1)
buttondivision.grid(row=6,column=2)
buttonsquare.grid(row=7,column=0,columnspan=2)
buttonsquare2.grid(row=7,column=2,columnspan=2)
buttonroot.grid(row=1,column=3,rowspan=3)
buttonsquare3.grid(row=4,column=3,rowspan=3)
buttonrootcube.grid(row=9,column=2,columnspan=2)
buttonsin.grid(row=8,column=0,columnspan=2)
buttoncos.grid(row=8,column=2,columnspan=2)
buttontan.grid(row=9,column=0,columnspan=2)
buttontandeg.grid(row=3,column=4)
buttonsindeg.grid(row=3,column=5)
buttoncosdeg.grid(row=2,column=5)
buttoncuberoot.grid(row=2,column=4)
buttonfactorial.grid(row=0,column=4)
buttonsec.grid(row=0,column=5)
buttoncosec.grid(row=1,column=4)
buttoncot.grid(row=1,column=5)
buttoncotdeg.grid(row=4,column=5)
buttoncosecdeg.grid(row=5,column=4,columnspan=2)
buttonsecdeg.grid(row=4,column=4)
buttonreciprocal.grid(row=6,column=4)
buttone.grid(row=6,column=5)
buttonpi.grid(row=7,column=4)
buttonhello.grid(row=7,column=5)
buttonlog.grid(row=8,column=4)
buttonpower.grid(row=8,column=5)


root.mainloop()
