from Friend import Person

def create_friend():
    path_to_file = "/workspaces/comp-170-su25-project/"
    file = "friends_database.csv"
    new_friend = Person(None, None)
    prompt_1 = input("First Name: ")
    if prompt_1:
        new_friend.first_name = prompt_1
        prompt_2 = input("Last Name: ")
        if prompt_2:
            new_friend.last_name = prompt_2
            prompt_3 = input("Birthday (month/day): ")
            date = prompt_3.split('/')
            month_str = date[0]
            day_str = date[1]
            month = int(month_str)
            day = int(day_str)
            new_friend.set_birthday(month,day)
            if prompt_3:
                    prompt_4 = input("Address (Street): ")
                    new_friend.street_address = prompt_4
                    if prompt_4:
                        prompt_5 = input("Address (City): ")
                        new_friend.city = prompt_5
                        if prompt_5:
                            prompt_6 = input("Address (State): ")
                            new_friend.state = prompt_6
                            if prompt_6:
                                prompt_7 = input("Address (Zip): ")
                                new_friend.zip = prompt_7
                                if prompt_7:
                                    final_prompt = input("Save Friend? (Yes/No): ")
                                    if final_prompt.lower() == "yes":
                                        first_name_str = str(new_friend.first_name)
                                        last_name_str = str(new_friend.last_name)
                                        birthmonth_str = str(month)
                                        birthday_str = str(day)
                                        street_str = str(new_friend.street_address)
                                        city_str = str(new_friend.city)
                                        state_str = str(new_friend.state)
                                        zip_str = str(new_friend.zip)
                                        attribute_list= [first_name_str, last_name_str, birthmonth_str, birthday_str, street_str,
                                        city_str, state_str, zip_str]
                                        save_stream = open(path_to_file + file, "a")
                                        attribute_str = ",".join(item for item in attribute_list)
                                        save_stream.write(attribute_str + '\n')
                                        print(f"New Friend: {new_friend.__str__()} saved to file")
                                        menu_options()
                                    else:
                                        if final_prompt.lower() == "no":
                                                print("Friend Creation Canelled")
                                                menu_options()
                                        

def menu_options():
    while True:
        prompt_1 = "Application closed, Goodbye"
        menu_options = input("1 - Create new friend record\n2 - Search for a friend\n3 - Run reports\n4 - Exit\n-> ")
        numeric = int(menu_options)
        if numeric == 1:
             create_friend()
        elif numeric == 2: 
             record_search()
        elif numeric == 3:
             report_options()
        elif numeric == 4:
             print(prompt_1)
             break
        else:
             if numeric < 1 or numeric > 4:
                  print("Error, input not in specified range")

def record_search():
     path_to_file = "/workspaces/comp-170-su25-project/"
     file = "friends_database.csv"
     load_stream = open(path_to_file + file, "r")
     content = load_stream.read()
     if len(content) == 0:
          print("No Records Available For Modification.")
     else: 
          friend_search()

def friend_search():
     path_to_file = "/workspaces/comp-170-su25-project/"
     file = "friends_database.csv"
     with open(path_to_file + file, "r") as load_stream: 
       lines = load_stream.readlines()
       prompt_1 = input("Friend Name (First Last): ").strip().lower()
       found = False
       for line in lines:  
          info = line.strip()
          friend_attr = info.split(',')
          if friend_attr:
               first_name = friend_attr[0].strip().lower()
               last_name = friend_attr[1].strip().lower()
               full_name = f"{first_name} {last_name}"
               if prompt_1 == full_name:
                    print(f"Record Found: {full_name.title()}")     
                    record_options()
                    found = True
                    break 
       
       if not found:
          print("Record Not Found")
          menu_options()
                         
