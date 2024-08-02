from StudentDatabase import *
from supabase import create_client, Client

class SupabaseStudentDatabase(StudentDatabase):
    
    url = "https://jpechybbeebbfsnwlcjr.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpwZWNoeWJiZWViYmZzbndsY2pyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjIyMjE1MDIsImV4cCI6MjAzNzc5NzUwMn0.L1hDg51ET2qGcioBF9z8OT-2gtixEEvzRAu7AZ7mLIQ"
    
    supabase:Client = create_client(url, key)
    
    def addStudentData(self, userid:str, data:dict):
        #working-> all feild null except password="working..."
        #cracked but null -> all feild null
        #cracked -> all feild populated
        existing_row = self.supabase.table("Student").select('roll').eq('roll', userid).execute()

        if existing_row.data:
            # Update the row if it exists
            response = self.supabase.table("Student").update(data).eq('roll', userid).execute()
        else:
            # Insert a new row if it does not exist
            response = self.supabase.table("Student").insert(data).execute()

        
    def updateStudentData(self, userid:str, data:dict):
        pass
        
    def getStudentData(self, userid):
        response = self.supabase.table("Student").select("*").eq("roll", userid).execute()
        if(response.count is not None):
            student = Student.from_dict(response.data[0])
            return student
        else:
            None

    
    
    
    
    
# db = SupabaseStudentDatabase()
# userid = "2023/8888" 
# null_dict = {
#     "password":None,
#     "studentName":None,
#     "phone":None,
#     "email":None,
#     "roll":userid, 
#     "address":None,
#     "fatherName":None,
#     "motherName":None,
#     "dob":None,
#     "gender":None,
#     "category":None,
#     "studentId":None,
#     "session":None,
#     "enrollmentNo":None,
#     "admissionDate":None,
#     "studentType":None,
#     "timeTaken":None
#     }

