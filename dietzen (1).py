from tkinter import *
import mysql.connector as sql
import math
from tkinter import messagebox
import matplotlib.pyplot as plt
####################################################
root=Tk()
root.title("Diet Zen")
root.geometry("500x500")
root.resizable(False,False)
#root.configure(background="#5a7d9a")
#######################################################
mycon=sql.connect(host="localhost",user="root",password="root",database="CUSTOMER_DETAILS")
mycursor=mycon.cursor()
########################################################
try:
	mycursor.execute("CREATE DATABASE CUSTOMER_LOGIN_DETAILS" )
	mycursor.execute("USE CUSTOMER_LOGIN_DETAILS")
	mycursor.execute("CREATE TABLE LOGIN_DETAILS (User_name VARCHAR(255) PRIMARY KEY,Password VARCHAR(255))")
except:
	mycursor.execute("USE CUSTOMER_LOGIN_DETAILS")
#########################################################
User_name_label=Label(root,text="Username:",font=("times",20,"bold"))
User_name_label.place(x=10,y=95)
Password_label=Label(root,text="Password:",font=("times",20,"bold"))
Password_label.place(x=10,y=175)
User_name_entry=Entry(root,font=("times",15,"bold"),borderwidth=5)
User_name_entry.place(x=140,y=100)
Password_entry=Entry(root,font=("times",15,"bold"),borderwidth=5)
Password_entry.place(x=140,y=180)
##########################################################
def Login():
	root1=Tk()
	root1.title("Diet Zen")
	root1.geometry("400x400")
	root1.resizable(False,False)
	######################################################################
	title_label=Label(root1,text="                  INFO                            ",font=("Helvetica",20),bg="red")
	title_label.grid(row=0,column=0,columnspan=2,pady=10)
	######################################################################
	firstname_label=Label(root1,text="First Name:")
	firstname_label.grid(row=1,column=0,sticky=W,padx=10)

	lastname_label=Label(root1,text="Last Name:")
	lastname_label.grid(row=2,column=0,sticky=W,padx=10)

	Mobile_number_label=Label(root1,text="Mobile number:")
	Mobile_number_label.grid(row=3,column=0,sticky=W,padx=10)

	Email_label=Label(root1,text="Email:")
	Email_label.grid(row=4,column=0,sticky=W,padx=10)

	Gender_label=Label(root1,text="Gender:")
	Gender_label.grid(row=5,column=0,sticky=W,padx=10)

	Age_label=Label(root1,text="Age:")
	Age_label.grid(row=6,column=0,sticky=W,padx=10)

	User_name1_label=Label(root1,text="Username:")
	User_name1_label.grid(row=7,column=0,sticky=W,padx=10)

	Password1_label=Label(root1,text="Password:")
	Password1_label.grid(row=8,column=0,sticky=W,padx=10)

	Weight_label=Label(root1,text="Weight:")
	Weight_label.grid(row=9,column=0,sticky=W,padx=10)

	Height_label=Label(root1,text="Height(in cm):")
	Height_label.grid(row=10,column=0,sticky=W,padx=10)

	firstname_entry=Entry(root1)
	firstname_entry.grid(row=1,column=1)

	lastname_entry=Entry(root1)
	lastname_entry.grid(row=2,column=1,pady=5)

	Mobile_number_entry=Entry(root1)
	Mobile_number_entry.grid(row=3,column=1,pady=5)

	Email_entry=Entry(root1)
	Email_entry.grid(row=4,column=1,pady=5)

	Gender_entry=Entry(root1)
	Gender_entry.grid(row=5,column=1,pady=5)

	Age_entry=Entry(root1)
	Age_entry.grid(row=6,column=1,pady=5)

	User_name1_entry=Entry(root1)
	User_name1_entry.grid(row=7,column=1,pady=5)

	Password1_entry=Entry(root1)
	Password1_entry.grid(row=8,column=1,pady=5)

	Weight_entry=Entry(root1)
	Weight_entry.grid(row=9,column=1,pady=5)

	Height_entry=Entry(root1)
	Height_entry.grid(row=10,column=1,pady=5)


	######################################################
	def BMI():
		root2=Tk()
		root2.title("Diet Zen")
		root2.geometry("300x300")
		root2.resizable(False,False)
		#################################################
		title1_label=Label(root2,text="BODY MASS INDEX     ",font=("Helvetica",20),bg="red")
		title1_label.grid(row=0,column=0,columnspan=2,pady=10)
		##################################################
		Weight_label=Label(root2,text="Weight(in kg):")
		Weight_label.grid(row=1,column=0,sticky=W,padx=10)

		Height_label=Label(root2,text="Height(in cm):")
		Height_label.grid(row=2,column=0,sticky=W,padx=10)

		Weight_entry=Entry(root2)
		Weight_entry.grid(row=1,column=1)

		Height_entry=Entry(root2)
		Height_entry.grid(row=2,column=1,pady=5)
		##################################################

		def cal_bmi():
			if eval(Weight_entry.get())>0 and eval(Height_entry.get())>0:
				HEIGHT_VALUE=eval(Height_entry.get())
				WEIGHT_VALUE=eval(Weight_entry.get())
				BMI_VALUE=round(WEIGHT_VALUE/(HEIGHT_VALUE**2),2)

				BMI_label=Label(root2,text="YOUR BMI IS "+str(BMI_VALUE))
				BMI_label.grid(row=3,column=1)


		BMI_button=Button(root2,text="Calculate BMI",command=cal_bmi)
		BMI_button.grid(row=3,column=0,padx=10,pady=10)

		def GOAL1():
			root3=Tk()
			root3.title("Diet Zen")
			root3.geometry("500x500")
			root3.resizable(False,False)
			#########################################################
			title2_label=Label(root3,text="GOAL                                   ",font=("Helvetica",20),bg="red",width=50)
			title2_label.grid(row=0,column=0,columnspan=2,pady=10)
			#########################################################
			goal_label=Label(root3,text="What is your goal?",font=("times",15))
			goal_label.place(x=170,y=50)
			###########################################################
			def typeofdiet():
				root6=Tk()
				root6.geometry("1000x700")
				root6.title("Diet Zen")
				root6.resizable(False,False)
				##################################################################
				Name=User_name_entry.get()
				title3_label=Label(root6,text="Welcome  "+Name,font=("Helvetica",20))
				title3_label.grid(row=0,column=0,columnspan=2,pady=10)
				################################################################
				title32_label=Label(root6,text="Today's Goal",font=("Helvetica",20))
				title32_label.grid(row=1,column=0,sticky=W)

				w=Weight_entry.get()
				h=Height_entry.get()
				gender=Gender_entry.get()
				age=Age_entry.get()
				if (gender=="M" or gender=="Male" or gender=="m"):
					BMR=(10*eval(w))+(6.25*eval(h))-(5*eval(age))+5
				if (gender=="F" or gender=="Female" or gender=="f"):
					BMR=(10*eval(w))+(6.25*eval(h))-(5*eval(age))-161
				Calorie=BMR-300
				Protein=2.2*eval(w)
				Fat=0.2*Calorie
				L=["Calorie","Protein","Fat"]
				L1=[Calorie,Protein,Fat]


			lose_fat=Button(root3,text="Lose fat",font=("times",15),width=40,height=3,command=typeofdiet)
			lose_fat.place(x=20,y=100)

			def typeofdiet1():
				root6=Tk()
				root6.geometry("1000x700")
				root6.title("Diet Zen")
				root6.resizable(False,False)
				##################################################################
				Name=User_name_entry.get()
				title3_label=Label(root6,text="Welcome  "+Name,font=("Helvetica",20))
				title3_label.grid(row=0,column=0,columnspan=2,pady=10)
				################################################################
				title32_label=Label(root6,text="Today's Goal",font=("Helvetica",20))
				title32_label.grid(row=1,column=0,sticky=W)

				w=Weight_entry.get()
				h=Height_entry.get()
				gender=Gender_entry.get()
				age=Age_entry.get()
				if (gender=="M" or gender=="Male" or gender=="m"):
					BMR=(10*eval(w))+(6.25*eval(h))-(5*eval(age))+5
				if (gender=="F" or gender=="Female" or gender=="f"):
					BMR=(10*eval(w))+(6.25*eval(h))-(5*eval(age))-161

				Calorie=eval(BMR)
				Protein=0.8*eval(w)
				Fat=0.2*eval(Calorie)
				L=["Calorie","Protein","Fat"]
				L1=[Calorie,Protein,Fat]

			Maintain_weight=Button(root3,text="Maintain weight",font=("times",15),width=40,height=3,command=typeofdiet1)
			Maintain_weight.place(x=20,y=220)

			def typeofdiet2():
				root6=Tk()
				root6.geometry("1000x700")
				root6.title("Diet Zen")
				root6.resizable(False,False)
				##################################################################
				Name=User_name_entry.get()
				title3_label=Label(root6,text="Welcome  "+Name,font=("Helvetica",20))
				title3_label.grid(row=0,column=0,columnspan=2,pady=10)
				################################################################
				title32_label=Label(root6,text="Today's Goal",font=("Helvetica",20))
				title32_label.grid(row=1,column=0,sticky=W)

				w=Weight_entry.get()
				h=Height_entry.get()
				gender=Gender_entry.get()
				age=Age_entry.get()
				if (gender=="M" or gender=="Male" or gender=="m"):
					BMR=(10*eval(w))+(6.25*eval(h))-(5*eval(age))+5
				if (gender=="F" or gender=="Female" or gender=="f"):
					BMR=(10*eval(w))+(6.25*eval(h))-(5*eval(age))-161

				Calorie=eval(BMR)+600
				Protein=1.5*eval(w)
				Fat=0.3*eval(Calorie)
				L=["Calorie","Protein","Fat"]
				L1=[Calorie,Protein,Fat]

			Build_muscle=Button(root3,text="Build muscle",font=("times",15),width=40,height=3,command=typeofdiet2)
			Build_muscle.place(x=20,y=340)
		####################################################################
		Next1_button=Button(root2,text="Next",command=GOAL1)
		Next1_button.place(x=150,y=120)
	def add_customer():
			mycursor.execute("USE CUSTOMER_DETAILS")
			sql_command="INSERT INTO INFO (First_name,Last_name,Mobile_no,email_adress,gender,age,Weight,Height,user_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
			values=(firstname_entry.get(),lastname_entry.get(),Mobile_number_entry.get(),Email_entry.get(),Gender_entry.get(),int(Age_entry.get()),int(Weight_entry.get()),int(Height_entry.get()),User_name1_entry.get())
			mycursor.execute(sql_command,values)
			mycon.commit()
			mycursor.execute("USE CUSTOMER_LOGIN_DETAILS")
			sql_command1="INSERT INTO LOGIN_DETAILS (User_name,Password) VALUES (%s,%s)"
			values1=(User_name1_entry.get(),Password1_entry.get())
			mycursor.execute(sql_command1,values1)
			mycon.commit()
			firstname_entry.delete(0,END)
			lastname_entry.delete(0,END)
			Mobile_number_entry.delete(0,END)
			Email_entry.delete(0,END)
			Gender_entry.delete(0,END)
			Age_entry.delete(0,END)
			User_name1_entry.delete(0,END)
			Password1_entry.delete(0,END)
			Weight_entry.delete(0,END)
			Height_entry.delete(0,END)
			root3=Tk()
			root3.title("Diet Zen")
			root3.geometry("500x500")
			root3.resizable(False,False)
			#########################################################
			title2_label=Label(root3,text="GOAL",font=("Helvetica",20))
			title2_label.grid(row=0,column=0,columnspan=2,pady=10)

			###########################################################
			goal_label=Label(root3,text="What is your goal?",font=("times",15))
			goal_label.place(x=170,y=50)
			###########################################################
			lose_fat=Button(root3,text="Lose fat",font=("times",15),width=40,height=3)
			lose_fat.place(x=20,y=100)

			Maintain_weight=Button(root3,text="Maintain weight",font=("times",15),width=40,height=3)
			Maintain_weight.place(x=20,y=220)

			Build_muscle=Button(root3,text="Build muscle",font=("times",15),width=40,height=3)
			Build_muscle.place(x=20,y=340)
	Next_button=Button(root1,text="Next",command=add_customer)
	Next_button.grid(row=11,column=0 ,padx=10,pady=10 )

	bmi_button=Button(root1,text="BMI",command=BMI)
	bmi_button.grid(row=11,column=1)	
