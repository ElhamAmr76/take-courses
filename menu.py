import register
from HandleFile import HandleFile
from accesses import Access
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
            


#--------------------------------------primary menu----------------------------------------------#
while True: #change try position
    try:
        print("",           #make a menu for user
            "Wellcome, please choose one:",
            "1. register",
            "2. login in",
            "3. exit", sep="\n")
        choice = read_choice(0, 3)
#_______________________________________register choice__________________________________________________#
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
                
                elif user=="teacher":                          #save teacher information in a csv file use register module
                    username=input("username:")
                    password=input("password:")

                    sample=register.Employee(user,username,password)
                    register.Teacher.saving(sample)
                else:
                    raise Exception("sorry! You can not have an account")


                    
 #____________________________________________________login choice________________________________________________#               
                
            elif choice == 2:   #login part
                
                User = input("Choose your use (student/employee/teacher): ").lower()
#________________________________________________login for student____________________________________________#

                if User == "student":
                    username = input("Enter your username: ")
                    password = input("Enter your Password: ")
                    with open('users_information.csv','r') as file:  #read information and let user to login
                        filereader = csv.DictReader(file)
                        for i in filereader:
                            if username in i['username'] and sha256(str(password).encode()).hexdigest() in i['password']: # username in file2 and password in file2:
                                if i['user'] == 'student':      #make hased password
                                    logging.info(f"{username} is register")         #show every info error
                                    os.system('cls')
                                else:
                                    pass
#________________________________________________accesses for student____________________________________________#
#                                 
                    print("",                       #seconed menu from person accesses
                                        "1. units list",
                                        "2. search units",
                                        "3. take units",
                                        "4. list of select units",
                                        "5. exit", sep="\n")
                    choice=input("Enter a number:")
                    if choice=="1":     #read the file that we made before by units
                    #     with open('lesson_file.csv','r') as file:
                    #         reader = csv.DictReader(file)
                    #         for i in reader:
                    #             print(i)
                        Access.units_list()

                    elif choice=="2":       #search by name of lesson and read the file
                        # lesson=input("which lesson?")
                        # with open('lesson_file.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         if lesson in i['lesson']:
                        #             print(i)

                        Access.search()
                    elif choice=="3":
                        Access.student_take_course
                        # selected_file = HandleFile('selected_units_by_student.csv')
                        # lesson_name=input("the lesson that you want to choose: ")
                        # teacher_name=input("teacher of that lesson: ") 
                        # with open('lesson_file.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         if lesson_name in i['lesson']:
                        #             if teacher_name in i["teacher"]:
                        #                 selected_file.append_info_user(i)
                        #                 with open('lesson_file.csv','r') as file:
                        #                     reader = csv.DictReader(file)
                        #                     for i in reader:
                        #                         if lesson_name in i['lesson']:
                        #                            i["remain_capacity"]-=1#make it int
                        #             else:
                        #                 print(f"this lesson just offered by {i[teacher]}")
                        #         else:
                        #             print("choose from the list!")


                                         
                    elif choice=="4":       
                        Access.selected_unit_list_student()

                        # with open('selected_units_by_student.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         print(i)

                            # sum=0
                            # for i in reader:
                            #     if i["unit_number"]:
                            #         sum+=int(i["unit_number"])
                            #     print(sum)
                    
                   

#________________________________________________login for employee____________________________________________#
                elif User == 'employee':
                    username = input("Enter your username: ")
                    password = input("Enter your Password: ")
                    with open('users_information.csv','r') as file:
                        filereader = csv.DictReader(file, delimiter=',')
                        for i in filereader:
                            if username in i['username'] and password in i['password']:
                                logging.info(f"{username} is register")

