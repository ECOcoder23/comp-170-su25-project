from MyFriendsApp import menu_options
from Friend import Person
from Birthday import Birthday

def report_options():
    report_prompt = input("3.1 List of Friends Alphabetically \n3.2 List of Friends by Upcoming\
 Birthdays \n3.3 Mailing Labels for Friends \n3.4 Return to Previous Menu: ")
    numeric_range = [1, 2, 3, 3.1, 3.1, 3.3, 3.4, 4]
    input_num = float(report_prompt)
    if input_num == 1 or 3.1:
        sorted_names = alpha_sort()
        for name in sorted_names:
            print(name.title())
    elif input_num == 2 or 3.2:
        birthdays = birthday_sort()
        for birthday in birthdays:
            print(birthday)
    elif input_num == 3 or 3.3:
        mailing_labels = print_labels()
        for label in mailing_labels:
            print(label)
    elif input_num == 4 or 3.4:
        menu_options()
    else:
        if input_num not in numeric_range:
            print(f"Input value {input_num} not in acceptable numeric range")

def birthday_sort():
    path_to_file = "/workspaces/comp-170-su25-project/"
    file = "friends_database.csv"
    birthday_dict = {}
    with open(path_to_file + file, "r") as load_stream:
        lines = load_stream.readlines()
        for line in lines:
            info = line.strip()
            friend_attr = info.split(',')
            if friend_attr:
                first_name = friend_attr[0]
                last_name = friend_attr[1]
                full_name = f"{first_name} {last_name}"
                friend = Person(first_name, last_name)
                month = int(friend_attr[2])
                day = int(friend_attr[3])
                friend.set_birthday(month, day)
                days_left = Birthday.days_until()
                birthday_dict[full_name] = f"Days Until Birthday: {days_left}"
        return birthday_dict
                
       

def alpha_sort(): 
     path_to_file = "/workspaces/comp-170-su25-project/"
     file = "friends_database.csv"
     names = []
     with open(path_to_file + file, "r") as load_stream: 
          lines = load_stream.readlines()
          for line in lines:  
               info = line.strip()
               friend_attr = info.split(',')
               if friend_attr:
                    first_name = friend_attr[0].strip().lower()
                    last_name = friend_attr[1].strip().lower()
                    full_name = f"{first_name} {last_name}"
                    names.append(full_name)
                    names.sort()
          return names          

def print_labels():
     path_to_file = "/workspaces/comp-170-su25-project/"
     file = "friends_database.csv"
     addresses = []
     with open(path_to_file + file, "r") as load_stream: 
          lines = load_stream.readlines()
          for line in lines:  
               info = line.strip()
               friend_attr = info.split(',')
               if friend_attr:
                    full_name_list = []
                    full_name = friend_attr[0] + " " + friend_attr[1]
                    full_name_list.append(full_name)
                    address = friend_attr[4:]
                    mailing_address = full_name_list + address
                    addresses.append(mailing_address)
          return addresses      
