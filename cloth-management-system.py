import tkinter
from tkinter import *
import mysql.connector
import customtkinter as ctk
from tkinter import messagebox
import time
from tkinter import ttk

mydb = mysql.connector.connect(host='localhost', user='root', passwd='1234')
mycursor = mydb.cursor()
try:
    a = 'create database dysprosia'
    mycursor.execute(a)
except:
    pass

try:
    b = 'use dysprosia'
    mycursor.execute(b)
except:
    pass
try:
    mycursor.execute(
        "create table Items(Item_code varchar(4),Item_name varchar(20),Price varchar(5),quantity varchar(5),size varchar(4))")
    mydb.commit()
except:
    pass

try:
    c = 'alter table Items add primary key(Item_Code)'
    mycursor.execute(c)
    mydb.commit()
except:
    pass

window = ctk.CTk()
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("System")


# interface
def interface():
    window.geometry("900x600")
    window.title("Interface")
    login_frame = ctk.CTkFrame(window, height=550, width=850, border_width=3)
    login_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    label = ctk.CTkLabel(login_frame, text="Login Successfully :", font=("Century Gothic", 20))
    label.place(x=40, y=50)

    def add_item():
        login_frame.destroy()
        window.title("Add Item")
        frame1 = ctk.CTkFrame(window, height=550, width=850, border_width=3)
        frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        label = ctk.CTkLabel(frame1, text=" Add item :", font=("Century Gothic", 20))
        label.place(x=40, y=50)

        # buttons of add item

        itmcode = ctk.CTkEntry(frame1, width=300, height=30, placeholder_text="Item Code",
                               placeholder_text_color="Grey")
        itmname = ctk.CTkEntry(frame1, width=300, height=30, placeholder_text="Item Name",
                               placeholder_text_color="Grey")
        price = ctk.CTkEntry(frame1, width=300, height=30, placeholder_text="Price",
                             placeholder_text_color="Grey")
        quantity = ctk.CTkEntry(frame1, width=300, height=30, placeholder_text="Quantity",
                                placeholder_text_color="Grey")
        size = ctk.CTkEntry(frame1, width=300, height=30, placeholder_text="Size",
                            placeholder_text_color="Grey")

        def enter():
            try:
                item_code = itmcode.get()
                item_name = itmname.get()
                prc = price.get()
                qty = quantity.get()
                sze = size.get()
                A = [item_code, item_name, prc, qty, sze]

                mycursor.execute("INSERT INTO Items VALUES(%s,%s,%s,%s,%s)", A)

                mydb.commit()

                l_added = ctk.CTkLabel(frame1, text="Item Added successfully!", font=("Century Gothic", 18))
                l_added.place(x=90, y=350)
            except:
                l_added2 = ctk.CTkLabel(frame1, text="Item Already exist!          .", font=("Century Gothic", 18))
                l_added2.place(x=90, y=350)
            itmcode.delete(0, END)
            itmname.delete(0, END)
            price.delete(0, END)
            quantity.delete(0, END)
            size.delete(0, END)

        next_button = ctk.CTkButton(frame1, text="Enter ", width=200, height=40, font=("Century Gothic", 18),
                                    command=enter)

        add_exit = ctk.CTkButton(frame1, text="Exit", width=70, height=40, font=("Century Gothic", 18),
                                 fg_color="Maroon",
                                 command=interface)
        # placing button

        itmcode.place(x=90, y=100)
        itmname.place(x=90, y=150)
        quantity.place(x=90, y=200)
        price.place(x=90, y=250)
        size.place(x=90, y=300)

        next_button.place(x=90, y=400)
        add_exit.place(x=300, y=400)

    def search():
        login_frame.destroy()
        window.title("Search an Item :")
        frame1 = ctk.CTkFrame(window, height=550, width=850, border_width=3)
        frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        label = ctk.CTkLabel(frame1, text=" Search Item :", font=("Century Gothic", 20))
        label.place(x=40, y=50)

        itmcode = ctk.CTkEntry(frame1, width=300, height=30, placeholder_text="Item Code",
                               placeholder_text_color="Grey", font=("Arial", 15))
        itmcode.place(x=90, y=100)

        def Enter():
            try:
                item_code = itmcode.get()
                sql = 'select * from Items where Item_code =%s'
                tp = (item_code,)
                mycursor.execute(sql, tp)
                fetch = mycursor.fetchall()

                # Text box

                for j in fetch:
                    i = list(j)

                t1 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t2 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t3 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t4 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t5 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )

                t6 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t7 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t8 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t9 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t10 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )

                t1.place(x=90, y=200)
                t2.place(x=220, y=200)
                t3.place(x=350, y=200)
                t4.place(x=480, y=200)
                t5.place(x=620, y=200)

                t6.place(x=90, y=270)
                t7.place(x=220, y=270)
                t8.place(x=350, y=270)
                t9.place(x=480, y=270)
                t10.place(x=620, y=270)

                t1.insert(0.0, "Item Code")
                t2.insert(0.0, "Item Name")
                t3.insert(0.0, "Prize (RS)")
                t4.insert(0.0, "Quantity")
                t5.insert(0.0, "Size")

                t6.insert(0.0, i[0])
                t7.insert(0.0, i[1])
                t8.insert(0.0, i[2])
                t9.insert(0.0, i[3])
                t10.insert(0.0, i[4])
            except:

                Label1 = ctk.CTkLabel(frame1, text="Item does not Exist!", font=("arial", 18))
                Label1.place(x=90, y=370)
                itmcode.delete(0, END)

        next_button = ctk.CTkButton(frame1, text="Enter ", width=150, height=30, font=("Century Gothic", 16),
                                    command=Enter, )
        next_button.place(x=90, y=140)

        exit2 = ctk.CTkButton(frame1, text="Exit ", width=100, height=30, font=("Century Gothic", 16),
                              command=interface, fg_color="Maroon")
        exit2.place(x=250, y=140)

    def view():

        login_frame.destroy()
        window.title("View")
        frame1 = ctk.CTkFrame(window, height=550, width=850, border_width=3)
        frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        label = ctk.CTkLabel(frame1, text=" View Item:", font=("Century Gothic", 20))
        label.place(x=40, y=20)
        frame2 = ctk.CTkFrame(frame1, height=450, width=800, border_width=3)
        frame2.place(x=25, y=70)
        add_exit = ctk.CTkButton(frame1, text="X", width=70, height=30, font=("Century Gothic", 18),
                                 fg_color="Maroon", command=interface)
        add_exit.place(x=750, y=20)

        def count():
            sq = "select count(*) from Items"
            mycursor.execute(sq)
            fetch1 = mycursor.fetchall()
            for x in fetch1:
                for m in x:
                    pass
            return m

        t5 = ctk.CTkLabel(frame2, width=120, height=50, font=("Century Gothic", 15), text="Item _code")
        t6 = ctk.CTkLabel(frame2, width=120, height=50, font=("Century Gothic", 15), text="Item Name")
        t7 = ctk.CTkLabel(frame2, width=120, height=50, font=("Century Gothic", 15), text="Price")
        t8 = ctk.CTkLabel(frame2, width=120, height=50, font=("Century Gothic", 15), text="Quantity")
        t9 = ctk.CTkLabel(frame2, width=120, height=50, font=("Century Gothic", 15), text="Size")

        t5.grid(row=0, column=0, padx=20, pady=10)
        t6.grid(row=0, column=1, padx=20, pady=10)
        t7.grid(row=0, column=2, padx=20, pady=10)
        t8.grid(row=0, column=3, padx=20, pady=10)
        t9.grid(row=0, column=4, padx=20, pady=10)

        sql = "select * from Items"
        mycursor.execute(sql)
        fetch = mycursor.fetchall()
        End = count()
        for g in range(1, End + 1, 1):
            t1 = ctk.CTkTextbox(frame2, width=120, height=50, font=("Century Gothic", 15), )
            t2 = ctk.CTkTextbox(frame2, width=120, height=50, font=("Century Gothic", 15), )
            t3 = ctk.CTkTextbox(frame2, width=120, height=50, font=("Century Gothic", 15), )
            t4 = ctk.CTkTextbox(frame2, width=120, height=50, font=("Century Gothic", 15), )
            t5 = ctk.CTkTextbox(frame2, width=120, height=50, font=("Century Gothic", 15), )

            t1.grid(row=g, column=0, padx=20, pady=10)
            t2.grid(row=g, column=1, padx=20, pady=10)
            t3.grid(row=g, column=2, padx=20, pady=10)
            t4.grid(row=g, column=3, padx=20, pady=10)
            t5.grid(row=g, column=4, padx=20, pady=10)

        for i in fetch:
            def hi():
                i0 = i[0]
                nonlocal t1
                t1.insert(0.0, i0)
                t2.insert(0.0, i[1])
                t3.insert(0.0, i[2])
                t4.insert(0.0, i[3])
                t5.insert(0.0, i[4])
                i0 = ""

            hi()

    def update():
        login_frame.destroy()
        window.title("Update an Item :")
        frame1 = ctk.CTkFrame(window, height=550, width=850, border_width=3)
        frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        label = ctk.CTkLabel(frame1, text=" Update an Item :", font=("Century Gothic", 20))
        label.place(x=40, y=50)

        itmcode = ctk.CTkEntry(frame1, width=300, height=30, placeholder_text="Item Code",
                               placeholder_text_color="Grey", font=("Arial", 15))
        itmcode.place(x=90, y=100)

        def Enter():
            try:
                item_code = itmcode.get()
                sql = 'select * from Items where Item_code =%s'
                tp = (item_code,)
                mycursor.execute(sql, tp)
                fetch = mycursor.fetchall()

                # Text box

                for j in fetch:
                    i = list(j)

                t1 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t2 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t3 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t4 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t5 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )

                t6 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t7 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t8 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t9 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t10 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )

                t1.place(x=90, y=200)
                t2.place(x=220, y=200)
                t3.place(x=350, y=200)
                t4.place(x=480, y=200)
                t5.place(x=620, y=200)

                t6.place(x=90, y=270)
                t7.place(x=220, y=270)
                t8.place(x=350, y=270)
                t9.place(x=480, y=270)
                t10.place(x=620, y=270)

                t1.insert(0.0, "Item Code")
                t2.insert(0.0, "Item Name")
                t3.insert(0.0, "Prize (RS)")
                t4.insert(0.0, "Quantity")
                t5.insert(0.0, "Size")

                t6.insert(0.0, i[0])
                t7.insert(0.0, i[1])
                t8.insert(0.0, i[2])
                t9.insert(0.0, i[3])
                t10.insert(0.0, i[4])

                def confrim():
                    frame1.destroy()
                    frame2 = ctk.CTkFrame(window, height=550, width=850, border_width=3)
                    frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
                    label3 = ctk.CTkLabel(frame2, text=" Update an Item :", font=("Century Gothic", 20))
                    label3.place(x=40, y=50)

                    new_var = StringVar()

                    # radio button
                    def radiobutton_event():
                        pass

                    Item_name = ctk.CTkRadioButton(frame2, text="Item Name", font=("Times New Roman", 18),
                                                   command=radiobutton_event, variable=new_var, value="Item_name")
                    Price = ctk.CTkRadioButton(frame2, text="Price", font=("Times New Roman", 18),
                                               command=radiobutton_event, variable=new_var, value="Price")
                    quantity = ctk.CTkRadioButton(frame2, text="Quantity", font=("Times New Roman", 18),
                                                  command=radiobutton_event, variable=new_var, value="Quantity")
                    size = ctk.CTkRadioButton(frame2, text="Size", font=("Times New Roman", 18),
                                              command=radiobutton_event, variable=new_var, value="Size")

                    def OK():
                        value = new_var.get()
                        if value == "Item_name":
                            textbox = ctk.CTkEntry(frame2, width=300, height=30, placeholder_text=" New Item Name",
                                                   placeholder_text_color="Grey", font=("Arial", 15))
                            textbox.place(x=90, y=200)

                            def next1():
                                new = textbox.get()
                                try:
                                    sql = "update Items set Item_Name='%s' where Item_Code='%s';" % (new, item_code)
                                    mycursor.execute(sql)
                                    mydb.commit()
                                    messagebox.showinfo("UPDATED", "Updated Successfully!")
                                    update()
                                except:
                                    messagebox.showerror("ERROR", "Try again")
                                    update()

                            nb = ctk.CTkButton(frame2, text=">", width=70, height=30, command=next1)
                            nb.place(x=400, y=200)

                        elif value == "Price":
                            textbox = ctk.CTkEntry(frame2, width=300, height=30, placeholder_text=" New Price",
                                                   placeholder_text_color="Grey", font=("Arial", 15))
                            textbox.place(x=90, y=200)

                            def next1():
                                new = textbox.get()
                                try:
                                    sql = "update Items set Price='%s' where Item_code='%s';" % (new, item_code)
                                    mycursor.execute(sql)
                                    mydb.commit()
                                    messagebox.showinfo("UPDATED", "Updated Successfully!")
                                    update()
                                except:
                                    messagebox.showerror("ERROR", "Try again")
                                    update()

                            nb = ctk.CTkButton(frame2, text=">", width=70, height=30, command=next1)
                            nb.place(x=400, y=200)
                        elif value == "Quantity":
                            textbox = ctk.CTkEntry(frame2, width=300, height=30, placeholder_text=" New Quantity",
                                                   placeholder_text_color="Grey", font=("Arial", 15))
                            textbox.place(x=90, y=200)

                            def next1():
                                new = textbox.get()
                                try:
                                    sql = "update Items set Quantity='%s' where Item_code='%s';" % (new, item_code)
                                    mycursor.execute(sql)
                                    mydb.commit()
                                    messagebox.showinfo("UPDATED", "Updated Successfully!")
                                    update()
                                except:
                                    messagebox.showerror("ERROR", "Try again")
                                    update()

                            nb = ctk.CTkButton(frame2, text=">", width=70, height=30, command=next1)
                            nb.place(x=400, y=200)

                        elif value == "Size":
                            textbox = ctk.CTkEntry(frame2, width=300, height=30, placeholder_text=" New Size",
                                                   placeholder_text_color="Grey", font=("Arial", 15))
                            textbox.place(x=90, y=200)

                            def next1():
                                new = textbox.get()
                                try:
                                    sql = "update Items set Size='%s' where Item_code='%s';" % (new, item_code)
                                    mycursor.execute(sql)
                                    mydb.commit()
                                    messagebox.showinfo("UPDATED", "Updated Successfully!")
                                    update()
                                except:
                                    messagebox.showerror("ERROR", "Try again")
                                    update()

                            nb = ctk.CTkButton(frame2, text=">", width=70, height=30, command=next1)
                            nb.place(x=400, y=200)

                    ok_button = ctk.CTkButton(frame2, text="OK", width=100, height=30,
                                              font=("Century Gothic", 16),
                                              command=OK)

                    Item_name.place(x=90, y=100)
                    Price.place(x=210, y=100)
                    quantity.place(x=300, y=100)
                    size.place(x=410, y=100)
                    ok_button.place(x=90, y=150)

                confirm_button = ctk.CTkButton(frame1, text="Confrim", width=100, height=30,
                                               font=("Century Gothic", 16),
                                               command=confrim)
                confirm_button.place(x=90, y=350)

            except:

                time.sleep(1)
                update()

        next_button = ctk.CTkButton(frame1, text="Enter ", width=150, height=30, font=("Century Gothic", 16),
                                    command=Enter, )
        next_button.place(x=90, y=140)

        exit2 = ctk.CTkButton(frame1, text="Exit ", width=100, height=30, font=("Century Gothic", 16),
                              command=interface, fg_color="Maroon")
        exit2.place(x=250, y=140)

    def delete():

        login_frame.destroy()
        window.title("Delete an ITem :")
        frame1 = ctk.CTkFrame(window, height=550, width=850, border_width=3)
        frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        label = ctk.CTkLabel(frame1, text=" Delete an Item :", font=("Century Gothic", 20))
        label.place(x=40, y=50)

        itmcode = ctk.CTkEntry(frame1, width=300, height=30, placeholder_text="Item Code",
                               placeholder_text_color="Grey", font=("Arial", 15))
        itmcode.place(x=90, y=100)

        def Enter():
            try:
                item_code = itmcode.get()
                sql = 'select * from Items where Item_code =%s'
                tp = (item_code,)
                mycursor.execute(sql, tp)
                fetch = mycursor.fetchall()

                # Text box

                for j in fetch:
                    i = list(j)

                t1 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t2 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t3 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t4 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t5 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )

                t6 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t7 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t8 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t9 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )
                t10 = ctk.CTkTextbox(frame1, width=120, height=50, font=("Century Gothic", 15), )

                t1.place(x=90, y=200)
                t2.place(x=220, y=200)
                t3.place(x=350, y=200)
                t4.place(x=480, y=200)
                t5.place(x=620, y=200)

                t6.place(x=90, y=270)
                t7.place(x=220, y=270)
                t8.place(x=350, y=270)
                t9.place(x=480, y=270)
                t10.place(x=620, y=270)

                t1.insert(0.0, "Item Code")
                t2.insert(0.0, "Item Name")
                t3.insert(0.0, "Prize (RS)")
                t4.insert(0.0, "Quantity")
                t5.insert(0.0, "Size")

                t6.insert(0.0, i[0])
                t7.insert(0.0, i[1])
                t8.insert(0.0, i[2])
                t9.insert(0.0, i[3])
                t10.insert(0.0, i[4])

                def confrim():
                    sq = "delete from Items where Item_code=%s"
                    t = (item_code,)
                    mycursor.execute(sq, t)
                    mydb.commit()
                    labe1 = ctk.CTkLabel(frame1, text="Deleted Succesfully", width=200, height=40,
                                         font=("Century Gothic", 16))
                    labe1.place(x=90, y=400)

                confirm_button = ctk.CTkButton(frame1, text="Confrim", width=100, height=30,
                                               font=("Century Gothic", 16),
                                               command=confrim)
                confirm_button.place(x=90, y=350)

            except:

                time.sleep(1)
                delete()

        next_button = ctk.CTkButton(frame1, text="Enter ", width=150, height=30, font=("Century Gothic", 16),
                                    command=Enter, )
        next_button.place(x=90, y=140)

        exit2 = ctk.CTkButton(frame1, text="Exit ", width=100, height=30, font=("Century Gothic", 16),
                              command=interface, fg_color="Maroon")
        exit2.place(x=250, y=140)

    def exit1():
        window.destroy()

    # Button of interface(definition)

    add_button = ctk.CTkButton(login_frame, text="Add a item", font=("Times New Roman", 20), width=200, height=120,
                               command=add_item)
    search_button = ctk.CTkButton(login_frame, text="Search a item", font=("Times New Roman", 20), width=200,
                                  height=120, command=search)
    delete_button = ctk.CTkButton(login_frame, text="Delete a item", font=("Times New Roman", 20), width=200,
                                  height=120, command=delete)
    update_button = ctk.CTkButton(login_frame, text="Update a item", font=("Times New Roman", 20), width=200,
                                  height=120, command=update)
    view_button = ctk.CTkButton(login_frame, text="View a item", font=("Times New Roman", 20), width=200, height=120,
                                command=view)
    exit_button = ctk.CTkButton(login_frame, text="Exit", font=("Times New Roman", 20), width=200, height=120,
                                command=exit1)

    add_button.place(x=100, y=120)
    search_button.place(x=340, y=120)
    update_button.place(x=580, y=120)

    delete_button.place(x=100, y=300)
    view_button.place(x=340, y=300)
    exit_button.place(x=580, y=300)


# login
def login1():
    window.title("Login")
    window.geometry("600x440")
    login_frame = ctk.CTkFrame(window, height=360, width=320, border_width=3)
    login_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    login_label = ctk.CTkLabel(login_frame, text="Login :", font=("Century Gothic", 20, "bold"))
    login_label.place(x=40, y=50)

    username = ctk.CTkEntry(login_frame, width=240, height=30, fg_color="white", corner_radius=10,
                            placeholder_text="Username",
                            font=("Calibri", 14), placeholder_text_color="black", text_color="Black")
    username.place(x=45, y=90)

    password = ctk.CTkEntry(login_frame, width=240, height=30, fg_color="white", corner_radius=10,
                            placeholder_text="Password",
                            font=("Calibri", 14), placeholder_text_color="black", show="*", text_color="Black")
    password.place(x=45, y=130)

    def login():
        user = username.get()
        psd = password.get()
        if user == "admin" and psd == "1234":
            login_frame.destroy()
            interface()
        else:
            messagebox.showerror("ERROR", 'Incorrect Password \nor Username')
            login1()

    button_login = ctk.CTkButton(login_frame, text="Login", font=("calibri", 14), width=240, command=login)
    button_login.place(x=45, y=200)


login1()

window.mainloop()