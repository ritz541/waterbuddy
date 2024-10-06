from functions import user_registration, user_login, add_to_database
from notification import notification
import threading

while True:
    print("\n")
    print("*************Welcome to WaterBuddy*************")
    print("1. Register\n2. Login\n3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        user_registration()
        
    elif choice == 2:
        if user_login():
            notification_thread = threading.Thread(target=notification)
            notification_thread.daemon = True
            notification_thread.start()
        
    elif choice == 3:
        print("Thank you for using WaterBuddy!")
        break
    
    else:
        print("Invalid choice. Please try again.")
        
    