import csv
import HandleFile
class Units:
    save_info=HandleFile.HandleFile("lesson_file.csv")  #use Handlefile module to write read and append to file
    
    def __init__(self,lesson,unit_number,Total_capacity,remain_capacity,teacher):  #define and add lesson to a file
        self.lesson=lesson
        self.unit_number=unit_number
        self.Total_capacity=int(Total_capacity)
        self.remain_capacity=int(remain_capacity)
        self.teacher=teacher
        
    def save(self): #append to file by this method
        self.save_info.append_info_user(self.__dict__)
   

                


