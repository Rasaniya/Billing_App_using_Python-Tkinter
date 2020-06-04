from tkinter import*
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root

        #===============HEADING===================>>
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        heading=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        

                                #===============ALL VARIABLES================>>

        #===============COSMETIC VARIABLES==========>
        self.soap=IntVar()
        self.facecream=IntVar()
        self.facewash=IntVar()
        self.deodrant=IntVar()
        self.hairgel=IntVar()
        self.bodylotion=IntVar()

        #================GROCERY VARIABLES==========>>
        self.rice=IntVar()
        self.wheat=IntVar()
        self.foodoil=IntVar()
        self.bread=IntVar()
        self.milk=IntVar()
        self.sugar=IntVar()

        #================COLD DRINKS VARIABLES==========>>
        self.maza=IntVar()
        self.dew=IntVar()
        self.frooti=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        self.thumbsup=IntVar()

        #================Total PRODUCT PRICE & TAX VARIABLES==========>>
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
        
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #================CUSTOMER VARIABLES==========>>
        self.customer_name=StringVar()
        self.customer_phone_no=StringVar()
        self.customer_bill_no=StringVar()
        
        self.customer_bill_no=StringVar()
        x=random.randint(1000,9999)
        self.customer_bill_no.set(str(x))

        self.search_bill_no=StringVar()


        #====================CUSTOMER FRAME=======================>>
        frame_1=LabelFrame(self.root,bd=10,relief=GROOVE,text="CUSTOMER DETAILS",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        frame_1.place(x=0,y=80,relwidth=1)

        Customer_Name_Label=Label(frame_1,text="Customer Name",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,padx=20,pady=5)
        Customer_Name_text=Entry(frame_1,width=15,textvariable=self.customer_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        Customer_PhoneNo_Label=Label(frame_1,text="Phone No.",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=2,padx=20,pady=5)
        Customer_PhoneNo_text=Entry(frame_1,width=15,textvariable=self.customer_phone_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        Customer_BillNo_Label=Label(frame_1,text="Bill Number",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=4,padx=20,pady=5)
        Customer_BillNo_text=Entry(frame_1,width=15,textvariable=self.search_bill_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)                                 
       
        Search_Button=Button(frame_1,text="Search",command=self.search_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)



        #===============COSMETICS FRAME====================>>
        frame_2=LabelFrame(self.root,bd=10,relief=GROOVE,text="COSMETICS",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        frame_2.place(x=5,y=200,width=500,height=430)

        Item1_Label=Label(frame_2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Item1_text=Entry(frame_2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Item2_Label=Label(frame_2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Item2_text=Entry(frame_2,width=10,textvariable=self.facecream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Item3_Label=Label(frame_2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Item3_text=Entry(frame_2,width=10,textvariable=self.facewash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Item4_Label=Label(frame_2,text="Deodrant",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Item4_text=Entry(frame_2,width=10,textvariable=self.deodrant,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Item5_Label=Label(frame_2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Item5_text=Entry(frame_2,width=10,textvariable=self.hairgel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        Item6_Label=Label(frame_2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Item6_text=Entry(frame_2,width=10,textvariable=self.bodylotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #===============GROCERY FRAME====================>>
        frame_3=LabelFrame(self.root,bd=10,relief=GROOVE,text="GROCERY",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        frame_3.place(x=400,y=200,width=500,height=430)

        Item1_Label=Label(frame_3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Item1_text=Entry(frame_3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Item2_Label=Label(frame_3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Item2_text=Entry(frame_3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Item3_Label=Label(frame_3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Item3_text=Entry(frame_3,width=10,textvariable=self.foodoil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Item4_Label=Label(frame_3,text="Bread",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Item4_text=Entry(frame_3,width=10,textvariable=self.bread,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Item5_Label=Label(frame_3,text="Milk",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Item5_text=Entry(frame_3,width=10,textvariable=self.milk,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        Item6_Label=Label(frame_3,text="sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Item6_text=Entry(frame_3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



        #===============COLD DRINKS FRAME====================>>
        frame_4=LabelFrame(self.root,bd=10,relief=GROOVE,text="COLD DRINKS",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        frame_4.place(x=750,y=200,width=500,height=430)

        Item1_Label=Label(frame_4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Item1_text=Entry(frame_4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Item2_Label=Label(frame_4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Item2_text=Entry(frame_4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Item3_Label=Label(frame_4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Item3_text=Entry(frame_4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Item4_Label=Label(frame_4,text="Dew",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Item4_text=Entry(frame_4,width=10,textvariable=self.dew,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Item5_Label=Label(frame_4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Item5_text=Entry(frame_4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        Item6_Label=Label(frame_4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Item6_text=Entry(frame_4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



        #=================BILL AREA==============>>
        frame_5=Frame(self.root,bd=10,relief=GROOVE)
        frame_5.place(x=1150,y=200,width=450,height=430)
        Bill_title=Label(frame_5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        Scroll_Vertical=Scrollbar(frame_5,orient=VERTICAL)
        self.txtarea=Text(frame_5,yscrollcommand=Scroll_Vertical.set)
        Scroll_Vertical.pack(side=RIGHT,fill=Y)
        Scroll_Vertical.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        
        #=================BILL MENU FRAME====================>>
        frame_6=LabelFrame(self.root,bd=10,relief=GROOVE,text="BILL MENU",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        frame_6.place(x=0,y=636,relwidth=1,height=180)
       
        Cost1_Label=Label(frame_6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        Cost1_text=Entry(frame_6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        Cost2_Label=Label(frame_6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        Cost2_text=Entry(frame_6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=4)

        Cost3_Label=Label(frame_6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        Cost3_text=Entry(frame_6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=3)

        
        Tax1_Label=Label(frame_6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        Tax1_text=Entry(frame_6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        Tax2_Label=Label(frame_6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        Tax2_text=Entry(frame_6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=4)

        Tax3_Label=Label(frame_6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        Tax3_text=Entry(frame_6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=3)



        #====================BUTTON FRAME===================>>
        Button_frame=Frame(frame_6,bd=7,relief=GROOVE)
        Button_frame.place(x=880,width=697,height=125)
     
        Total_Button=Button(Button_frame,command=self.total,text="Total",bg="cadetblue",bd=2,fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=10)
        Bill_Button=Button(Button_frame,command=self.bill_area,text="Generate Bill",bg="cadetblue",bd=2,fg="white",pady=15,width=11,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=10)
        Clear_Button=Button(Button_frame,text="Clear",command=self.clear_data,bg="cadetblue",bd=2,fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=10)
        Total_Button=Button(Button_frame,text="Exit",command=self.exit_app,bg="cadetblue",bd=2,fg="white",pady=15,width=9,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=10)

        self.welcome_bill()


    #===================CALCULATIONS=============>>
    def total(self):
        #=========COSMETIC COST CALCULATION==============>
        self.soap_price=self.soap.get()*30
        self.facecream_price=self.facecream.get()*120
        self.facewash_price=self.facewash.get()*60
        self.deodrant_price=self.deodrant.get()*190
        self.hairgel_price=self.hairgel.get()*50
        self.bodylotion_price=self.bodylotion.get()*80

        self.total_cosmetic_price=float(
            self.soap_price + self.facecream_price + self.facewash_price +
            self.deodrant_price + self.hairgel_price + self.bodylotion_price
        )
        
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))


        #============GROCERY COST CALCULATION============>>
        self.rice_price=self.rice.get()*40
        self.wheat_price=self.wheat.get()*290
        self.foodoil_price=self.foodoil.get()*180
        self.bread_price=self.bread.get()*35
        self.milk_price=self.milk.get()*26
        self.sugar_price=self.sugar.get()*45

        self.total_grocery_price=float(
             self.rice_price + self.wheat_price + self.foodoil_price +
             self.bread_price + self.milk_price + self.sugar_price 
        )
        
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        
        #=============COLD DRINK COST CALCULATION===========>>
        self.frooti_price=self.frooti.get()*60
        self.sprite_price=self.sprite.get()*70
        self.maza_price=self.maza.get()*60
        self.dew_price=self.dew.get()*70
        self.limca_price=self.limca.get()*70
        self.thumbsup_price=self.thumbsup.get()*70

        self.total_cold_drink_price=float(
             self.frooti_price + self.sprite_price + self.maza_price + 
             self.dew_price + self.limca_price + self.thumbsup_price 
        )
        
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.drink_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.drink_tax))


        #=============TOTAL BILL AMOUNT===============>>
        self.total_bill_cost=float(
            self.total_cosmetic_price + self.c_tax +
            self.total_grocery_price + self.g_tax +
            self.total_cold_drink_price + self.drink_tax
        )

    

    #===================BILL AREA============>>
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Easy Day Retail\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.customer_bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.customer_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.customer_phone_no.get()}")
        self.txtarea.insert(END,f"\n========================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n========================================")


    def bill_area(self):

        #=================VALIDATIONS===============>>
        if self.customer_name.get()=="" or self.customer_phone_no=="":
            messagebox.showerror("Error","Customer Details are must")
    
        elif self.cosmetic_price.get()=="Rs. 0.0" or self.grocery_price.get()=="Rs. 0.0" or self.cold_drink_price.get()=="Rs. 0.0": 
            messagebox.showerror("Error","No product purchased")
        
        else:
            self.welcome_bill()

            #=================COSMETIC CONDITIONS============>>
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.soap_price}")

            if self.facecream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.facecream.get()}\t\t{self.facecream_price}")

            if self.facewash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.facewash.get()}\t\t{self.facewash_price}")

            if self.deodrant.get()!=0:
                self.txtarea.insert(END,f"\n Deodrant\t\t{self.deodrant.get()}\t\t{self.deodrant_price}")

            if self.hairgel.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.hairgel.get()}\t\t{self.hairgel_price}") 
        
            if self.bodylotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.bodylotion.get()}\t\t{self.bodylotion_price}")

            
            #=================Grocery CONDITIONS============>>
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.rice_price}")

            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.wheat_price}")

            if self.foodoil.get()!=0:
                self.txtarea.insert(END,f"\n Food oil\t\t{self.foodoil.get()}\t\t{self.foodoil_price}")

            if self.bread.get()!=0:
                self.txtarea.insert(END,f"\n Bread\t\t{self.bread.get()}\t\t{self.bread_price}")

            if self.milk.get()!=0:
                self.txtarea.insert(END,f"\n Milk\t\t{self.milk.get()}\t\t{self.milk_price}") 
        
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.sugar_price}")

            
            #=================COLD DRINK CONDITIONS============>>
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.frooti_price}")

            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.sprite_price}")

            if self.dew.get()!=0:
                self.txtarea.insert(END,f"\n Dew\t\t{self.dew.get()}\t\t{self.dew_price}")

            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.maza_price}")

            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.limca_price}") 
        
            if self.thumbsup.get()!=0:
                self.txtarea.insert(END,f"\n Thumbs up\t\t{self.thumbsup.get()}\t\t{self.thumbsup_price}")


            #================TAX CONDITIONS======================>>       
            self.txtarea.insert(END,f"\n----------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")

            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")

            #===========TOTAL COST===========>>
            self.txtarea.insert(END,f"\n\n Total Bill Amount: Rs. \t\t\t{self.total_bill_cost}")
            self.txtarea.insert(END,f"\n----------------------------------------")
            
            self.save_data()


   
    #=================SAVE BILL=================>>
    def save_data(self):
        op=messagebox.askyesno("Save Bill","Do you want to save Bill?")

        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            save_file=open("Bills/"+str(self.customer_bill_no.get())+".txt","w")   
            save_file.write(self.bill_data)
            save_file.close()
            messagebox.showinfo("Saved",f"Bill Number: {self.customer_bill_no.get()} saved successfully")

        else:
            return


    #=====================SEARCH BILL===================>>
    def search_bill(self):

        flag=False
        for i in os.listdir("Bills/"):
            if i.split(".")[0]==self.search_bill_no.get():
                save_file=open(f"Bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for j in save_file:
                    self.txtarea.insert(END,j)
                save_file.close()
                flag=True

        if flag is False:
            messagebox.showerror("Error","Invalid Bill Number")
    

    #=========================CLEAR DATA================>>
    def clear_data(self):

        op=messagebox.askyesno("Clear","Do you really want to Clear Data?")
        if op>0:
            self.root.destroy()

            #===============COSMETIC VARIABLES==========>
            self.soap.set(0)
            self.facecream.set(0)
            self.facewash.set(0)
            self.deodrant.set(0)
            self.hairgel.set(0)
            self.bodylotion.set(0)

            #================GROCERY VARIABLES==========>>
            self.rice.set(0)
            self.wheat.set(0)
            self.foodoil.set(0)
            self.bread.set(0)
            self.milk.set(0)
            self.sugar.set(0)

            #================COLD DRINKS VARIABLES==========>>
            self.maza.set(0)
            self.dew.set(0)
            self.frooti.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            self.thumbsup.set(0)

            #================Total PRODUCT PRICE & TAX VARIABLES==========>>
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            #================CUSTOMER VARIABLES==========>>
            self.customer_name.set("")
            self.customer_phone_no.set("")
            self.customer_bill_no.set("")
            
            self.customer_bill_no.set("")
            x=random.randint(1000,9999)
            self.customer_bill_no.set(str(x))

            self.search_bill_no.set("")
            self.welcome_bill()


    #=================EXIT APP===========>>
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to Exit?")
        if op>0:
            self.root.destroy()

        

root=Tk()
obj=Bill_App(root)
root.mainloop()