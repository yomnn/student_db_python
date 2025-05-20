def read_stds ():
    hand = open("std_list.txt" , "r")
    stds = hand.read().strip().split("\n")
    hand.close()
    return stds


def write_stds(std_info="" , opt="a" , empty=0):
    hand=open("std_list.txt" , opt)
    if empty == 0:
        hand.write(std_info+"\n")
    hand.close()
        

def enter_stds():
    std_info=input("Enter FN LN Term GPA ID:\nOr done to quit:\n").lower()
    if len(std_info.split()) == 5:
        return std_info
    elif std_info == "done":
        return "done"
    else:
        return "Error"


    
"""

std_info = enter_stds()
if std_info != "Error":
    write_stds(std_info)
    print("Student added succesfully.")
else:
    print("Data inserted is invalid !")
stds = read_stds()
print(stds)


"""
        

    
