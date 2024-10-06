from pymongo import MongoClient

def database():
    client = MongoClient("mongodb+srv://apple:<db_password>@cluster0.arozz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["waterbuddy"]
    return db