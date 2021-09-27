
#from tkinter import *
#import logging
#import os
import HandleFile
import csv
from hashlib import sha256
#root=Tk()
#root.geometry("500x300")
class Student:
    file_variable = HandleFile.HandleFile('user_information.csv')#use Handlefile module to write read and append to file
    def __init__(self,user,username,password):#make a file for store users information
        self.user = user
        self.username=self.validation_name(username)
        self.password=self.validation_pasword(password)
        

    def validation_pasword(self,password):      #check valid of password, it shpuld be more than 8 character
        if password.isdigit() and len(password) >= 8:
            confirm_password = input("confirm password :")
            while confirm_password != password:         #use confirm password and check for being match with password
                confirm_password = input("not match\ntry again :")
            return sha256(str(confirm_password).encode()).hexdigest()    #hashing password
        else:
            print("invalid password")
    def validation_name(self,name): #check for exist name and should use just alphabet for username
        if name.isalpha() :
            with open('user_information.csv','r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if name not in i['username']:
                        return name
                    else:
                        print("Duplicate name")
                else:
                    return name
        else:
            print("invalid username")

    def saving (self):
        self.file_variable.append_info_user(self.__dict__)  #save every got info and append to csv file

        
class Employee(Student):
    idfc = HandleFile.HandleFile('user_information.csv')        #use Handlefile module to write read and append to file
    def __init__(self,user, username, password):                #make a file for store users information
        super().__init__(user, username, password)
       
    def saving (self):
        self.idfc.append_info_user(self.__dict__)
    
    

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


# a = Employee("employee","amiri","4580301277")
# a.saving()


# a = Student("student","elham","4580275608")
# a.saving()