##########################################################
def Login1():
	mycursor.execute("USE CUSTOMER_LOGIN_DETAILS")
	mycursor.execute("SELECT * FROM LOGIN_DETAILS")
	data=mycursor.fetchall()
	t=(User_name_entry.get(),Password_entry.get())
	for i in data:
		if t==i:
			root5=Tk()
			root5.title("Diet Zen")
			root5.geometry("500x500")
			root5.resizable(False,False)
			#########################################################
			title2_label=Label(root5,text="GOAL                                   ",font=("Helvetica",20),bg="red",width=50)
			title2_label.grid(row=0,column=0,columnspan=2,pady=10)
			#########################################################
			goal_label=Label(root5,text="What is your goal?",font=("times",15))
			goal_label.place(x=170,y=50)
			############################################################

			def Welcome():
				root6=Tk()
				root6.geometry("1000x700")
				root6.title("Diet Zen")
				root6.resizable(False,False)
				##################################################################
				Name=User_name_entry.get()
				title3_label=Label(root6,text="Welcome  "+Name,font=("Helvetica",20))
				title3_label.grid(row=0,column=0,columnspan=2,pady=10)
				################################################################
				title32_label=Label(root6,text="Today's Goal",font=("Helvetica",20))
				title32_label.grid(row=1,column=0,sticky=W)

				sql1="SELECT Weight,Height,Gender,Age FROM INFO WHERE user_name=%s"
				value1=User_name_entry.get()
				mycursor.execute(sql1,value1)
				data=mycursor.fetchall()
				w,h,gender,age=data
				if (gender=="M" or gender=="Male" or gender=="m"):
					BMR=(10*eval(w))+(6.25*eval(h))-(5*eval(age))+5
				if (gender=="F" or gender=="Female" or gender=="f"):
					BMR=(10*eval(w))+(6.25*eval(h))-(5*eval(age))-161
				Calorie=BMR-300
				Protein=2.2*eval(w)
				Fat=0.2*Calorie
				L=["Calorie","Protein","Fat"]
				L1=[Calorie,Protein,Fat]


			lose_fat=Button(root5,text="Lose fat",font=("times",15),width=40,height=3,command=Welcome)
			lose_fat.place(x=20,y=100)

			def Welcome1():
				root6=Tk()
				root6.geometry("1000x700")
				root6.title("Diet Zen")
				root6.resizable(False,False)
				##################################################################
				Name=User_name_entry.get()
				title3_label=Label(root6,text="Welcome  "+Name,font=("Helvetica",20))
				title3_label.grid(row=0,column=0,columnspan=2,pady=10)
				################################################################
				title32_label=Label(root6,text="Today's Goal",font=("Helvetica",20))
				title32_label.grid(row=1,column=0,sticky=W)
				sql1="SELECT Weight,Height,Gender,Age FROM INFO WHERE user_name=%s"
				value1=User_name_entry.get()
				mycursor.execute(sql1,value1)
				data=mycursor.fetchall()
				w,h,gender,age=data
				if (gender=="M" or gender=="Male" or gender=="m"):
					BMR=(10*eval(w))+(6.25*eval(h))-(5*eval(age))+5
				if (gender=="F" or gender=="Female" or gender=="f"):
					BMR=(10*eval(w))+(6.25*eval(h))-(5*eval(age))-161

				Calorie=eval(BMR)
				Protein=0.8*eval(w)
				Fat=0.2*eval(Calorie)
				L=["Calorie","Protein","Fat"]
				L1=[Calorie,Protein,Fat]


			Maintain_weight=Button(root5,text="Maintain weight",font=("times",15),width=40,height=3,command=Welcome1)
			Maintain_weight.place(x=20,y=220)

			def Welcome2():
				root6=Tk()
				root6.geometry("1000x700")
				root6.title("Diet Zen")
				root6.resizable(False,False)
				##################################################################
				Name=User_name_entry.get()
				title3_label=Label(root6,text="Welcome  "+Name,font=("Helvetica",20))
				title3_label.grid(row=0,column=0,columnspan=2,pady=10)
				################################################################
				title32_label=Label(root6,text="Today's Goal",font=("Helvetica",20))
				title32_label.grid(row=1,column=0,sticky=W)
				sql1="SELECT Weight,Height,Gender,Age FROM INFO WHERE user_name=%s"
				value1=User_name_entry.get()
				mycursor.execute(sql1,value1)
				data=mycursor.fetchall()
				w,h,gender,age=data
				if (gender=="M" or gender=="Male" or gender=="m"):
					BMR=(10*eval(w))+(6.25*eval(h))-(5*eval(age))+5
				if (gender=="F" or gender=="Female" or gender=="f"):
					BMR=(10*eval(w))+(6.25*eval(h))-(5*eval(age))-161

				Calorie=eval(BMR)+600
				Protein=1.5*eval(w)
				Fat=0.3*eval(Calorie)
				L=["Calorie","Protein","Fat"]
				L1=[Calorie,Protein,Fat]

			Build_muscle=Button(root5,text="Build muscle",font=("times",15),width=40,height=3,command=Welcome2)
			Build_muscle.place(x=20,y=340)
			break
		elif t[0]==i[0] and t[1]!=i[1]:
			messagebox.showerror("Error","Invalid Password")
			break

	else:
		messagebox.showerror("Error","Invalid Username and Password")
Login_Button=Button(root,text="Login",font=("times",20,"bold"),width=10,borderwidth=5,bg="grey",command=Login1)
Login_Button.place(x=160,y=250)
#############################################################
Newuser_label=Label(root,text="New user?",font=("times",15,"bold"))
Newuser_label.place(x=160,y=320)
##############################################################
Signup_Button=Button(root,text="Sign Up",font=("times",15,"bold"),width=0,borderwidth=0,fg="green",command=Login)
Signup_Button.place(x=250,y=317)
#####################################
root.mainloop()