from functions import user_registration, user_login, add_to_database


while True:
    print("*************Welcome to WaterBuddy*************")
    print("1. Register\n2. Login\n3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        user_registration()
        
    elif choice == 2:
        user_login()
        
    elif choice == 3:
        print("Thank you for using WaterBuddy!")
        break
    
    else:
        print("Invalid choice. Please try again.")