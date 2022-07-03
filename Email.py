from tkinter import *
from tkinter import messagebox
import random
import smtplib
from email.message import EmailMessage
root=Tk()
root.title("SMART ALERT SYSTEM")
root.geometry('1440x1280')
bg_color='#088aff'

#======================variable=================
c_name=StringVar()
c_phone=StringVar()
item=StringVar()
Rate=IntVar()
quantity=IntVar()
bill_no=StringVar()
x= random.randint(10000,99999)
bill_no.set(str(x))

global l
l=[]

#=========================Functions================================


def email_alert(subject, body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    user = "alertsystemsos@gmail.com"
    msg['from'] = user
    password = "xbgucelsmrdsccmz"
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    
    server.quit()




def gbill():
 
    if  c_phone.get() == "8971504592":
        textAreaText = textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END, textAreaText)
        textarea.insert(END, f"\n======================================")
        textarea.insert(END, f"\nTotal Fine Amount :\t\t      {sum(l)}")
        textarea.insert(END, f"\n\n======================================")
        save_bill()
        
    else:
       messagebox.showerror("Error", "Number not found")



def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set(0)
    quantity.set(0)
    welcome()
    
def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()
        
def save_bill():
    op=messagebox.askyesno("Send The Receipt","Do you want to send the Challan?")
    email_alert("Alert", "Over Speeding Alert!", "asp2work@gmail.com")
  
        
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t  Smart Alert System")
    textarea.insert(END,f"\n\nChallan Number:\t\t{bill_no.get()}")
    textarea.insert(END,f"\nPhone Number:\t\t{c_phone.get()}")
    textarea.insert(END,f"\n\n====================================================")
    textarea.insert(END,"\nOverspeeding\t\t\t\t\tRs1000")
    textarea.insert(END,f"\n====================================================\n")
    textarea.configure(font='arial 15 bold')



title=Label(root,pady=2,text="Challan Software",bd=12,bg=bg_color,fg='white',font=('times new roman', 30 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)

#=================Product Frames=================
F1=LabelFrame(root,bd=10,relief=GROOVE,text='Customer Details',font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
F1.place(x=0,y=50,relwidth=1)


cphone_lbl=Label(F1,text='Phone No. ',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

F2 = LabelFrame(root, text='Overspeeding', font=('times new romon', 18, 'bold'), fg='gold',bg=bg_color)
F2.place(x=5, y=180,width=500,height=500)



rate= Label(F2, text='Rs 1000', font=('times new romon',18, 'bold'), bg=bg_color, fg='black').grid(
row=1, column=0, padx=30, pady=20)



#========================Bill area================
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=430,y=180,width=500,height=500)

bill_title=Label(F3,text='Challan',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()

F4 = LabelFrame(root, text='Message', font=('times new romon', 18, 'bold'), fg='black',bg='white')
F4.place(x=930, y=180,width=500,height=500)


welcome()
#=========================Buttons======================

btn2=Button(F2,text='Send',font='arial 15 bold',command=gbill,padx=10,pady=10,bg='red',width=15)
btn2.grid(row=5,column=0,padx=10,pady=30)
btn3=Button(F2,text='Clear',font='arial 15 bold',padx=3,pady=10,command=clear,bg='lime',width=15)
btn3.grid(row=6,column=0,padx=10,pady=30)


root.mainloop()