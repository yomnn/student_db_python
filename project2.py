from student_text import enter_stds
from student_text import read_stds
from student_text import write_stds

def print_stds():
    stds=read_stds()
    for std in stds:
        std_info = std.split()
        print("First Name:",std_info[0],"Last Name:",std_info[1],"Term:", std_info[2],"GPA:", std_info[3], "Student ID: ", std_info[4])  
    
def search_stds():
    std_id = input("Enter Student's ID: ")
    stds = read_stds()
    for std in stds:
        std_info = std.split()
        if std_info[4] == std_id:  
            return "found", std
    return "not found",None

def remove_stds(std_id):
    stds=read_stds()
    for std in stds:
        std_info = std.split()
        if std_info[4] == std_id:
            stds.remove(std)
            write_stds(opt= "w" , empty = 1)
            for std in stds:
                write_stds(std)
    return "removed"

def update_stds():
    opt_update = input("Enter:\n1-For updating Term \n2-For updating GPA \n")
    search_result , std = search_stds()
    if opt_update == "1":
        if search_result == "found":
            term = input("Enter Term: ")
            std=std.split()
            new_std= std.copy()
            new_std[2]=term
            remove_stds(std[4])
            new_std = " ".join(new_std)
            write_stds(new_std)
            return new_std
        else:
            return "not found"

    elif opt_update == "2":
        if search_result == "found":
            term = input("Enter GPA: ")
            new_std= std.copy()
            new_std[3]=term
            remove_stds(std[4])
            new_std = " ".join(new_std)
            write_stds(new_std)
            return new_std
        else:
            return "not found"


def sort_stds():
    opt_sort = input("Enter \n1- From a to z \n2- From z to a")
    stds= read_stds()
    
    if opt_sort == "1":
        sorted_list = sorted(stds , reverse = False)

    elif opt_sort == "2":
        sorted_list = sorted(stds , reverse = True)

    return sorted_list
        
        
        
        
        
        
    
        
        


while True:
    opt=input("1-enter new std 2-print all 3-search 4-remove 5-update 6-sort or done to exit:").lower()
    if opt=="done":
        break
    elif opt=="1":
        while True:
            std_info = enter_stds()
            if std_info == "done":
                print("Done !")
                break
            elif std_info != "Error":
                write_stds(std_info)
                print("Student added succesfully.\n\n\n")
            else:
                print("Data inserted is invalid !")

    elif opt=="2":
        print_stds()


    elif opt=="3":
        result , std = search_stds()
        if result == "not found":
            print("Student not found !")
        else:
            print("Student found Sucessfullly\n\n\n")
            std_info= std.split()
            print("First Name:",std_info[0],"Last Name:",std_info[1],"Term:", std_info[2],"GPA:", std_info[3], "Student ID: ", std_info[4])

    elif opt=="4":
        result , std = search_stds()
        if result == "found":
            remove_stds(std.split()[4])
            print("Removed Successfully")
        else:
            print("Student not found !")


    elif opt=="5":
        update_result = update_stds()
        if update_result == "not found":
            print("Error: Student not found")
        else:
            print(update_result , "\n\nStudent updated successfully")
            
            
        
    elif opt=="6":
        stds = sort_stds()
        for std in stds:
            std_info = std.split()
            print("First Name:",std_info[0],"Last Name:",std_info[1],"Term:", std_info[2],"GPA:", std_info[3], "Student ID: ", std_info[4])   
    
