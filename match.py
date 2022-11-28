import platform
from tkinter import*
import math
import time

def ButtonPressMAR():
	ButtonPressMAR.counter +=1 
	print( ButtonPressMAR.counter)
	Result=Label(match,bd='13',text=str(ButtonPressMAR.counter))
	Result.place(x=120,y=200)
ButtonPressMAR.counter =0

def ButtonPressCRO():
	ButtonPressCRO.counter +=1 
	print( ButtonPressCRO.counter)
	Result=Label(match,bd='13',text=str(ButtonPressCRO.counter))
	Result.place(x=280,y=200)
ButtonPressCRO.counter =0



def clock():
	hour=time.strftime("%H")
	minute=time.strftime("%M")
	second=time.strftime("%S")
	
	timer.config(text=hour + ":" + minute + ":" + second)
	match.after(1000,clock)
	
# def update():
	# timer.config(text="New")
	
	

match=Tk()

match.title("Hello from tkinter ")	
match.geometry('500x300')

photo1=PhotoImage(file='mar.png')
photo1 = photo1.subsample(2,2)

photo2=PhotoImage(file='croo.png')
photo2= photo2.subsample(2,2)

timer=Button(match,text="Start the Mtach :",bd='3',command=clock)
timer.place(x=20,y=15)


MARph=Label(match,text="MaR",bd='5',image=photo1)
MARph.place(x=50,y=50)

CROph=Label(match,text="CRO",bd='5',image=photo2)
CROph.place(x=200,y=50)

MAR=Button(match,text="G",bd='10',background='red',command=ButtonPressMAR)
MAR.place(x=80,y=200)

CRO=Button(match,text="G",bd='10',background='red',command=ButtonPressCRO)
CRO.place(x=240,y=200)





match.mainloop()