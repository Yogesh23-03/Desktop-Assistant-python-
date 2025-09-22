from tkinter import *
import speech_to_text
import action
def ask():
    user_v=speech_to_text.speech_to_text()
    bot_val=action.Action(user_v)
    text.insert(END,'User---->'+user_v+'\n')
    if bot_val!=None:
        text.insert(END,'Bot<--'+str(bot_val)+'\n')
    if bot_val=='ok sir':
        root.destroy()


def send():
    send=entry.get()
    bot_val=action.Action(send)
    text.insert(END,'User---->'+send+'\n')
    if bot_val!=None:
        text.insert(END,'Bot<--'+str(bot_val)+'\n')
    if bot_val=='ok sir':
        root.destroy()
        



def delete():
    text.delete(1.0,END)
    
    





root=Tk()
root.title("I'M YOUR ASSISTENT")
root.geometry('550x675')
root.resizable(False,False)
root.config(bg="#2f4f4f")
frame=LabelFrame(root,padx=100,pady=7,borderwidth=3,relief='raised')
frame.grid(row=0,column=1,padx=55,pady=10)
text=Label(frame,text=" i'm Merlin",font=('conic Sans ms',14,'bold'),bg='#324345')
text.grid(row=0,column=0,padx=20,pady=10)
from PIL import Image,ImageTk
img=ImageTk.PhotoImage(Image.open('VIDEO DIRECTORIES/assist.jpg'))
img_label=Label(frame,image=img)
img_label.grid(row=1,column=0,pady=20)
frame.config(bg='#2f4f4f')
text=Text(root ,font=('courier 10 bold'),bg='#324345' )
text.grid(row=2,column=0)
text.place(x=100,y=375,width=375,height=100)
entry=Entry(root,justify=CENTER)
entry.place(x=100,y=500,width=375,height=30)
Button1=Button(root,text='ASK',bg='#324345',padx=40,pady=16,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=70,y=575)

Button2=Button(root,text='SEND',bg='#324345',padx=40,pady=16,borderwidth=3,relief=SOLID,command=send)
Button2.place(x=400,y=575)

Button3=Button(root,text='DELETE',bg='#324345',padx=40,pady=16,borderwidth=3,relief=SOLID,command=delete)
Button3.place(x=225,y=575)
root.mainloop()