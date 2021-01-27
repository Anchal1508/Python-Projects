from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import pymysql
import re

class Register:
    def __init__(self,root):
        self.root= root
        self.root.title('Registeration Window')
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")

        #=========Bg Image========
        self.bg=ImageTk.PhotoImage(file="img/cafe img11.jpg")
        bg = Label(self.root, image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)    
        title_lbl = Label(self.root, text = "BusyBeans Cafe", bd=6,relief=SUNKEN, fg="#3d1400",bg="white",
                      font = ("Bradley Hand ITC", 42, "bold"),pady = 2).pack(fill = X)
        self.logo=ImageTk.PhotoImage(file="img/logo.jpg")
        logo = Label(self.root, image=self.logo, bd=6,relief=FLAT).place(x=400,y=7,width=118,height=78)

        #title_lbl=Label(self.root,text="BusyBeans Cafe",font = ("Bradley Hand ITC", 30, "bold"),bg="#081923",fg="white").place(x=450,y=20,width=500)

        
        #=========left Image========
        self.left=ImageTk.PhotoImage(file="img/try1.jpg")
        left = Label(self.root, image=self.left).place(x=80,y=100)

        #=========Register Frame======
        frame1=Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=573)

        title= Label(frame1, text="REGISTER HERE", font=("times new roman",20,"bold"),bg="white", fg="green").place(x=50,y=30)

        #-----------------Row 1
        f_name= Label(frame1, text="First Name", font=("times new roman",16,"bold"),bg="white", fg="saddle brown").place(x=50,y=100)
        self.txt_fname= Entry(frame1, font=("Comic sans MS",15),bg="papaya whip")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name= Label(frame1, text="Last Name", font=("times new roman",16,"bold"),bg="white", fg="saddle brown").place(x=370,y=100)
        self.txt_lname= Entry(frame1, font=("Comic sans MS",15),bg="papaya whip")
        self.txt_lname.place(x=370,y=130,width=250)


        #-----------------Row 2
        contact= Label(frame1, text="Contact", font=("times new roman",16,"bold"),bg="white", fg="saddle brown").place(x=50,y=180)
        self.txt_contact= Entry(frame1, font=("Comic sans MS",15),bg="papaya whip")
        self.txt_contact.place(x=50,y=210,width=250)

        email= Label(frame1, text="Email", font=("times new roman",16,"bold"),bg="white", fg="saddle brown").place(x=370,y=180)
        self.txt_email= Entry(frame1, font=("Comic sans MS",15),bg="papaya whip")
        self.txt_email.place(x=370,y=210,width=250)

        #-------------------Row 3
        question= Label(frame1, text="Security Question", font=("times new roman",16,"bold"),bg="white", fg="saddle brown").place(x=50,y=260)
        self.cmb_quest= ttk.Combobox(frame1, font=("times new roman",13),state='readonly', justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your School Name","Your Mother Name","Your Favourite Song") 
        self.cmb_quest.place(x=50,y=290,width=250)
        self.cmb_quest.current(0)

        answer= Label(frame1, text="Answer", font=("times new roman",16,"bold"),bg="white", fg="saddle brown").place(x=370,y=260)
        self.txt_answer= Entry(frame1, font=("Comic sans MS",15),bg="papaya whip")
        self.txt_answer.place(x=370,y=290,width=250)

        #-------------------Row 4
        password= Label(frame1, text="Password",font=("times new roman",16,"bold"),bg="white", fg="saddle brown").place(x=50,y=340)
        self.txt_password= Entry(frame1,show='*', font=("Comic sans MS",15),bg="papaya whip")
        self.txt_password.place(x=50,y=370,width=250)

        cpassword= Label(frame1, text="Confirm Password", font=("times new roman",16,"bold"),bg="white", fg="saddle brown").place(x=370,y=340)
        self.txt_cpassword= Entry(frame1,show='*', font=("Comic sans MS",15),bg="papaya whip")
        self.txt_cpassword.place(x=370,y=370,width=250)

        #--------------------Thanks
        thanku = Label(frame1, text="Thank you for registration !", font=("times new roman", 13,"bold"), bg="white", fg="black").place(x=50,y=420)
        #------------------- Row 5
        self.btn_img = ImageTk.PhotoImage(file="img/register12.jpg")
        btn_register=Button(frame1, image=self.btn_img, bd=0, cursor="hand2",command=self.register_data).place(x=50, y=450)
        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",20), bd=4, cursor="hand2").place(x=200, y=580, width=180)

    def login_window(self):
        self.root.destroy()
        import login

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
    
    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_email.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required!", parent=self.root)
        elif len(self.txt_contact.get()) < 10:
            messagebox.showerror("Error","Please enter correct phone number!", parent=self.root)
        elif not re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", self.txt_email.get()):
            messagebox.showerror("Error","Please enter correct Email ID!", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password must be same!", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost", user="root",password="", database="cafe")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s;",self.txt_email.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another email")
                else:
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s);",
                                (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_quest.get(),
                                self.txt_answer.get(),
                                self.txt_password.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registered successfully!", parent=self.root)
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{(es)}", parent=self.root)
            




root = Tk()
obj = Register(root)
root.mainloop()