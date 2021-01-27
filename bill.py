from tkinter import *
import random  ,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Billing Software")
        bg_color = "peach puff"
        title = Label(self.root, text = "BusyBeans Cafe", bd=12,relief=GROOVE, bg=bg_color,fg="midnight blue",
                      font = ("Bradley Hand ITC", 38, "bold"),pady = 2).pack(fill = X)

#==================variables================================
        #========sandwich===========
        self.sandwich1 = IntVar()
        self.sandwich2 = IntVar()
        self.sandwich3 = IntVar()
        self.sandwich4 = IntVar()
        self.sandwich5 = IntVar()
        self.sandwich6 = IntVar()

        #========pizza===========
        self.pizza1 = IntVar()
        self.pizza2 = IntVar()
        self.pizza3 = IntVar()
        self.pizza4 = IntVar()
        self.pizza5 = IntVar()
        self.pizza6 = IntVar()

        #========beverages===========
        self.drink1 = IntVar()
        self.drink2 = IntVar()
        self.drink3 = IntVar()
        self.drink4 = IntVar()
        self.drink5 = IntVar()
        self.drink6 = IntVar()

#==================Total Product Price & Tax Variable================================       
        self.sandwich_price = StringVar()
        self.pizza_price = StringVar()
        self.drink_price = StringVar()

        self.sandwich_tax = StringVar()
        self.pizza_tax = StringVar()
        self.drink_tax = StringVar()

#====================Customer=============================
        self.c_name = StringVar()
        self.c_phon = StringVar()       
        self.bill_no = StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

