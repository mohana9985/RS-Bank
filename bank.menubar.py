from cProfile import label
from cgi import test
from ctypes import resize
from ctypes.wintypes import LONG
from email import message
from email.mime import image
from fileinput import filename
from select import select
from sqlite3 import connect
from tkinter import *
from tkinter import messagebox
import tkinter
import cryptography
import pymysql
from datetime import date, datetime
from dateutil import parser
import sqlite3
from tkinter import image_types
from tkinter import Tk 
from tkinter import Canvas
from PIL import Image,ImageTk

class Bank:

    # Login
    def log(self):

        self.lg = Tk()
        self.lg.geometry("700x500+350+100")
        self.lg.title("RS Bank")

        # Labels
        l1 = Label(self.lg, text="Login Page", font="Arial 30")
        l1.place(x=270, y=30)
        l2 = Label(self.lg, text="User name or Full name:", font="arial 15")
        l2.place(x=120, y=150)
        l3 = Label(self.lg, text="Password:", font="arial 15")
        l3.place(x=120, y=200)
        l4 = Label(self.lg, text="Create a new account", font="arial 15")
        l4.place(x=100, y=450)

        # Text box
        self.lt1 = Text(self.lg, width=15, height=1)
        self.lt1.place(x=400, y=150)

        self.lt1.focus()

        self.lt2 = Entry(self.lg, width=20, show='*')
        self.lt2.place(x=400, y=200)
        # widget = Entry(self.lg, show="*", width=15foreground="black")
        # widget.place(x=400,y=200)

        # Buttons
        b1 = Button(text="Login", command=self.ver)
        b1.place(x=150, y=300)
        b2 = Button(text="Cancel", command=self.lg.destroy)
        b2.place(x=450, y=300)
        b3 = Button(text="Sign in", command=self.reg)
        b3.place(x=400, y=450)

        self.lg.mainloop()

    # Registration
    def reg(self):

        self.lg.destroy()

        self.main = Tk()
        self.main.geometry("700x500+350+100")
        self.main.title("Registration Page")
        self.main

        # Labels

        l1 = Label(self.main, text="Registration Form", font="Arial 20")
        l1.place(x=260, y=20)
        l2 = Label(self.main, text="Full name:", font="18")
        l2.place(x=150, y=100)
        l3 = Label(self.main, text="Nick name:", font="18")
        l3.place(x=150, y=130)
        l4 = Label(self.main, text="Date of Birth(YYYY-MM-DD):", font="18")
        l4.place(x=150, y=160)
        l5 = Label(self.main, text="Phone Number:", font="18")
        l5.place(x=150, y=190)
        l6 = Label(self.main, text="Mail id:", font="18")
        l6.place(x=150, y=220)
        l7 = Label(self.main, text="Password:", font="18")
        l7.place(x=150, y=250)
        l8 = Label(self.main, text="Confirm Password:", font="18")
        l8.place(x=150, y=280)

        # Text Box

        self.rt1 = Text(self.main, width=15, height=1)
        self.rt1.place(x=450, y=100)
        self.rt1.focus()
        self.rt2 = Text(self.main, width=15, height=1)
        self.rt2.place(x=450, y=130)
        self.rt3 = Text(self.main, width=15, height=1)
        self.rt3.place(x=450, y=160)
        self.rt4 = Text(self.main, width=15, height=1)
        self.rt4.place(x=450, y=190)
        self.rt5 = Text(self.main, width=15, height=1)
        self.rt5.place(x=450, y=220)
        self.rt6 = Entry(self.main, width=15, show='*')
        self.rt6.place(x=450, y=250)
        self.rt7 = Entry(self.main, width=15, show='*')
        self.rt7.place(x=450, y=280)

        # Buttons

        b1 = Button(self.main, text="Ok", command=self.suc)
        b1.place(x=200, y=350)
        b2 = Button(self.main, text="Cancel", command=self.regback)
        b2.place(x=450, y=350)

        self.main.mainloop()

    def regback(self):
        self.main.destroy()
        self.log()

    # Registration Successfull
    def suc(self):

        try:
            con = pymysql.connect(
                host="localhost", user="root", password="rootroot", db="bank")
            cur = con.cursor()

            fn = self.rt1.get(1.0, "end")
            nn = self.rt2.get(1.0, "end")
            dob = self.rt3.get(1.0, "end")
            ph = self.rt4.get(1.0, "end")
            mid = self.rt5.get(1.0, "end")
            pw = self.rt6.get()
            rpw = self.rt7.get()
            dob = dob[0:-1]
            fn = fn[0:-1]
            nn = nn[0:-1]
            ph = ph[0:-1]
            mid = mid[0:-1]

            try:
                dob = parser.parse(dob)
                dob = datetime.date(dob)
                # dob=str(dob)
                if (fn == ""):
                    messagebox.showinfo("Info", "Enter Full name")
                elif (nn == ""):
                    messagebox.showinfo("Info", "Enter Nick name")
                elif (fn == nn):
                    messagebox.showinfo(
                        "Info", "Full name & nick name can't be same")
                elif (len(ph) != 10):
                    messagebox.showinfo("Info", "Incorrect mobile no.")
                elif (mid[-1:-11:-1] != "moc.liamg@"):
                    messagebox.showinfo("Info", "Incorrect mail id")
                elif (pw == ""):
                    messagebox.showinfo("Info", "Enter password")
                elif (pw != rpw):
                    messagebox.showinfo(
                        "Info", "Once check the password and confirm password")
                else:
                    cur.execute("select * from login")
                    temp = 0
                    for j in cur:
                        if (j[0] == fn):
                            temp = 1
                            break
                    if (temp):
                        messagebox.showinfo("Info", "Full name already exits")
                    else:
                        cur.execute(
                            "insert into login values(%s,%s,%s,%s,%s,%s);", (fn, pw, dob, nn, ph, mid))
                        con.commit()
                        messagebox.showinfo("Info", "Registration successfull")
                        self.main.destroy()
                        self.log()
            except Exception as e:
                messagebox.showinfo("Info", "Incorrect date format")

        except Exception as e:
            print(e)

        finally:
            cur.close()
            con.close()

    def ver(self):
        try:
            con = pymysql.connect(
                host="localhost", user="root", password="rootroot", db="bank")
            cur = con.cursor()

            n = self.lt1.get(1.0, "end")
            pw = self.lt2.get()
            cur.execute("select * from login")
            temp = 0
            for j in cur:
                if (n[0:-1] == j[0] and pw == j[1]):
                    temp = 1
                    break
            if (temp):
                self.lg.destroy()
                self.acc()
            else:
                messagebox.showinfo("Info", "Incorrect Username or Password")

        except Exception as e:
            messagebox.showinfo("Info", "Something went wrong")
            print(e)

        finally:
            cur.close()
            con.close()

    # Account

    def acc(self):
        self.ac = Tk()
        self.ac.geometry("1525x800+0+0")
        self.ac.title("Account Page")
    #image settings

        can=Canvas(self.ac,width=1525,height=800)
        can.pack()
        img=(Image.open("/Users/kuretimohanasambasiva/Desktop/RSBank/banking/bank1.png"))
        #img1=(Image.open("/Users/kuretimohanasambasiva/Desktop/RSBank/banking/acc_open.png"))
        resi=img.resize((1525,800))
        newimg=ImageTk.PhotoImage(resi)
        can.create_image(0,0,anchor=NW,image=newimg)
    #MenuBar 
        menubar = Menu(self.ac)
        bankmenu = Menu(menubar)
        bankmenu.add_command(label="Account Open", command=self.accopen)
        bankmenu.add_command(label="Account Info", command=self.info)
        bankmenu.add_command(label="Deposit", command=self.depo)
        bankmenu.add_command(label="Withdraw", command=self.withdraw)
        bankmenu.add_command(label="Account Summary", command=self.accsum)
        bankmenu.add_command(label="Remove account", command=self.rem)
        bankmenu.add_command(label="Logout", command=self.logout)

        menubar.add_cascade(label="Bank", menu=bankmenu)

        self.ac.config(menu=menubar)
        self.ac.mainloop()

        #without menubar

        #   # Account Page
        #   self.ac = Tk()
        #   self.ac.geometry("1525x820+0+0")
        #   self.ac.title("Account Page")

        #   menubar = Menu(self.ac)
        #   bankmenu = Menu(menubar, tearoff=0)
        #   bankmenu.add_command(Label="Account Open", command=self.accopen)
        #   bankmenu.add_command(Label="Account Info", command=self.info)
        #   bankmenu.add_command(Label="Deposit", command=self.depo)
        #   bankmenu.add_command(Label="Withdraw", command=self.withdraw)
        #   bankmenu.add_command(Label="Account Summary", command=self.accsum)
        #   bankmenu.add_command(Label="Remove account", command=self.rem)
        #   bankmenu.add_command(Label="Logout", command=self.logout)
        #   menubar.add_cascade(Label="Bank", menu=bankmenu)

        # Buttons
         # b1 = Button(self.ac, text="Account Open", command=self.accopen)
        #   b1.place(x=30, y=50)
        #   b2 = Button(self.ac, text="Account Info", command=self.info)
        #   b2.place(x=30, y=100)
        #   b3 = Button(self.ac, text="Deposit", command=self.depo)
        #   b3.place(x=30, y=150)
        #   b4 = Button(self.ac, text="Withdraw", command=self.withdraw)
        #   b4.place(x=410, y=50)
        #   b5 = Button(self.ac, text="Account Summary", command=self.accsum)
        #   b5.place(x=362, y=100)
        #   b6 = Button(self.ac, text="Remove acccont", command=self.rem)
        #   b6.place(x=372, y=150)
        #   b7 = Button(self.ac, text="Logout", command=self.logout)
        #   b7.place(x=220, y=220)

        self.ac.mainloop()

    # Logout

    def logout(self):

        self.small = Tk()

        self.small.geometry("300x200+500+200")
        self.small.title("Info")
        self.small

        # Labels
        l1 = Label(self.small, text="Are you sure to logout:")
        l1.place(x=50, y=50)

        # Buttons
        b1 = Button(self.small, text="Yes", command=self.lo)
        b1.place(x=50, y=100)
        b2 = Button(self.small, text="No", command=self.small.destroy)
        b2.place(x=130, y=100)
        self.small.mainloop()

    def lo(self):
        self.small.destroy()
        self.ac.destroy()
        #messagebox.showinfo("Info","Loged out successfully")

    # Remove account
    def rem(self):

        self.rm = Tk()
        self.rm.geometry("600x400+400+150")
        self.rm.title("Account closing page")

        # Labels
        l1 = Label(self.rm, text="Name:")
        l1.place(x=200, y=125)
        l2 = Label(self.rm, text="DOB:")
        l2.place(x=200, y=175)
        l3 = Label(self.rm, text="Balance:")
        l3.place(x=200, y=225)
        l4 = Label(self.rm, text="Account no")
        l4.place(x=125, y=50)

        # Text box
        self.rt1 = Text(self.rm, width=20, height=1)
        self.rt1.place(x=225, y=50)

        # Buttons
        b1 = Button(self.rm, text="Remove Account", command=self.racc)
        b1.place(x=400, y=300)
        b2 = Button(self.rm, text="Back", command=self.rm.destroy)
        b2.place(x=100, y=300)
        b3 = Button(self.rm, text="Search", command=self.rser)
        b3.place(x=450, y=50)

        self.rm.mainloop()

    def rser(self):
        an = self.rt1.get(1.0, "end")
        an = int(an[0:-1])
        try:
            con = pymysql.connect(
                host="localhost", user="root", password="rootroot", db="bank")
            cur = con.cursor()
            if (cur.execute("select name,dob,bal from accounts where an=%s and alive=%s", (an, "yes"))):
                for i in cur:
                    if (cur):
                        l4 = Label(self.rm, text=i[0])
                        l4.place(x=350, y=125)
                        l5 = Label(self.rm, text=i[1])
                        l5.place(x=350, y=175)
                        l6 = Label(self.rm, text=i[2])
                        l6.place(x=350, y=225)
            else:
                messagebox.showinfo("Info", "Account not found")

        except Exception as e:
            messagebox.showinfo("Info", "Something went wrong")
            print(e)

        finally:
            cur.close()
            con.close()

    def racc(self):
        self.rser()
        an = self.rt1.get(1.0, "end")
        an = int(an[0:-1])
        try:
            con = pymysql.connect(
                host="localhost", user="root", password="rootroot", db="bank")
            cur = con.cursor()
            if (cur.execute("select name,dob,bal from accounts where an=%s and alive=%s", (an, "yes"))):
                cur.execute("update accounts set alive = " +
                            "'"+"no"+"'"+" where an = %s", (an))
                con.commit()
                messagebox.showinfo("Info", "Account Closed")
            else:
                messagebox.showinfo("Info", "Account not found")

        except Exception as e:
            messagebox.showinfo("Info", "Something went wrong")
            print(e)

        finally:
            cur.close()
            con.close()

    # Info

    def info(self):

        #self.io = Tk()
        self.io=Toplevel()
        self.io.geometry("400x300+500+150")
        self.io.title("INFO")
    #Image Setting
        can2=Canvas(self.io,width=400,height=300)
        can2.pack()
        img2=(Image.open("/Users/kuretimohanasambasiva/Desktop/RSBank/banking/accinfo.png"))
        resi2=img2.resize((400,300))
        newimg2=ImageTk.PhotoImage(resi2)
        can2.create_image(0,0,anchor=NW,image=newimg2)
        
        # Label
        l1 = Label(self.io, text="Account no")
        l1.place(x=100 , y=100)
        # textbox
        self.it1 = Text(self.io, width=15, height=1)
        self.it1.place(x=150, y=55)

        # button
        b1 = Button(self.io, text="Sumbit", command=self.ai)
        b1.place(x=300, y=50)
        b2 = Button(self.io, text="Back", command=self.io.destroy)
        b2.place(x=150, y=250)
        l1.pack(pady=50)
        self.io.mainloop()

    def ai(self):

        an = self.it1.get(1.0, "end")
        an = int(an[0:-1])

        try:
            con = pymysql.connect(
                host="localhost", user="root", password="rootroot", db="bank")
            cur = con.cursor()
            if (cur.execute("select name,dob,bal from accounts where an=%s and alive=%s", (an, "yes"))):
                for i in cur:
                    if (cur):
                        l1 = Label(self.io, text="Name")
                        l1.place(x=100, y=100)
                        l2 = Label(self.io, text="DOB")
                        l2.place(x=100, y=150)
                        l3 = Label(self.io, text="Balance")
                        l3.place(x=100, y=200)

                        l4 = Label(self.io, text=i[0])
                        l4.place(x=200, y=100)
                        l5 = Label(self.io, text=i[1])
                        l5.place(x=200, y=150)
                        l6 = Label(self.io, text=i[2])
                        l6.place(x=200, y=200)
            else:
                messagebox.showinfo("Info", "Account not found")
        except Exception as e:
            messagebox.showinfo("Info", "Something went wrong")
            print(e)

        finally:
            cur.close()
            con.close()

    # Deposit
    def depo(self):

        self.dp = tkinter.Toplevel()
        self.dp.geometry("500x400+500+150")
        self.dp.title("Deposit Page")
    #image settings
        can4=Canvas(self.dp,width=500,height=400)
        can4.pack()
        img4=(Image.open("/Users/kuretimohanasambasiva/Desktop/RSBank/banking/deposit.png"))
        resi4=img4.resize((500,400))
        newimg4=ImageTk.PhotoImage(resi4)
        can4.create_image(0,0,anchor=NW,image=newimg4)
        
        
        # Label
        l1 = Label(self.dp, text="Account no")
        l1.place(x=50, y=50)
        l2 = Label(self.dp, text="Deposit amount")
        l2.place(x=50, y=100)
        # textbox
        self.dt1 = Text(self.dp, width=20, height=1)
        self.dt1.place(x=200, y=50)
        self.dt2 = Text(self.dp, width=20, height=1)
        self.dt2.place(x=200, y=100)

        # button
        b1 = Button(self.dp, text="Search", command=self.dser)
        b1.place(x=400, y=75)
        b2 = Button(self.dp, text="Back", command=self.dp.destroy)
        b2.place(x=100, y=350)
        b3 = Button(self.dp, text="Deposit", command=self.ds)
        b3.place(x=350, y=350)

        self.dp.mainloop()

    def dser(self):
        an = self.dt1.get(1.0, "end")
        an = int(an[0:-1])
        try:
            con = pymysql.connect(
                host="localhost", user="root", password="rootroot", db="bank")
            cur = con.cursor()
            if (cur.execute("select name,dob,bal from accounts where an=%s and alive=%s", (an, "yes"))):
                for i in cur:
                    if (cur):
                        l1 = Label(self.dp, text="Name")
                        l1.place(x=150, y=175)
                        l2 = Label(self.dp, text="DOB")
                        l2.place(x=150, y=225)
                        l3 = Label(self.dp, text="Balance")
                        l3.place(x=150, y=275)

                        l4 = Label(self.dp, text=i[0])
                        l4.place(x=250, y=175)
                        l5 = Label(self.dp, text=i[1])
                        l5.place(x=250, y=225)
                        l6 = Label(self.dp, text=i[2])
                        l6.place(x=250, y=275)
            else:
                messagebox.showinfo("Info", "Account not found")

        except Exception as e:
            messagebox.showinfo("Info", "Something went wrong")
            print(e)

        finally:
            cur.close()
            con.close()

    def ds(self):
        an = self.dt1.get(1.0, "end")
        an = int(an[0:-1])
        da = self.dt2.get(1.0, "end")
        da = int(da[0:-1])

        try:
            con = pymysql.connect(
                host="localhost", user="root", password="rootroot", db="bank")
            cur = con.cursor()
            if (cur.execute("select name,dob,bal from accounts where an=%s and alive=%s", (an, "yes"))):
                for i in cur:
                    if (cur):
                        l1 = Label(self.dp, text="Name")
                        l1.place(x=150, y=175)
                        l2 = Label(self.dp, text="DOB")
                        l2.place(x=150, y=225)
                        l3 = Label(self.dp, text="Balance")
                        l3.place(x=150, y=275)

                        l4 = Label(self.dp, text=i[0])
                        l4.place(x=250, y=175)
                        l5 = Label(self.dp, text=i[1])
                        l5.place(x=250, y=225)
                        am = i[2]+da
                        l6 = Label(self.dp, text=i[2]+da)
                        l6.place(x=250, y=275)
                cur.execute("update accounts set bal=%s where an=%s", (am, an))
                con.commit()
                messagebox.showinfo("Info", "Amount Deposited")
            else:
                messagebox.showinfo("Info", "Account not found")

        except Exception as e:
            messagebox.showinfo("Info", "Something went wrong")
            print(e)

        finally:
            cur.close()
            con.close()

    # Withdraw

    def withdraw(self):

        self.wd = Tk()
        self.wd.geometry("500x400+500+150")
        self.wd.title("Withdraw Page")
        self.wd
        # Label
        l1 = Label(self.wd, text="Account no")
        l1.place(x=50, y=50)
        l2 = Label(self.wd, text="Withdraw amount")
        l2.place(x=50, y=100)
        # textbox
        self.wt1 = Text(self.wd, width=20, height=1)
        self.wt1.place(x=200, y=50)
        self.wt2 = Text(self.wd, width=20, height=1)
        self.wt2.place(x=200, y=100)

        # button
        b1 = Button(self.wd, text="Search", command=self.wser)
        b1.place(x=400, y=75)
        b2 = Button(self.wd, text="Back", command=self.wd.destroy)
        b2.place(x=100, y=350)
        b3 = Button(self.wd, text="Withdraw", command=self.ws)
        b3.place(x=350, y=350)

        self.wd.mainloop()

    def wser(self):
        an = self.wt1.get(1.0, "end")
        an = int(an[0:-1])
        try:
            con = pymysql.connect(
                host="localhost", user="root", password="rootroot", db="bank")
            cur = con.cursor()
            if (cur.execute("select name,dob,bal from accounts where an=%s and alive=%s", (an, "yes"))):
                for i in cur:
                    if (cur):
                        l1 = Label(self.wd, text="Name")
                        l1.place(x=150, y=175)
                        l2 = Label(self.wd, text="DOB")
                        l2.place(x=150, y=225)
                        l3 = Label(self.wd, text="Balance")
                        l3.place(x=150, y=275)

                        l4 = Label(self.wd, text=i[0])
                        l4.place(x=250, y=175)
                        l5 = Label(self.wd, text=i[1])
                        l5.place(x=250, y=225)
                        l6 = Label(self.wd, text=i[2])
                        l6.place(x=250, y=275)
            else:
                messagebox.showinfo("Info", "Account not found")

        except Exception as e:
            messagebox.showinfo("Info", "Something went wrong")
            print(e)

        finally:
            cur.close()
            con.close()

    def ws(self):
        an = self.wt1.get(1.0, "end")
        an = int(an[0:-1])
        wa = self.wt2.get(1.0, "end")
        wa = int(wa[0:-1])
        try:
            con = pymysql.connect(
                host="localhost", user="root", password="rootroot", db="bank")
            cur = con.cursor()
            if (cur.execute("select name,dob,bal from accounts where an=%s and alive=%s", (an, "yes"))):
                for i in cur:
                    if (cur):
                        l1 = Label(self.wd, text="Name")
                        l1.place(x=150, y=175)
                        l2 = Label(self.wd, text="DOB")
                        l2.place(x=150, y=225)
                        l3 = Label(self.wd, text="Balance")
                        l3.place(x=150, y=275)

                        l4 = Label(self.wd, text=i[0])
                        l4.place(x=250, y=175)
                        l5 = Label(self.wd, text=i[1])
                        l5.place(x=250, y=225)
                        am = i[2]-wa
                        l6 = Label(self.wd, text=i[2]-wa)
                        l6.place(x=250, y=275)
                cur.execute("update accounts set bal=%s where an=%s", (am, an))
                con.commit()
                messagebox.showinfo("Info", "Collect the cash")
            else:
                messagebox.showinfo("Info", "Account not found")

        except Exception as e:
            messagebox.showinfo("Info", "Something went wrong")
            print(e)
        finally:
            cur.close()
            con.close()

    def accopen(self):

        self.ao =Tk()
        self.ao.geometry("500x400+500+200")
        self.ao.title("Account Open")
    # #image setting
    #     can1=Canvas(self.ao,width=500,height=400)
    #     can1.pack()
    #     img1=(Image.open("/Users/kuretimohanasambasiva/Desktop/RSBank/banking/acc_open.png"))
    #     resi1=img1.resize((499,399))
    #     neimg=ImageTk.PhotoImage(resi1)
    #     print("hello")
    #     can1.create_image(10,10,image=neimg,ANCHOR=N)
        
        con = pymysql.connect(host="localhost", user="root",
                              password="rootroot", db="bank")
        cur = con.cursor()
        cur.execute("select max(an) from accounts")
        for i in cur:
            for j in i:
                self.an = j+1
        # Labels
        l1 = Label(self.ao, text="Acc No")
        l1.place(x=100, y=50)
        l2 = Label(self.ao, text="Name")
        l2.place(x=100, y=100)
        l3 = Label(self.ao, text="Address")
        l3.place(x=100, y=150)
        l4 = Label(self.ao, text="Date of Birth")
        l4.place(x=100, y=200)
        l5 = Label(self.ao, text="Amount")
        l5.place(x=100, y=250)
        l6 = Label(self.ao, text=self.an)
        l6.place(x=200, y=50)
        # Button
        b1 = Button(self.ao, text="Sumbit", command=self.accosuc)
        b1.place(x=300, y=325)
        b2 = Button(self.ao, text="Back", command=self.ao.destroy)
        b2.place(x=100, y=325)
        # TextBox
        # self.at1=Text(self.ao,width=20,height=1)
        # self.at1.place(x=200,y=50)
        self.at2 = Text(self.ao, width=20, height=1)
        self.at2.place(x=200, y=100)
        self.at3 = Text(self.ao, width=20, height=1)
        self.at3.place(x=200, y=150)
        self.at4 = Text(self.ao, width=20, height=1)
        self.at4.place(x=200, y=200)
        self.at5 = Text(self.ao, width=20, height=1)
        self.at5.place(x=200, y=250)

        self.ao.mainloop()

    def accosuc(self):

        n = self.at2.get(1.0, "end")
        add = self.at3.get(1.0, "end")
        dob = self.at4.get(1.0, "end")
        amt = self.at5.get(1.0, "end")

        try:
            con = pymysql.connect(
                host="localhost", user="root", password="rootroot", db="bank")
            cur = con.cursor()
            cur.execute("insert into accounts values(%s,%s,%s,%s,%s,%s);",
                        (n, add, dob, amt, self.an, "yes"))
            con.commit()

            self.ao.destroy()
            messagebox.showinfo("Info", "Account opened successfully")

        except Exception as e:
            messagebox.showinfo("Info", "Something went wrong")
            print(e)

        finally:
            cur.close()
            con.close()

    def accsum(self):

        self.am = Tk()
        self.am.geometry("400x300+500+200")
        self.am.title("Account Summary")

        # Button
        b1 = Button(self.am, text="Back", command=self.am.destroy)
        b1.place(x=250, y=250)
        b2 = Button(self.am, text="Display All", command=self.dis)
        b2.place(x=75, y=250)

        self.am.mainloop()

    def dis(self):
        try:
            con = pymysql.connect(
                host="localhost", user="root", password="rootroot", db="bank")
            cur = con.cursor()
            cur.execute("select count(*) from accounts")
            for i in cur:
                for j in i:
                    l1 = Label(self.am, text="Total no. of accounts :")
                    l1.place(x=100, y=50)
                    l4 = Label(self.am, text=j)
                    l4.place(x=250, y=50)
            cur.execute(
                "select count(an) from accounts where alive = "+"'"+"yes"+"'")
            for i in cur:
                for j in i:
                    l2 = Label(self.am, text="No. of alive accounts :")
                    l2.place(x=100, y=100)
                    l5 = Label(self.am, text=j)
                    l5.place(x=250, y=100)
            cur.execute(
                "select count(an) from accounts where alive = "+"'"+"no"+"'")
            for i in cur:
                for j in i:
                    l3 = Label(self.am, text="No. of closed accounts :")
                    l3.place(x=100, y=150)
                    l6 = Label(self.am, text=j)
                    l6.place(x=250, y=150)
        except Exception as e:
            messagebox.showinfo("Info", "Something went wrong")
            print(e)

        finally:
            cur.close()
            con.close()


obj = Bank()
obj.log()