#________________________________________________accesses for employee____________________________________________#
                
                    print("",
                            "1. units_list",
                            "2. search_units",
                            "3. all_units",
                            "4. define unit",
                            "5. student list for a special unit",
                            "6. student list",
                            "7. search student",
                            "8. search select units by student",
                            "9. accept take course",
                            "10. exit", sep="\n")
                    choice=input("Enter a number:")
                    if choice=="1":#read the file that we made before by units
                        Access.units_list()
                        # with open('lesson_file.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         print(i)
                    elif choice=="2":
                        Access.search()
                        # lesson=input("which lesson?") #search by name of lesson and read the file
                        # with open('lesson_file.csv','r') as file:    #function#make ex
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         if lesson in i['lesson']:
                        #             print(i["lesson"],i["teacher"])
                            
                    elif choice=="3":   #can see the sum of units of lesson
                        Access.all_unit()                        # with open('lesson_file.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     sum=0
                        #     for i in reader:
                        #         if i["unit_number"]:
                        #             sum+=int(i["unit_number"])
                        #         print(sum)
                    elif choice=="4":   #define a lesson and add to file from register module
                        Access.define_unit()
                        # lesson=input("lesson: ")
                        # unit_num=input("unit_num: ")
                        # Total_capacity=input("Total_capacity: ")
                        # remain_capacity=input(" remain capacity: ")
                        # teacher=input("teacher: ")
                                    
                        # variable=Units.Units(lesson,unit_num,Total_capacity,remain_capacity,teacher)
                        # Units.Units.save(variable)
                    elif choice=="5":       #can see the sum of units of lesson
                        Access.student_list_for_a_special_unit()
                        # student_lesson=input("watch list of students who picked up this lesson: ")
                        # with open('selected_units_by_student.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         if student_lesson==i["lesson"]:
                        #             print(i["user_name"])
                    elif choice=="6":
                        Access.student_list()
                        # with open('users_information.csv','r') as file:
                        #     filereader = csv.DictReader(file)
                        #     for i in filereader:
                        #         print(i["student"])
                    elif choice == "7":
                        Access.search_student()
                        # student_name=input("username? ") #search by name of lesson and read the file
                        # with open('users_information.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         if student_name in i['username']:
                        #             print(i)
                    elif choice=="8":
                        Access.search_select_units_by_student()
                        
                        # student_name=input("user name?") #search by name of lesson and read the file
                        # with open('lesson_file.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         if student_name in i['user_name']:
                        #             print(i["lesson"])
                    elif choice=="9":
                        Access.accept_take_course()
                        # with open('lesson_file.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     with open('selected_units_by_student.csv','r') as sec_file:
                        #         reader2 = csv.DictReader(sec_file)

                        #         for i in reader2:
                        #             print(i)
                        #             Input=input( "Accept/Reject ")
                        #             if Input=="Accept".lower():
                        #                 continue
                        #             else:
                        #                 for j in reader:
                        #                     if i["lesson"]==j["lesson"]:
                        #                          i["remain_capacity"]+=1
                                                
                    else:
                        sys.exit()

#________________________________________________login for teacher____________________________________________#
                if User == "teacher":
                    username = input("Enter your username: ")
                    password = input("Enter your Password: ")
                    with open('users_information.csv','r') as file:  #read information and let user to login
                        filereader = csv.DictReader(file)
                        for i in filereader:
                            if username in i['username'] and sha256(str(password).encode()).hexdigest() in i['password']: # username in file2 and password in file2:
                                if i['user'] == 'teacher':      #make hased password
                                    logging.info(f"{username} is register")         #show every info error
                                    os.system('cls')
                                else:
                                    pass 

 #________________________________________________accesses for teacher____________________________________________#
                               
                    print("",
                            "1. units_list",
                            "2. search_units",
                            "3. take units",
                            "4. list of select units",
                            "5. student list for a special unit"
                            "6. exit", sep="\n")
                    choice=input("Enter a number:")
                    if choice=="1":#read the file that we made before by units
                        Access.units_list()
                        # with open('lesson_file.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         print(i)
                    elif choice=="2":
                        Access.search()
                        # lesson=input("which lesson?") #search by name of lesson and read the file
                        # with open('lesson_file.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         if lesson in i['lesson']:
                        #             print(i)
                            
                    elif choice=="3":   #can see the sum of units of lesson
                        Access.take_units_teacher()
                        # selected_file = HandleFile('selected_units_by_teacher.csv')
                        # lesson_name=input("the lesson that you want to choose: ")
                        # with open('lesson_file.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         if lesson_name in i['lesson']:
                        #            selected_file.append_info_user(i)
                        #            with open('lesson_file.csv','r') as file:
                        #                     reader = csv.DictReader(file)
                        #                     for i in reader:
                        #                         if lesson_name in i['lesson']:
                        #                             reader.pop(i)
                    elif choice=="4":   
                        Access.list_of_select_units()    
                        # with open('selected_units_by_teacher.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         print(i)

                    elif choice=="5":    
                        Access.student_list_for_a_special_unit() 
                        # student_lesson=input("watch list of students who picked up this lesson: ")
                        # with open('selected_units_by_student.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     for i in reader:
                        #         if student_lesson==i["lesson"]:
                        #             print(i)





                        # with open('lesson_file.csv','r') as file:
                        #     reader = csv.DictReader(file)
                        #     sum=0
                        #     for i in reader:
                        #         if i["unit_number"]:
                        #             sum+=int(i["unit_number"])
                        #         print(sum)
                    # elif choice=="4":   #define a lesson and add to file from register module
                    #     lesson=input("lesson: ")
                    #     unit_num=input("unit_num: ")
                    #     Total_capacity=input("Total_capacity: ")
                    #     remain_capacity=input(" remain capacity: ")
                    #     teacher=input("teacher: ") 
                                    
                        # variable=Units.Units(lesson,unit_num,Total_capacity,remain_capacity,teacher)
                        # Units.Units.save(variable)

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
                        
                