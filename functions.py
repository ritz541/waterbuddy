from connection import database
import bcrypt

db = database()
collection = db["pine"]

import bcrypt

def user_registration():
    user_name = input("Create a new username: ")
    
    # Check if the user already exists
    check_user = collection.find_one({
        "username": user_name
    })
    
    if check_user:
        print(f"{user_name} username already exists!")
        return
    
    password = input("Enter password: ")
    re_password = input("Re-enter password: ")
    
    if password != re_password:
        print("Passwords do not match!")
        return
    
    # Hash the password using bcrypt
    salt = bcrypt.gensalt()  # Generate a salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    if add_to_database(user_name, hashed_password):
        print("User created successfully! Please login.")

def add_to_database(username, password):
    try:
        collection.insert_one({
            "username": username,
            "password": password
        })
        return True
    except Exception as e:
        print(f"Error adding to database: {e}")
        return False
    
def user_login():
    user_name = input("Enter your username: ")
    
    try:
        check_user = collection.find_one({
            "username": user_name
        })
        
        if check_user:
            password = input("Enter your password: ")
            
            if bcrypt.checkpw(password.encode('utf-8'), check_user["password"]):
                print("Login successful!")
                return True
            else:
                print("Incorrect password!")
        else:
            print("User does not exist!")
    
    except Exception as e:
        print(f"Error occurred: {e}")
        
