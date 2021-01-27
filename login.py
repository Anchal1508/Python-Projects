from tkinter import*
from PIL import Image,ImageTk, ImageDraw
from datetime import *
import time
from math import*
import pymysql
from tkinter import messagebox, ttk
class login_window:
    def __init__(self, root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="#021e2f")
        
        ##========Background color========
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=700)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=700,y=0,relheight=1,relwidth=1)

        #========Login Frame==================
        login_frame=Frame(self.root, bg="white")
        login_frame.place(x=250,y=160,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE", font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
     
        email=Label(login_frame,text="EMAIL ADDRESS", font=("times new roman",18,"bold"),bg="white",fg="saddle brown").place(x=250,y=150)
        self.txt_email=Entry(login_frame, font=("comic sans MS",15),bg="papaya whip")
        self.txt_email.place(x=250,y=185,width=350,height=35)
        
        pass_=Label(login_frame,text="PASSWORD", font=("times new roman",18,"bold"),bg="white",fg="saddle brown").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame,show='*', font=("comic sans MS",15),bg="papaya whip")
        self.txt_pass_.place(x=250,y=285,width=350,height=35)
        
        btn_reg=Button(login_frame,text="Register new Account?",command=self.register_window,font=("times new roman",14),bg="white",bd=0,fg="#B00857",cursor="hand2").place(x=250,y=325)
        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_password_window,font=("times new roman",14),bg="white",bd=0,fg="red",cursor="hand2").place(x=450,y=325)

        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=250,y=385,width=180,height=40)


        #========Clock=====================
        self.lbl=Label(self.root,text="\n\nIt's Cafe Time",font=("Book Antiqua",25,"bold"),compound=BOTTOM,bg="#081923",bd=0,fg="white")
        self.lbl.place(x=90,y=180,height=450,width=350)
        self.working()

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)

    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="cafe")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and answer=%s;",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Please Enter Correct Security Question / Answer to reset your password!",parent=self.root2) 
                else:
                    cur.execute("update employee set password=%s where email=%s;",(self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password has been reset! Please login with new Password.",parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as es: 
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)
                
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="cafe")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s;",self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Please enter the valid email address to reset your password!",parent=self.root) 
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+470+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

                    #-------------------Forget Password
                    question= Label(self.root2, text="Security Question", font=("times new roman",16,"bold"),bg="white", fg="saddle brown").place(x=50,y=100)
                    self.cmb_quest= ttk.Combobox(self.root2, font=("times new roman",13),state='readonly', justify=CENTER)
                    self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your School Name","Your Mother Name","Your Favourite Song") 
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)

                    answer= Label(self.root2, text="Answer", font=("times new roman",16,"bold"),bg="white", fg="saddle brown").place(x=50,y=180)
                    self.txt_answer= Entry(self.root2, font=("Comic sans MS",15),bg="papaya whip")
                    self.txt_answer.place(x=50,y=210,width=250)

                    new_password= Label(self.root2, text="New Password", font=("times new roman",16,"bold"),bg="white", fg="saddle brown").place(x=50,y=260)
                    self.txt_new_pass= Entry(self.root2, font=("Comic sans MS",15),bg="papaya whip")
                    self.txt_new_pass.place(x=50,y=290,width=250)

                    btn_change_password=Button(self.root2,command=self.forget_password,text="Reset Password",bg="#031F3C",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)

            

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All the fields are required!",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="cafe")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s;",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root) 
                else:
                    messagebox.showinfo("Success","Welcome!",parent=self.root)
                    self.root.destroy()
                    import bill
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)




    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #===========For Clock Image
        bg=Image.open("img/c.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        # Formula To Rotate the clock
        # angle_in_radians = angle_in_degree * math.pi / 180
        # line_length = 100
        # center_x = 250
        # center_y = 250
        # end_x = center_x + line_length * math.cos(angle_in_radians)
        # end_y = center_y - line_length * math.sin(angle_in_radians)
        
        #===========Hour Line Image
        origin = 200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        clock.save("img/clock_new.png")
        #===========Min Line Image
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        clock.save("img/clock_new.png")
        #===========Second Line Image
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="white")
        clock.save("img/clock_new.png")

    def working(self):
        h=datetime.now().time().hour 
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
       
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="img/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)


root=Tk()
obj=login_window(root)
root.mainloop()