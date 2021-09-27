import register
import Units
import logging
import os
import sys      
import csv      #for using files
from hashlib import sha256      #for make hpassword hash
#from tkinter import *
#root=Tk()
#root.geometry("500x300")

    
def read_choice(start, stop):
    try:
        choice = int(input(":"))
    except ValueError:
        print("wrong input!")
    else:
        if start <= choice <= stop:
            return choice
        else:
            print("wrong choice.")
            

try:
    while True:
        print("",           #make a menu for user
            "Wellcome, please choose one:",
            "1. register",
            "2. login in",
            "3. exit", sep="\n")
        choice = read_choice(0, 3)
        if choice:
            if choice == 1:         #register part for employee and student
                user=input("user: ")
                if user=="student":
                    username=input("username:")
                    password=input("password:")

                    sample=register.Student(user,username,password) #save student information in a csv file use register module
                    register.Student.saving(sample)

                elif user=="employee":                          #save employee information in a csv file use register module
                    username=input("username:")
                    password=input("password:")

                    sample=register.Employee(user,username,password)
                    register.Employee.saving(sample)

                    
                
                
            elif choice == 2:   #login part
                
                User = input("Choose your use (student/employee): ").lower()
                if User == "student":
                    username = input("Enter your username: ")
                    password = input("Enter your Password: ")
                    with open('user_information.csv','r') as file:  #read information and let user to login
                        filereader = csv.DictReader(file)
                        for i in filereader:
                            if username in i['username'] and sha256(str(password).encode()).hexdigest() in i['password']: # username in file2 and password in file2:
                                if i['role'] == 'student':      #make hased password
                                    logging.info(f"{username} is register")         #show every info error
                                    os.system('cls')
                                else:
                                    pass
                    print("",                       #accesses
                                        "1. units_list",
                                        "2. search_units",
                                        "3. all_units",
                                        "4. exit", sep="\n")
                    choice=input("Enter a number:")
                    if choice=="1":     #read the file that we made before by units
                        with open('lesson_file.csv','r') as file:
                            reader = csv.DictReader(file)
                            for i in reader:
                                print(i)
                    elif choice=="2":       #search by name of lesson and read the file
                        lesson=input("which lesson?")
                        with open('lesson_file.csv','r') as file:
                            reader = csv.DictReader(file)
                            for i in reader:
                                if lesson in i['lesson']:
                                    print(i)
                    elif choice=="3":       #can see the sum of units of lesson
                        with open('lesson_file.csv','r') as file:
                            reader = csv.DictReader(file)
                            sum=0
                            for i in reader:
                                if i["unit_number"]:
                                    sum+=int(i["unit_number"])
                                print(sum)
                    
                    else:
                        sys.exit()

                elif User == 'employee':
                    username = input("Enter your username: ")
                    password = input("Enter your Password: ")
                    with open('user_information.csv','r') as file:
                        filereader = csv.DictReader(file, delimiter=',')
                        for i in filereader:
                            if username in i['username'] and password in i['password']:
                                logging.info(f"{username} is register")
                    print("",
                            "1. units_list",
                            "2. search_units",
                            "3. all_units",
                            "4. define unit",
                            "5. exit", sep="\n")
                    choice=input("Enter a number:")
                    if choice=="1":#read the file that we made before by units
                        with open('lesson_file.csv','r') as file:
                            reader = csv.DictReader(file)
                            for i in reader:
                                print(i)
                    elif choice=="2":
                        lesson=input("which lesson?") #search by name of lesson and read the file
                        with open('lesson_file.csv','r') as file:
                            reader = csv.DictReader(file)
                            for i in reader:
                                if lesson in i['lesson']:
                                    print(i)
                            
                    elif choice=="3":   #can see the sum of units of lesson
                        with open('lesson_file.csv','r') as file:
                            reader = csv.DictReader(file)
                            sum=0
                            for i in reader:
                                if i["unit_number"]:
                                    sum+=int(i["unit_number"])
                                print(sum)
                    elif choice=="4":   #define a lesson and add to file from register module
                        lesson=input("lesson: ")
                        unit_num=input("unit_num: ")
                        Total_capacity=input("Total_capacity: ")
                        remain_capacity=input(" remain capacity: ")
                        teacher=input("teacher: ")
                                    
                        variable=Units.Units(lesson,unit_num,Total_capacity,remain_capacity,teacher)
                        Units.Units.save(variable)

                    else:
                        sys.exit()
except Exception as e:  #show all exception about value error , type error , syntax error ,...
    print(e)
# Label(root,text="register",font="times 15 bold").grid(row=0,column=3)
# user=Label(root,text="user")
# user.grid(row=1,column=2)
# username=Label(root,text="username")
# username.grid(row=2,column=2)
# password=Label(root,text="password")
# password.grid(row=3,column=2)
# confirm_password=Label(root,text="confirm password")
# confirm_password.grid(row=4,column=2)
# user_value=StringVar
# username_value=StringVar
# password_value=IntVar
# confirm_password_value=IntVar
# user_box=Entry(root,textvariable=user_value)
# user_box.grid(row=1,column=3)
# username_box=Entry(root,textvariable=username_value)
# username_box.grid(row=2,column=3)
# password_box=Entry(root,textvariable=password_value)
# password_box.grid(row=3,column=3)
# confirm_password_box=Entry(root,textvariable=confirm_password_value)
# confirm_password_box.grid(row=4,column=3)
# Button(text="submit",command=Student.saving).grid(row=7,column=3)
# root.mainloop()
                        
                