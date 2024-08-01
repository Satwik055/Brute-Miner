from modules.firestore_module import *
from modules.requests_module import *


# Update category of students

def storeCategoryToDatabase(userid, password):
    cookie = getSessionCookie(userid, password)
    studentDetailsHtml = getStudentDetails(cookie)
    student = parseStudentDetailsHtmlToStudent(studentDetailsHtml)
    data = {
            "category":student.category,
            }
    updateDataOfFirestore(userid, data)

def main():
    for i in range(1, 625):
        formatted = '{0:04}'.format(i)
        userid = "2023/" + formatted
        try:
            if(isCategoryAvailable(userid)):
                print(f"Student {userid} category exists")
            else:
                print(f"Retriving and storing category for {userid}...")
                password = getPasswordFromFirestore(userid)
                storeCategoryToDatabase(userid, password)
        except Exception as e:
                print(f"Error: {str(e)} ")


main()