def record_options():
     path_to_file = "/workspaces/comp-170-su25-project/"
     file = "friends_database.csv"
     edit_stream = open(path_to_file + file, "r")
     record_prompt = input("Press E to Edit record or D to Delete record ")                                                
     lines = edit_stream.readlines()
     if record_prompt:
          if record_prompt.lower() == "e":
               edit_record()                                       
          else:
               if record_prompt.lower() == "d":
                  deletion_prompt = input("Are you sure you want to delete this friend record? (Yes/No): ")
                  if deletion_prompt.lower() == "yes":
                    confirmation_prompt = input("Confirmation of Friend Record for Deletion (First Last): ") 
                    deletion_stream = open(path_to_file + file, "wt") 
                    for line in lines:
                       if confirmation_prompt not in line:
                         deletion_stream.write(line)
                         deletion_stream.close()
                         print("Record Deleted")
                         menu_options()
                  else:
                       if deletion_prompt.lower() == "no":
                          edit_record()        
                                   
def edit_record():
     path_to_file = "/workspaces/comp-170-su25-project/"
     file = "friends_database.csv"
     load_stream = open(path_to_file + file, "r")
     lines = load_stream.readlines() 
     initial_edit_prompt = input("Confirmation of Friend Record for Modification (First Last): ").strip().lower()
     found = False 
     updated_lines = []
     for line in lines: 
          info = line.strip()
          friend_attr = info.split(',')
          full_name = f"{friend_attr[0].strip().lower()} {friend_attr[1].strip().lower()}"
          if initial_edit_prompt == full_name:
               found = True 
               print(f"Friend Record for Modification: {full_name.title()}")    
               edit_promt_1 = input("First Name (modified): ")                                                     
               if edit_promt_1:
                    friend_attr[0] = edit_promt_1
                    edit_prompt_2 = input("Last Name (modified): ")
                    if edit_prompt_2:
                         friend_attr[1] = edit_prompt_2
                         edit_prompt_3 = input("Birthmonth (modified): ")
                         if edit_prompt_3:
                              friend_attr[2] = edit_prompt_3
                              edit_prompt_4 = input("Birthday (modified): ")
                              if edit_prompt_4:
                                   friend_attr[3] = edit_prompt_4
                                   edit_prompt_5 = input("Street Address (modified): ")
                                   if edit_prompt_5:
                                        friend_attr[4] = edit_prompt_5
                                        edit_prompt_6 = input("City (modified): ")
                                        if edit_prompt_6:
                                             friend_attr[5] = edit_prompt_6
                                             edit_prompt_7 = input("State (modified): ")
                                             if edit_prompt_7:
                                                  friend_attr[6] = edit_prompt_7
                                                  edit_prompt_8 = input("Zip (modified): ")
                                                  if edit_prompt_8:
                                                       friend_attr[7] = edit_prompt_8
                                                       final_prompt = input("Save Edit? (Yes/No): ").strip().lower()
                                                       if final_prompt.lower() == "yes":
                                                            updated_line = ",".join(item for item in friend_attr) + "\n"
                                                            updated_lines.append(updated_line)
                                                            print(f"Friend Edit: {(friend_attr[0] + " " + friend_attr[1]).title()} saved to file")
                                                            menu_options()
                                                       else:
                                                            if final_prompt.lower() == "no":
                                                                 updated_lines.append(line)
                                                                 print("Record Unchanged")                              
              
     if not found:
          print("Friend Not in Record")  
          menu_options()
     
     save_stream = open(path_to_file + file, "wt") 
     save_stream.writelines(updated_lines)
     menu_options()

def report_options():
     report_prompt = input("3.1 List of Friends Alphabetically \n3.2 List of Friends by Upcoming\
Birthdays \n3.3 Mailing Labels for Friends \n3.4 Return to Previous Menu: ")
     numeric_range = [1, 2, 3, 4, 3.1, 3.2, 3.3, 3.4]
     report_prompt_num = int(report_prompt)
     if report_prompt_num == 1 or 3.1:
          alpha_sort()
          sorted_names = alpha_sort()
          for name in sorted_names:
               print(f"{name.title()}")
     elif report_prompt_num == 2 or 3.2:
          birthday_sort()
     elif report_prompt_num == 3 or 3.3:
          print_labels()
     elif report_prompt_num == 4 or 3.4:
          menu_options()
     else:
          if report_prompt_num not in numeric_range:
               print(f"Input value {report_prompt_num} not in acceptable numeric range")

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

def birthday_sort():
     pass

def print_labels():
     pass


menu_options()