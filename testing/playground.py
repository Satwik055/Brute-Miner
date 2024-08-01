from FirebaseStudentDatabase import *
from SupabaseStudentDatabase import *

def main():
    db = SupabaseStudentDatabase()
    try:
        print(db.getStudentData("2023/00"))
    except Exception as e:
        print(f"Error:{e}")

        
    
main()