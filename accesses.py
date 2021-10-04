import csv
from os import access
from HandleFile import HandleFile
import Units

class Access:
    lesson_file = HandleFile('lesson_file.csv') 
    reader1=HandleFile.read_info(lesson_file)
    select_by_student = HandleFile('selected_units_by_student.csv')
    reader2=HandleFile.read_info(select_by_student)
    unit_info = HandleFile('users_information.csv')
    reader3=HandleFile.read_info(unit_info)
    select_by_teacher = HandleFile('selected_units_by_teacher.csv')
    reader4=HandleFile.read_info(select_by_teacher)
    user_info=HandleFile("users_information.csv")
    reader5=HandleFile.read_info(user_info)

    
    def units_list():
        for i in Access.reader1:
            print(i)
    def search():
        lesson=input("which lesson?")
        for i in Access.reader1:
            if lesson in i['lesson']:
                print(i)
    def student_take_course():

        
        lesson_name=input("the lesson that you want to choose: ")
        teacher_name=input("teacher of that lesson: ") 
                        
        for i in Access.reader1:
            if lesson_name in i['lesson']:
                if teacher_name in i["teacher"]:
                    Access.select_by_student.append_info_user(i)
                                        
                    for i in Access.reader1:
                        if lesson_name in i['lesson']:
                            i["remain_capacity"]-=1#make it int
                        else:
                            print(f"this lesson just offered by {i[teacher]}")
                    else:
                            print("choose from the list!")
    def selected_unit_list_student():
        
        for i in Access.reader2:
            print(i)
    def all_unit():
        sum=0
        for i in Access.reader1:
            if i["unit_number"]:
                sum+=int(i["unit_number"])
                print(sum)
    def define_unit():
        lesson=input("lesson: ")
        unit_num=input("unit_num: ")
        Total_capacity=input("Total_capacity: ")
        remain_capacity=input(" remain capacity: ")
        teacher=input("teacher: ")
                                    
        variable=Units.Units(lesson,unit_num,Total_capacity,remain_capacity,teacher)
        Units.Units.save(variable)
    def student_list_for_a_special_unit():
        student_lesson=input("watch list of students who picked up this lesson: ")
                        
        for i in Access.reader2:
            if student_lesson==i["lesson"]:
                print(i["user_name"])
    def student_list():
        
            for i in Access.reader5:
                print(i["student"])
    def search_student():
        student_name=input("username? ") #search by name of lesson and read the file
        
        for i in Access.reader5:
            if student_name in i['username']:
                print(i)
    def search_select_units_by_student():
        
        student_name=input("user name?") #search by name of lesson and read the file
        
        for i in Access.reader1:
            if student_name in i['user_name']:
                print(i["lesson"])
    def accept_take_course():
        
        for i in Access.reader2:
            print(i)
            Input=input( "Accept/Reject ")
            if Input=="Accept".lower():
                continue
            else:
                for j in Access.reader1:
                    if i["lesson"]==j["lesson"]:
                            i["remain_capacity"]+=1
    def take_units_teacher():
        
        lesson_name=input("the lesson that you want to choose: ")
        
        for i in Access.reader1:
            if lesson_name in i['lesson']:
                Access.select_by_teacher.append_info_user(i)
                
                for i in Access.reader1:
                    if lesson_name in i['lesson']:
                        Access.reader1.pop(i)
    def list_of_select_units():
        
        for i in Access.reader4:
            print(i)


                                    