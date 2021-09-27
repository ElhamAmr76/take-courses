import csv

class HandleFile :
    def __init__ (self, file_path):
        self.file_path = file_path

    def read_info (self):
        with open (self.file_path, 'r') as read_file :
            readerdict = csv.DictReader(read_file)
            return(list(readerdict))


    def write_info_user (self, new_value):
    # check this new value is dict or list of dict
        if isinstance (new_value, dict):
            field = new_value.keys()
            new_value = [new_value]
        elif isinstance(new_value, list):
            field = new_value[0].keys()

        with open (self.file_path, 'w') as f_append :  # this part helps if the file is full the info is not appened agian 
            write = csv.DictWriter(f_append, fieldnames= field)
            # check just put header top of the file 
            if f_append.tell() == 0:
                write.writeheader()
            write.writerows(new_value)  # <===
                

    def append_info_user (self, new_value):
        # check this new value is dict or list of dict
        if isinstance (new_value, dict):
            field = new_value.keys()
            new_value = [new_value]
        elif isinstance(new_value, list):
            field = new_value[0].keys()

        with open (self.file_path, 'a') as f_append :
            write = csv.DictWriter(f_append, fieldnames= field)
            # check just put header top of the file 
            if f_append.tell() == 0:
                write.writeheader()
            write.writerows(new_value)
            