#=================Customer Detail Frame======================
        F1 = LabelFrame(self.root,bd=10,relief = GROOVE, text= "CUSTOMER DETAILS", highlightbackground="black",highlightthickness=1,font=("times new roman",15,"bold"),fg="red",bg=bg_color)
        F1.place(x=0,y=80,relwidth = 1)

        cname_lbl = Label(F1,text="Customer Name",bg=bg_color,fg="black", font=("Comic Sans MS", 18, "bold")).grid(row=0, column = 0,padx=20,pady=5)
        cname_txt = Entry(F1,width = 15, textvariable = self.c_name, font = "arial 15",bd=7,relief = SUNKEN).grid(row = 0,column = 1,pady=5,padx=10)

        cphn_lbl = Label(F1,text="Customer Phone No.",bg=bg_color,fg="black", font=("Comic Sans MS", 18, "bold")).grid(row=0, column = 2,padx=20,pady=5)
        cphn_txt = Entry(F1,width = 15, textvariable =self.c_phon, font = "arial 15",bd=7,relief = SUNKEN).grid(row = 0,column = 3,pady=5,padx=10)

        cbill_lbl = Label(F1,text="Bill Number",bg=bg_color,fg="black", font=("Comic Sans MS", 18, "bold")).grid(row=0, column = 4 ,padx=20,pady=5)
        cbill_txt = Entry(F1,width = 15, textvariable =self.search_bill, font = "arial 15",bd=7,relief = SUNKEN).grid(row = 0,column = 5,pady=5,padx=10)

        bill_btn = Button(F1, text = "Search",command=self.find_bill,width = 10, bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

#==================Sandwich Frame===========================
        F2 = LabelFrame(self.root,bd=10,relief = GROOVE, text= "SANDWICH", highlightbackground="black",highlightthickness=1,font=("times new roman",15,"bold"),fg="red",bg=bg_color)
        F2.place(x=5,y=180,width = 355,height=380)

        s1_lbl = Label(F2,text="Veg. Sandwich",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=0,column=0,padx=5,pady=10,sticky="w")
        s1_txt = Entry(F2,width=6, textvariable =self.sandwich1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        s2_lbl = Label(F2,text="Toast Sandwich",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=1,column=0,padx=5,pady=10,sticky="w")
        s2_txt = Entry(F2,width=6, textvariable =self.sandwich2,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)

        s3_lbl = Label(F2,text="Cheese toast Sandwich",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=2,column=0,padx=5,pady=10,sticky="w")
        s3_txt = Entry(F2,width=6, textvariable =self.sandwich3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)

        s4_lbl = Label(F2,text="Mayonnaise cheese toast",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=3,column=0,padx=5,pady=10,sticky="w")
        s4_txt = Entry(F2,width=6, textvariable =self.sandwich4,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)

        s5_lbl = Label(F2,text="Veg. Paneer grill",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=4,column=0,padx=5,pady=10,sticky="w")
        s5_txt = Entry(F2,width=6, textvariable =self.sandwich5,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)

        s6_lbl = Label(F2,text="Shezwan grill sandwich",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=5,column=0,padx=5,pady=10,sticky="w")
        s6_txt = Entry(F2,width=6, textvariable =self.sandwich6,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=10)

#==================Pizza Frame===========================
        F3 = LabelFrame(self.root,bd=10,relief = GROOVE, text= "PIZZA", highlightbackground="black",highlightthickness=1,font=("times new roman",15,"bold"),fg="red",bg=bg_color)
        F3.place(x=365,y=180,width = 325,height=380)

        p1_lbl = Label(F3,text="Golden Corn",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=0,column=0,padx=5,pady=10,sticky="w")
        p1_txt = Entry(F3,width=7, textvariable =self.pizza1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        p2_lbl = Label(F3,text="Veg loaded",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=1,column=0,padx=5,pady=10,sticky="w")
        p2_txt = Entry(F3,width=7, textvariable =self.pizza2,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)

        p3_lbl = Label(F3,text="Paneer & Onion",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=2,column=0,padx=5,pady=10,sticky="w")
        p3_txt = Entry(F3,width=7, textvariable =self.pizza3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)

        p4_lbl = Label(F3,text="Deluxe Veggie",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=3,column=0,padx=5,pady=10,sticky="w")
        p4_txt = Entry(F3,width=7, textvariable =self.pizza4,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)

        p5_lbl = Label(F3,text="Mexican green wave",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=4,column=0,padx=5,pady=10,sticky="w")
        p5_txt = Entry(F3,width=7, textvariable =self.pizza5,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)

        p6_lbl = Label(F3,text="Paneer Makhani",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=5,column=0,padx=5,pady=10,sticky="w")
        p6_txt = Entry(F3,width=7, textvariable =self.pizza6,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=10)

#==================Beverages Frame===========================
        F4 = LabelFrame(self.root,bd=10,relief = GROOVE, text= "BEVERAGES", highlightbackground="black",highlightthickness=1,font=("times new roman",15,"bold"),fg="red",bg=bg_color)
        F4.place(x=695,y=180,width = 300,height=375)

        d1_lbl = Label(F4,text="Masala Tea",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        d1_txt = Entry(F4,width=7, textvariable =self.drink1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=30,pady=10)

        d2_lbl = Label(F4,text="Hot coffee",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        d2_txt = Entry(F4,width=7, textvariable =self.drink2,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=30,pady=10)

        d3_lbl = Label(F4,text="Cold coffee",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        d3_txt = Entry(F4,width=7, textvariable =self.drink3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=30,pady=10)

        d4_lbl = Label(F4,text="Oreo shake",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        d4_txt = Entry(F4,width=7, textvariable =self.drink4,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=30,pady=10)

        d5_lbl = Label(F4,text="Coca-cola",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        d5_txt = Entry(F4,width=7, textvariable =self.drink5,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=40,pady=10)

        d6_lbl = Label(F4,text="Sprite",font=("Comic Sans MS",14,"bold"),bg=bg_color,fg="brown4").grid(row=5,column=0,padx=10,pady=5,sticky="w")
        d6_txt = Entry(F4,width=7, textvariable =self.drink6,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=50,pady=10)

#========================Bill Area===================================
        F5 = Frame(self.root,bd=10,relief = GROOVE)
        F5.place(x=1000,y=180,width = 530,height=380)
        bill_title= Label(F5,text="Bill Area",font="arial 15 bold",highlightbackground="black",highlightthickness=1,bd=7,relief= GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5,orient = VERTICAL)
        self.textarea = Text(F5,yscrollcommand = scrol_y.set)
        scrol_y.pack(side=RIGHT, fill = Y)
        scrol_y.config( command = self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

#=========================Button Frame==================================

        F6 = LabelFrame(self.root,bd=10,relief = GROOVE, text= "BILL MENU", font=("times new roman",15,"bold"),highlightbackground="black",highlightthickness=1,fg="red",bg=bg_color)
        F6.place(x=0,y=560,relwidth = 1,height=235)
        m1_lbl = Label(F6, text="Total Sandwich Price",bg=bg_color,fg="black" ,font=("Comic Sans MS",16,"bold")).grid(row=0,column=0, padx=20, pady=10, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable =self.sandwich_price,font="arial 10 bold",bd=7,relief = SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        m2_lbl = Label(F6, text="Total Pizza Price",bg=bg_color,fg="black" ,font=("Comic Sans MS",16,"bold")).grid(row=1,column=0, padx=20, pady=10, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable =self.pizza_price,font="arial 10 bold",bd=7,relief = SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        m3_lbl = Label(F6, text="Total Beverages Price",bg=bg_color,fg="black" ,font=("Comic Sans MS",16,"bold")).grid(row=2,column=0, padx=20, pady=10, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable =self.drink_price,font="arial 10 bold",bd=7,relief = SUNKEN).grid(row=2,column=1,padx=10,pady=10)


        c1_lbl = Label(F6, text="Sandwich Tax",bg=bg_color,fg="black" ,font=("Comic Sans MS",16,"bold")).grid(row=0,column=2, padx=20, pady=10, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable =self.sandwich_tax,font="arial 10 bold",bd=7,relief = SUNKEN).grid(row=0,column=3,padx=10,pady=10)

        c2_lbl = Label(F6, text="Pizza Tax",bg=bg_color,fg="black" ,font=("Comic Sans MS",16,"bold")).grid(row=1,column=2, padx=20, pady=10, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable =self.pizza_tax,font="arial 10 bold",bd=7,relief = SUNKEN).grid(row=1,column=3,padx=10,pady=10)

        c3_lbl = Label(F6, text="Beverages Tax",bg=bg_color,fg="black" ,font=("Comic Sans MS",16,"bold")).grid(row=2,column=2, padx=20, pady=10, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable =self.drink_tax,font="arial 10 bold",bd=7,relief = SUNKEN).grid(row=2,column=3,padx=10,pady=10)

        btn_F = Frame(F6, bd=7,highlightbackground="black",highlightthickness=1, relief = GROOVE)
        btn_F.place(x=810,y=10,width=690, height=150)

        total_btn = Button(btn_F, command = self.total ,text="Total",bg="#081923",fg="white", pady=15 , width=12,bd=3, font="arial 15 bold").grid(row=0,column=0, padx=8, pady=25)
        GBill_btn = Button(btn_F, text="Generate Bill",command = self.bill_area,bg="#081923",fg="white", pady=15 , width=12,bd=3, font="arial 15 bold").grid(row=0,column=1, padx=5, pady=25)
        Clear_btn = Button(btn_F, text="Clear",command=self.clear,bg="#081923",fg="white", pady=15 , width=12,bd=3, font="arial 15 bold").grid(row=0,column=2, padx=5, pady=25)
        Exit_btn = Button(btn_F, text="Exit",command=self.Exit_app,bg="#081923",fg="white", pady=15 , width=12,bd=3, font="arial 15 bold").grid(row=0,column=3, padx=5, pady=25)
        self.welcome_bill()


    def total(self):
        self.s1_price = self.sandwich1.get()*30
        self.s2_price = self.sandwich2.get()*40
        self.s3_price = self.sandwich3.get()*50
        self.s4_price = self.sandwich4.get()*60
        self.s5_price = self.sandwich5.get()*90
        self.s6_price = self.sandwich6.get()*70
        self.total_sandwich_price = float(
                                        (self.s1_price)+
                                        (self.s2_price)+
                                        (self.s3_price)+
                                        (self.s4_price)+
                                        (self.s5_price)+
                                        (self.s6_price))

        self.sandwich_price.set("Rs. "+str(self.total_sandwich_price))
        self.s_tax = round((self.total_sandwich_price * 0.05),2)
        self.sandwich_tax.set("Rs. "+str(self.s_tax))


        self.p1_price = self.pizza1.get()*105
        self.p2_price = self.pizza2.get()*130
        self.p3_price = self.pizza3.get()*120
        self.p4_price = self.pizza4.get()*200
        self.p5_price = self.pizza5.get()*240
        self.p6_price = self.pizza6.get()*260
        self.total_pizza_price = float(
                                        (self.p1_price)+
                                        (self.p2_price)+
                                        (self.p3_price)+
                                        (self.p4_price)+
                                        (self.p5_price)+
                                        (self.p6_price))

        self.pizza_price.set("Rs. "+str(self.total_pizza_price))
        self.p_tax = round((self.total_pizza_price * 0.1),2)
        self.pizza_tax.set("Rs. "+str(self.p_tax))

        self.d1_price = self.drink1.get()*20
        self.d2_price = self.drink2.get()*70
        self.d3_price = self.drink3.get()*90
        self.d4_price = self.drink4.get()*100
        self.d5_price = self.drink5.get()*40
        self.d6_price = self.drink6.get()*45
        self.total_drink_price = float(
                                        (self.d1_price)+
                                        (self.d2_price)+
                                        (self.d3_price)+
                                        (self.d4_price)+
                                        (self.d5_price)+
                                        (self.d6_price))

        self.drink_price.set("Rs. "+ str(self.total_drink_price))
        self.d_tax = round((self.total_drink_price * 0.05),2)
        self.drink_tax.set("Rs. "+str(self.d_tax))

        self.Total_bill = float(self.total_sandwich_price +
                                self.total_pizza_price +
                                self.total_drink_price +
                                self.s_tax +
                                self.p_tax +
                                self.d_tax)

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t\t Welcome Webcode Retail\n")
        self.textarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.textarea.insert(END,f"\n=============================================================")
        self.textarea.insert(END,f"\n Products\t\t\t      QTY\t\t\t    Price")
        self.textarea.insert(END,f"\n=============================================================")
        

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are must!")
        elif self.sandwich_price.get() == "Rs. 0.0" and self.pizza_price.get() == "Rs. 0.0" and self.drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error","No Product Purchased!")        
        else:
            self.welcome_bill()
            #========sandwich========
            if self.sandwich1.get() != 0:
                self.textarea.insert(END,f"\n Veg. Sandwich\t\t\t       {self.sandwich1.get()}\t\t\t     {self.s1_price}")
            if self.sandwich2.get() != 0:
                self.textarea.insert(END,f"\n Toast Sandwich\t\t\t       {self.sandwich2.get()}\t\t\t     {self.s2_price}")
            if self.sandwich3.get() != 0:
                self.textarea.insert(END,f"\n Cheese toast Sandwich\t\t\t      {self.sandwich3.get()}\t\t\t     {self.s3_price}")
            if self.sandwich4.get() != 0:
                self.textarea.insert(END,f"\n Mayonnaise cheese toast\t\t\t    {self.sandwich4.get()}\t\t\t     {self.s4_price}")
            if self.sandwich5.get() != 0:
                self.textarea.insert(END,f"\n Veg. Paneer grill\t\t\t       {self.sandwich5.get()}\t\t\t     {self.s5_price}")
            if self.sandwich6.get() != 0:
                self.textarea.insert(END,f"\n Shezwan grill Sandwich\t\t\t     {self.sandwich6.get()}\t\t\t     {self.s6_price}")

            #========pizza========
            if self.pizza1.get() != 0:
                self.textarea.insert(END,f"\n Golden Corn\t\t\t       {self.pizza1.get()}\t\t\t     {self.p1_price}")
            if self.pizza2.get() != 0:
                self.textarea.insert(END,f"\n Veg Loaded pizza\t\t\t       {self.pizza2.get()}\t\t\t     {self.p2_price}")
            if self.pizza3.get() != 0:
                self.textarea.insert(END,f"\n Paneer & Onion pizza\t\t\t       {self.pizza3.get()}\t\t\t     {self.p3_price}")
            if self.pizza4.get() != 0:
                self.textarea.insert(END,f"\n Deluxe Veggie pizza\t\t\t       {self.pizza4.get()}\t\t\t     {self.p4_price}")
            if self.pizza5.get() != 0:
                self.textarea.insert(END,f"\n Mexican green wave\t\t\t       {self.pizza5.get()}\t\t\t     {self.p5_price}")
            if self.pizza6.get() != 0:
                self.textarea.insert(END,f"\n Paneer Makhani\t\t\t       {self.pizza6.get()}\t\t\t     {self.p6_price}")

            #========beverages========
            if self.drink1.get() != 0:
                self.textarea.insert(END,f"\n Masala Tea\t\t\t       {self.drink1.get()}\t\t\t     {self.d1_price}")
            if self.drink2.get() != 0:
                self.textarea.insert(END,f"\n Hot coffee\t\t\t       {self.drink2.get()}\t\t\t     {self.d2_price}")
            if self.drink3.get() != 0:
                self.textarea.insert(END,f"\n Cold coffee\t\t\t       {self.drink3.get()}\t\t\t     {self.d3_price}")
            if self.drink4.get() != 0:
                self.textarea.insert(END,f"\n Oreo Shake\t\t\t       {self.drink4.get()}\t\t\t     {self.d4_price}")
            if self.drink5.get() != 0:
                self.textarea.insert(END,f"\n Coca-cola\t\t\t       {self.drink5.get()}\t\t\t     {self.d5_price}")
            if self.drink6.get() != 0:
                self.textarea.insert(END,f"\n Sprite\t\t\t       {self.drink6.get()}\t\t\t     {self.d6_price}")

            self.textarea.insert(END,f"\n-------------------------------------------------------------")
            if self.sandwich_tax.get() != "Rs. 0.0":
                self.textarea.insert(END,f"\n Sandwich Tax\t\t\t\t\t\t {self.sandwich_tax.get()}")
            if self.pizza_tax.get() != "Rs. 0.0":
                self.textarea.insert(END,f"\n Pizza Tax\t\t\t\t\t\t {self.pizza_tax.get()}")
            if self.drink_tax.get() != "Rs. 0.0":
                self.textarea.insert(END,f"\n Beverages Tax\t\t\t\t\t\t {self.drink_tax.get()}")
            self.textarea.insert(END,f"\n-------------------------------------------------------------")
            self.textarea.insert(END,f"\n Total Bill : \t\t\t\t\t\t Rs. {self.Total_bill}")
            self.textarea.insert(END,f"\n-------------------------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Sava Bill","Do you want to save the Bill ?")
        if op>0:
            self.bill_data = self.textarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+ ".txt",'w')
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved Successfully!")
        else :
            return

    def find_bill(self):
        present = 'no'
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1=open(f"bills/{i}",'r')
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present = 'yes'
        if present == 'no':
            messagebox.showerror("Error",'Invalid Bill Number!')

    def clear(self):
        op = messagebox.askyesno("Clear","Do you really want to Clear ?")
        if op>0:
            #========sandwich===========
            self.sandwich1.set(0)
            self.sandwich2.set(0)
            self.sandwich3.set(0)
            self.sandwich4.set(0)
            self.sandwich5.set(0)
            self.sandwich6.set(0)

            #========pizza===========
            self.pizza1.set(0)
            self.pizza2.set(0)
            self.pizza3.set(0)
            self.pizza4.set(0)
            self.pizza5.set(0)
            self.pizza6.set(0)

            #========beverages===========
            self.drink1.set(0)
            self.drink2.set(0)
            self.drink3.set(0)
            self.drink4.set(0)
            self.drink5.set(0)
            self.drink6.set(0)

    #==================Total Product Price & Tax Variable================================       
            self.sandwich_price.set("")
            self.pizza_price.set("")
            self.drink_price.set("")

            self.sandwich_tax.set("")
            self.pizza_tax.set("")
            self.drink_tax.set("")

    #====================Customer=============================
            self.c_name.set("")
            self.c_phon.set("")       
            self.bill_no.set("")
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op = messagebox.askyesno("Exit","Do you really want to exit ?")
        if op>0:
            self.root.destroy()



#=======5min


root = Tk()
obj= Bill_App(root)
root.mainloop()
