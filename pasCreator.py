import random
import math
from tkinter import *
from tkinter import ttk

tk = Tk()
frm = ttk.Frame(tk, padding=100)
tk.title('Генератор Паролів')
tk.geometry('300x150')
tk.resizable(width=0, height=0)
def creator():
  numPassword =0
  numpassword =password = ''
  word ="qwertyuiopasdfghjklzxcvbnm"
  wordArr = "".join(word)
  rand2=rand3=rand4=serialNum=ss=rand_1= 0
  rand_1 = random.randint(0,3)
  firstWord =str(random.choice(wordArr)).upper()+(random.choice(wordArr)).upper()
  lastWord = str(random.choice(wordArr)).upper()+(random.choice(wordArr)).upper()
  serialNum= str((random.randint(0,9)))+str((random.randint(0,9)))

  while rand3<4:
    firstNum = random.randint(0,512)
    firstNum = int(firstNum) 
    randWord = random.choice(wordArr)
    rand4=random.randint(0,3)
    if rand4>2:
         randWord= randWord.upper() 
    numPassword=numPassword+firstNum
    numpassword = str(numPassword)
    passBit = numpassword+randWord
    password=password+passBit
    rand3 =rand3+1
  password=firstWord+serialNum+password+serialNum+lastWord
  print(password)
  def copy():
     tk.clipboard_clear()
     tk.clipboard_append(password)
  ttk.Label(text=password).place(x=70, y=10)
  tk.clipboard_clear()
  btn1 = Button(tk,text="Copy" ,command=copy).place(x=230, y=100) 
  return password  
btn = Button(tk,text="Generate" ,height=2, width=10,command=creator).place(x=110, y=50)


   

tk.mainloop()
 

 
#tk.update()
#word ="q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m"
#word ="q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m"

