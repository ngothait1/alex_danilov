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
    user_name, user_age = user_dict[user_id]
    print("ID: " + str(user_id) + "\nName: " + user_name + "\nAge: " + str(user_age))

def error_msg(value, name_of_entry, pause_message):
        print("Error: " + name_of_entry + " must be number. " + value + " is not a number")
        input(pause_message)
    
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

def main():
    
    user_dict = {}
    keys_list = []
    user_stats = {"total_age": 0, "user_count": 0}
    # user_dict = {
    #                 101 : ["Alex", 25],
    #                 102 : ["John", 30],
    #                 103 : ["David", 22]
    #               }




    press_enter_msg = "Press Enter to continue "
    
    while True:
        selected_option = input(get_menu())
        
        if selected_option == "1":
            user_id = input("ID: ")
            if user_id.isdigit() is False:
                error_msg(user_id, "ID", press_enter_msg)
                continue
            user_id = int(user_id)
            if user_id  in user_dict:
                entry_name, entry_age = user_dict[user_id]
                print("Error: ID already exists: {'name': '" + entry_name + "' , 'age': " + str(entry_age) + " }")
                pause()
                continue

                
            user_name = input("Name: ")
    
            user_age = input("Age: ")
            if user_age.isdigit() is False:
                error_msg(user_age, "Age", press_enter_msg)
                continue
            user_age = int(user_age)
            save_new_entry(user_dict, [user_id, user_name, user_age], user_stats)
            print("ID [" + str(user_id) + "] saved successfully.")
            keys_list = list(user_dict)
            pause()
            
        elif selected_option == "2":
            entry_id = input("Please enter the ID you want to look for: ")
            if entry_id.isdigit() is False:
                error_msg(entry_id, "ID", press_enter_msg)
                continue
            entry_id = int(entry_id)
                
            result = search_entry_by_id(user_dict, entry_id)
            if result is None:
                print("Error: ID " + str(entry_id) + " is not saved")
            else:
                entry_name, entry_age = result
                print("ID: " + str(entry_id) + "\nName: " + entry_name + "\nAge: " + str(entry_age)) 
            pause()
            
        elif selected_option == "3":
            print_ages_average(user_dict, user_stats)
            pause()
            
        elif selected_option == "4":
            print_all_names(user_dict)
            pause()

        elif selected_option == "5":
            print_all_ids(user_dict)
            pause()

        elif selected_option == "6":
            print_all_entries(user_dict)
            pause()

        elif selected_option == "7":
            entry_index = input("Please enter the index of the entry you want to print: ")
            
            if entry_index.isdigit() is False:
                error_msg(entry_index, "Index", press_enter_msg)
                continue
            
            entry_index = int(entry_index)
            
            print_entry_by_index(user_dict,entry_index, keys_list)        
            pause()

        elif selected_option == "8":
            while True:
                user_input = input("Are you sure? (y/n) ")
                if user_input == "y" or user_input == "n":
                    break
                
            if user_input == "y":
                print("Goodbye!")
                break
            
        else:
            print("Error: Option [" + selected_option + "] does not exist. Please try again")
    
if __name__ == "__main__":
    main()
