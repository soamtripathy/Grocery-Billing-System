from tkinter import *
import random
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700")
        self.root.maxsize(width = 1280,height = 720)
        self.root.minsize(width = 1280,height = 720)
        self.root.title("Billing System")
        
        #====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        #For Generating Random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(x))

        self.bread = IntVar()
        self.candy = IntVar()
        self.Burger = IntVar()
        self.pizza = IntVar()
        self.pasta = IntVar()
        self.rice = IntVar()
        self.salt = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.maaza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.amulcool= IntVar()
        self.redbull= IntVar()
        self.total_food = StringVar()
        self.total_grocery = StringVar()
        self.total_drink = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_drink= StringVar()


        #=================================== FONT AND COLOURS
        label_font="times new roman,bold"
        entry_font="aerial,bold"
        bg_color = "teal"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.root,text = "Billing System By Soumya",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("times new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,font=("times new roman",10,"bold"),textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,font=("times new roman",10,"bold"),textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,font=("times new roman",10,"bold"),textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        
        search_button=Button(F1,text="Search",font=("times new roman",10,"bold"),width=8,relief=GROOVE,bd=8)
        search_button.grid(row=0,column=6,padx=20)

        #==================Food Frame=====================#
        F2 = LabelFrame(self.root,text = 'Food',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 380)

        #===========Frame Content
        bread_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bread")
        bread_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        bread_en = Entry(F2,bd = 8,relief = GROOVE,font = ("ariel",8,"bold"),textvariable = self.bread)
        bread_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Candy
        candy_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Candy")
        candy_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        candy_en = Entry(F2,bd = 8,relief = GROOVE,font = ("ariel",8,"bold"),textvariable = self.candy)
        candy_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #========Burger
        Burger_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Burger")
        Burger_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        Burger_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.Burger)
        Burger_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Pizza
        pizza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Pizza")
        pizza_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        pizza_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.pizza)
        pizza_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============pasta
        pasta_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Pasta")
        pasta_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        pasta_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.pasta)
        pasta_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Grocery Frame=====================#
        F2 = LabelFrame(self.root,text = 'Grocery',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 180,width = 325,height = 380)

        #===========Frame Content
        rice_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Rice")
        rice_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        rice_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.rice)
        rice_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======food oil
        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Oil")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.food_oil)
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======salt
        salt_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Salt")
        salt_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        salt_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.salt)
        salt_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========wheat
        wheat_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Wheat")
        wheat_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        wheat_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.wheat)
        wheat_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============sugar
        sugar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sugar")
        sugar_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        sugar_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.sugar)
        sugar_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Drinks frame=====================#

        F2 = LabelFrame(self.root,text = 'Others',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 180,width = 325,height = 380)

        #===========Frame Content

        #===========maaza

        maaza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Maaza")
        maaza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        maaza_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.maaza)
        maaza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======coke
        coke_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coke")
        coke_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        coke_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.coke)
        coke_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======frooti
        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Frooti")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.frooti)
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========amul cool
        amul_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Amul cool")
        amul_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        amul_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.amulcool)
        amul_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Red bull
        redbull_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Red bull")
        redbull_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        redbull_en = Entry(F2,font = ("ariel",8,"bold"),bd = 8,relief = GROOVE,textvariable = self.redbull)
        redbull_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #===================Bill Area================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 960,y = 180,width = 325,height = 380)

        #===========Bill area title
        bill_title = Label(F3,text = "Bill Area",font = ("times new ",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============Scrollbar in bill area
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set,wrap='wo')
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 145)

        #===================Total food
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Food")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE,font = ("ariel",8,"bold"),textvariable = self.total_food)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #=================== Total grocery
        gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Grocery")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F4,bd = 8,relief = GROOVE,font = ("ariel",8,"bold"),textvariable = self.total_grocery)
        gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================Total drink
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Drink")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,font = ("ariel",8,"bold"),relief = GROOVE,textvariable = self.total_drink)
        oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        #================ Food tax
        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Tax")
        cosmt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        cosmt_en = Entry(F4,bd = 8,font = ("ariel",8,"bold"),relief = GROOVE,textvariable = self.tax_cos)
        cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #================= Grocery tax
        grot_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Grocery Tax")
        grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        grot_en = Entry(F4,bd = 8,relief = GROOVE,font = ("ariel",8,"bold"),textvariable = self.tax_groc)
        grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================Drink tax
        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Drink Tax")
        otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 8,relief = GROOVE,font = ("ariel",8,"bold"),textvariable = self.tax_drink)
        otht_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

        #====================Buttons

        #===================Total button
        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("times new roman",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #========================Generate bill button
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("times new roman",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================Clear button
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("times new roman",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #======================Exit button
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("times new roman",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)

#Function to get total prices

    def total(self):
        #=================Total Food Prices
        self.total_food_prices = float(

            (self.bread.get() * 10)+
            (self.candy.get() * 3)+
            (self.Burger.get() * 80)+
            (self.pizza.get() * 250)+
            (self.pasta.get() * 120)
        )
        self.total_food.set("Rs. "+str(self.total_food_prices))
        self.tax_cos.set("Rs. "+str(round(self.total_food_prices*0.05)))

        #====================Total Grocery Prices
        self.total_grocery_prices = float(

            (self.rice.get() *20)+
            (self.food_oil.get() * 70)+
            (self.salt.get() * 10)+
            (self.wheat.get()*40)+
            (self.sugar.get() * 20)

        )
        self.total_grocery.set("Rs. "+str(self.total_grocery_prices))
        self.tax_groc.set("Rs. "+str(round(self.total_grocery_prices*0.07)))  #for 5% tax

        #======================Total Other Prices
        self.total_drink_prices = float(

            (self.maaza.get() * 15)+
            (self.coke.get() * 15)+
            (self.frooti.get() * 10)+
            (self.amulcool.get() * 20)+
            (self.redbull.get() * 80)
        )
        self.total_drink.set("Rs. "+str(self.total_drink_prices))
        self.tax_drink.set("Rs. "+str(round(self.total_drink_prices*0.03)))

        #==================total pricing
        self.total_pricing=self.total_food_prices+self.total_grocery_prices+self.total_drink_prices

        #=================total tax pricing
        self.total_tax=round(self.total_food_prices * 0.05+self.total_grocery_prices * 0.07+self.total_drink_prices * 0.03)


#Function For Text Area
    def welcome_bill(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To Soumya's Retail\n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\nProduct          Qty         Price")
        self.txt.insert(END,"\n===================================")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)
        self.bread.set(0)
        self.candy.set(0)
        self.Burger.set(0)
        self.pizza.set(0)
        self.pasta.set(0)
        self.rice.set(0)
        self.salt.set(0)
        self.food_oil.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.maaza.set(0)
        self.coke.set(0)
        self.frooti.set(0)
        self.amulcool.set(0)
        self.redbull.set(0)
        self.total_food.set("")
        self.total_grocery.set("")
        self.total_drink.set("")
        self.tax_cos.set("")
        self.tax_groc.set("")
        self.tax_drink.set("")
    
#Add Product name , qty and price to bill area
    def bill_area(self):
        self.no_detail()
        
        self.save_bill()
        
        self.welcome_bill()
        if self.bread.get() != 0:
            self.txt.insert(END,f"\nBread          {self.bread.get()}           {self.bread.get() * 10}")
        if self.candy.get() != 0:
            self.txt.insert(END,f"\nCandy          {self.candy.get()}           {self.candy.get() * 3}")
        if self.Burger.get() != 0:
            self.txt.insert(END,f"\nBurger         {self.Burger.get()}          {self.Burger.get() * 80}")
        if self.pizza.get() != 0:
            self.txt.insert(END,f"\nPizza          {self.pizza.get()}           {self.pizza.get() * 250}")
        if self.pasta.get() != 0 :
            self.txt.insert(END,f"\nPasta          {self.pasta.get()}           {self.pasta.get() * 120}")
        if self.rice.get() != 0:
            self.txt.insert(END,f"\nRice           {self.rice.get()}            {self.rice.get() * 20}")
        if self.food_oil.get() != 0:
            self.txt.insert(END,f"\nFood Oil       {self.food_oil.get()}        {self.food_oil.get() * 70}")
        if self.salt.get() != 0:
            self.txt.insert(END,f"\nSalt           {self.salt.get()}            {self.salt.get() * 10}")
        if self.wheat.get() != 0:
            self.txt.insert(END,f"\nWheat          {self.wheat.get()}           {self.wheat.get() * 40}")    
        if self.sugar.get() != 0:
            self.txt.insert(END,f"\nSugar          {self.sugar.get()}           {self.sugar.get() * 20}")
        if self.maaza.get() != 0:
            self.txt.insert(END,f"\nMaaza          {self.maaza.get()}           {self.maaza.get() * 15}")
        if self.coke.get() != 0:
            self.txt.insert(END,f"\nCoke           {self.coke.get()}            {self.coke.get() * 15}")
        if self.frooti.get() != 0:
            self.txt.insert(END,f"\nFrooti         {self.frooti.get()}          {self.frooti.get() * 10}")
        if self.amulcool.get() != 0:
            self.txt.insert(END,f"\nAmul cool      {self.amulcool.get()}           {self.amulcool.get() * 20}")
        if self.redbull.get() != 0:
            self.txt.insert(END,f"\nRedbull        {self.redbull.get()}         {self.redbull.get() * 80}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\nTotal price : Rs. {self.total_pricing}")
        self.txt.insert(END,f"\nTotal Tax : Rs. {self.total_tax}")
        self.txt.insert(END,f"\nNet Amount : Rs. {self.total_pricing+self.total_tax}")
#=========fuction for exit button
    def exit(self):
        self.root.destroy()


#function to get bill data
    def bill_data(self):
        file_=open("Bills/"+str(self.c_bill_no.get())+".txt","w")
        f=self.txt.get(END)
        file_.write(f)

        file_.close()

#function to get save bill data
    def save_bill(self):
       op= messagebox.askyesno("save","Do you want to save the bill?")

       if op>0:
          self.bill_data()
        

      
#====== Detail and product error      
    def no_detail(self):
        if self.cus_name.get() =="":
            messagebox.showerror("Error","Please enter the details !!!")
        elif self.c_phone.get() =="":
            messagebox.showerror("Error","Please enter the details !!!") 
        elif self.total_pricing==0.0:
            messagebox.showerror("Error","No product selected")    
        else:
            pass
