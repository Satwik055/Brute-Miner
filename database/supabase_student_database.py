from supabase import create_client, Client

from database.student_database import StudentDatabase
from model.student import Student


class SupabaseStudentDatabase(StudentDatabase):
    url = "https://jpechybbeebbfsnwlcjr.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpwZWNoeWJiZWViYmZzbndsY2pyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjIyMjE1MDIsImV4cCI6MjAzNzc5NzUwMn0.L1hDg51ET2qGcioBF9z8OT-2gtixEEvzRAu7AZ7mLIQ"

    supabase: Client = create_client(url, key)

    def addStudentData(self, userid: str, data: dict):
        existing_row = self.supabase.table("student").select('roll').eq('roll', userid).execute()
        if existing_row.data:
            self.supabase.table("student").update(data).eq('roll', userid).execute()
        else:
            self.supabase.table("student").insert(data).execute()

    def updateStudentData(self, userid: str, data: dict):
        pass

    def getStudentData(self, userid):
        response = self.supabase.table("student").select("*").eq("roll", userid).execute()
        if response.data:
            student = Student.from_dict(response.data[0])
            return student


# db = SupabaseStudentDatabase()
# print(db.addStudentData("2023/01300", {"roll": "2023/01300"}))
