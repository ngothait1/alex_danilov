def save_new_entry(user_dict, user, user_stats):
    user_id, user_name, user_age = user
    user_dict[user_id] = [user_name, user_age]
    user_stats["total_age"] += user_age
    user_stats["user_count"] += 1

def search_entry_by_id(user_dict, user_id):
    if user_id in user_dict:
        return user_dict[user_id]
    return None

def print_ages_average(user_dict, user_stats):
    if not user_dict:
        print("No users in the database.\nThe ages average is: 0")
        return
    
    average = user_stats["total_age"] / user_stats["user_count"]
    print("The ages average is: " + str(average))

def print_all_names(user_dict):
    if not user_dict:
        print("No users in the database.")
        return
   
    for index, (user_name, user_age) in enumerate(user_dict.values()):
        print(str(index) + ". " + user_name)
        
def print_all_ids(user_dict):
    if not user_dict:
        print("No users in the database.")
        return
   
    for index, user_id in enumerate(user_dict):
        print(str(index) + ". " + str(user_id))

def print_all_entries(user_dict):
    if not user_dict:
        print("No users in the database.")
        return

    for index, (user_id, (user_name, user_age)) in enumerate(user_dict.items()):
      print(str(index) + ". " + str(user_id) +"\n   Name: " + user_name + "\n   Age: " + str(user_age))

def print_entry_by_index(user_dict, entry_index, keys_list):
    if len(user_dict) == 0:
        print("No users in the database.")  
        return
    
    if entry_index < 0 or entry_index > (len(user_dict) - 1):
        print("Index out of range. The maximum index allowed is " + str(len(user_dict) - 1))
        return
    user_id = keys_list[entry_index]
    print_entry(user_dict,user_id)

def print_entry(user_dict, user_id):
    user_name, user_age = user_dict[user_id]
    print("ID: " + str(user_id) + "\nName: " + user_name + "\nAge: " + str(user_age))

def error_not_number_msg(value, name_of_entry):
        print("Error: " + name_of_entry + " must be number. " + value + " is not a number")
    
def get_menu():
    menu = """
1. Save a new entry
2. Search by ID
3. Print ages average
4. Print all names
5. Print all IDs
6. Print all entries
7. Print entry by index
8. Exit
Please enter your choice: """
    return menu

def pause(msg="Press Enter to continue "):
    input(msg)

def option_1(user_dict, user_stats):
    user_id = input("ID: ")
    if user_id.isdigit() is False:
        error_not_number_msg(user_id, "ID")
        return False
    user_id = int(user_id)
    if user_id  in user_dict:
        entry_name, entry_age = user_dict[user_id]
        print("Error: ID already exists: {'name': '" + entry_name + "' , 'age': " + str(entry_age) + " }")
        return False
    user_name = input("Name: ")
    user_age = input("Age: ")
    if user_age.isdigit() is False:
        error_not_number_msg(user_age, "Age")
        return False
    user_age = int(user_age)
    save_new_entry(user_dict, [user_id, user_name, user_age], user_stats)
    print("ID [" + str(user_id) + "] saved successfully.")
    return True

def option_2(user_dict):
    entry_id = input("Please enter the ID you want to look for: ")
    if entry_id.isdigit() is False:
        error_not_number_msg(entry_id, "ID")
        return
    entry_id = int(entry_id)  
    result = search_entry_by_id(user_dict, entry_id)
    if result is None:
        print("Error: ID " + str(entry_id) + " is not saved")
    else:
        print_entry(user_dict,entry_id)
 
def option_3(user_dict, user_stats):
    print_ages_average(user_dict, user_stats)
    
def option_4(user_dict):
    print_all_names(user_dict)

def option_5(user_dict):
    print_all_ids(user_dict)
    
def option_6(user_dict):
    print_all_entries(user_dict)
       
def option_7(user_dict, keys_list):
    entry_index = input("Please enter the index of the entry you want to print: ")
    if entry_index.isdigit() is False:
        error_not_number_msg(entry_index, "Index")
        return
    entry_index = int(entry_index)
    print_entry_by_index(user_dict,entry_index, keys_list)  
   
def option_8():
    while True:
        user_input = input("Are you sure? (y/n) ")
        if user_input == "n":
            return False
        elif user_input == "y":
            print("Goodbye!")
            return True
            
def main():
    
    user_dict = {}
    keys_list = []
    keys_list_dirty = True # Flag to track if user_dict has changed and keys_list needs to be updated
    user_stats = {"total_age": 0, "user_count": 0}
    
    while True:
        selected_option = input(get_menu())
        
        if selected_option == "1":
            return_keys_list_dirty = option_1(user_dict, user_stats)
            if keys_list_dirty == False:
                keys_list_dirty = return_keys_list_dirty
              
        elif selected_option == "2":
            option_2(user_dict)
            
        elif selected_option == "3":
            option_3(user_dict, user_stats)
            
        elif selected_option == "4":
            option_4(user_dict)

        elif selected_option == "5":
            option_5(user_dict)

        elif selected_option == "6":
            option_6(user_dict)

        elif selected_option == "7":
            if keys_list_dirty is True:
                keys_list = list(user_dict)
                keys_list_dirty = False
            option_7(user_dict, keys_list)
   
        elif selected_option == "8":
            if option_8() == True:
                break

        else:
            print("Error: Option [" + selected_option + "] does not exist. Please try again")
        pause()

if __name__ == "__main__":
    main()