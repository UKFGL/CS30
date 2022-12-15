import csv
import functions
import json

# Direction,Year,Date,Weekday,Country,Commodity,Transport_Mode,Measure,Value,Cumulative

# Multi Accs - make a write+ function to create a new list for a user

# Data Management Project

# Global Variable(s)
# Data files
data_list = functions.read_file('./text-files/trade-data-set.txt')
users = functions.read_file('./text-files/users.txt')
# Other(s)
cur_user = None

# Run main function
def main():

    # Local Variable(s)
    line_num_1_archive = 0 #used in selection 1
    main_loop = False
    login_loop = True

    while login_loop:
        # Login or Sign-up Page
        print(
        '''
Welcome to Your Data Manager!
1. Login in
2. Sign up
        '''
        )

        option = input("Selection an option (1 or 2): ")

        if option == "1":
            user_login = functions.login(users)
            # Login function
            if user_login == -1:
                print("Inccorect Username or Password")
            else:
                cur_user = user_login
                main_loop = True
                login_loop = False
        
        elif option == "2":
            functions.sign_up(users)

        else: 
            print("Invalid Entry")

    # Main Menu (while loop)
    while main_loop:
        print(
        '''
DATE MANAGEMENT MAIN MENU

1. Display First 10 Items in Data Set
2. Search/Filter Data
3. Sort Data
4. Add to Favourites List
5. Remove Data from Favourites List
6. Display Favourites List
7. Exit

        '''
            )

        select = input("Input number of desired option (1-7): ")

        match select:
            case "1":

                # Track lines printed
                line_num_1 = 0

                # print(data_list[line_num_1:line_num_1 + 10])
                for i in range(line_num_1, line_num_1 + 10):
                    print("\n" + str(data_list[i]))
                
                # Set inner loop
                inner_loop_1 = True

                while inner_loop_1:
                    print(
'''
1. Display the next 10 items
2. Track back to last set of items displayed on previous visit
3. Return to Main Menu
'''
                    )

                    # Get input for inner loop
                    select_1 = input("Input number of desired option (1-3): ")

                    # Process input
                    if select_1 == "1":
                        # Add to line tracker
                        line_num_1 += 10

                        # print(data_list[line_num_1:line_num_1 + 10])
                        functions.print_10_lines(data_list, line_num_1) 
                    
                    elif select_1 == "2":
                        # Set current line # to the one the user was at during last session
                        line_num_1 = line_num_1_archive

                        # print(data_list[line_num_1:line_num_1 + 10])
                        functions.print_10_lines(data_list, line_num_1)

                    elif select_1 == "3":
                        line_num_1_archive = line_num_1
                        inner_loop_1 = False

                    else:
                        print("Invalid Entry")

            case "2":
                # Set inner loop 
                inner_loop_2 = True

                while inner_loop_2:
                    print(
'''
Filter By: 
1. Day of the Week
2. Date
3. Return to Main Menu
'''
                    )

                    select_2 = input("Input number of desired option (1-3): ")

                    if select_2 == "1":
                        day = input("Enter the day you would like to see data for: ")

                        functions.filter_search(data_list, day, "Weekday")

                    elif select_2 == "2":
                        date = input("Enter the date you would like to see data for (YYYY-MM-DD): ")

                        functions.filter_search(data_list, date, "Date")

                    elif select_2 == "3":
                        inner_loop_2 = False
                    
                    else: 
                        print("Invalid Entry")
            
            case "3":
                # Set inner loop 
                inner_loop_3 = True

                while inner_loop_3:
                    print(
'''
Sort By:
1. Date
2. Cumulative Value (Increasing)
3. Cumulative Value (Decreasing)
4. Return to Main Menu
'''
                    )

                    select_3 = input("Input number of desired option (1-4): ")


                    match select_3:
                        case "1":
                            functions.selection_sort(data_list, "Date", functions.sort_inc)
                            print(data_list)

                        case "2":
                            functions.selection_sort(data_list, "Cumulative", functions.sort_inc)
                            print(data_list)


                        case "3":
                            functions.selection_sort(data_list, "Cumulative", functions.sort_dec)
                            print(data_list)
                
                        case "4":
                            inner_loop_3 = False
                    
                        case other:
                            print("Invalid Entry")

            case "4":
                select_4 = input("Input date of trade you wish to add to favorites (YYYY-MM-DD): ")

                # Functionize so if no trade took place that day it returns -1 and check if trade is already in fav list
                for i in range(0, len(data_list)):
                    if data_list[i]["Date"] == select_4:
                        cur_user["Favorites"].append(data_list[i])
                
                # Add to current user's fav list
                functions.add_cur_user_fav(users, cur_user["Favorites"])               
                functions.write_data(users, './text-files/users.txt')
            
            case "5":
                select_5 = input("Input date of trade you wish to delete from favorites (YYYY-MM-DD): ")

                search_return_val = functions.search_data(cur_user, "Date", select_5)
                
                if search_return_val == -1:
                    print("Data was not found in list")
                else:
                    cur_user.pop(search_return_val)
                    # Add to current user's fav list
                    functions.add_cur_user_fav(users, cur_user)
                    
                functions.write_data(users, './text-files/favorites.txt')

            case "6":
                for i in range(0, len(cur_user["Favorites"])):
                    print("\n" + str(cur_user["Favorites"][i]))


            case "7":
                main_loop = False
                print ("Program Terminated")

            case other:
                print("Invalid Entry")

main()