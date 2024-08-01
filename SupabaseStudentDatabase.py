from StudentDatabase import *
import os
import json
from StudentNotFoundException import *
from supabase import create_client, Client

class SupabaseStudentDatabase(StudentDatabase):
    
    url = "https://jpechybbeebbfsnwlcjr.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpwZWNoeWJiZWViYmZzbndsY2pyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjIyMjE1MDIsImV4cCI6MjAzNzc5NzUwMn0.L1hDg51ET2qGcioBF9z8OT-2gtixEEvzRAu7AZ7mLIQ"
    
    supabase:Client = create_client(url, key)
    
    def addStudentData(self, username:str, data:dict):
        print(username)

    def updateStudentData(self, username:str, data:dict):
        print(username)
        
    def getStudentData(self, roll) -> Student:
        response = self.supabase.table("Student").select("*").eq("roll", roll).execute()
        if(response.count is not None):
            student = Student.from_dict(response.data[0])
            return student
        else:
            raise StudentNotFoundException

    
    
    
    
    
    

db = SupabaseStudentDatabase()
db.getStudentData("2023/00")