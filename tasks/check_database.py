from database.database import Database

db = Database()
def check_database():
    result = db.check_database() 
    if not(result):
        return None
        