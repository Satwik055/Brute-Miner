from modules.firestore_module import *
from modules.requests_module import *

# usernames from 300 - 500 don't have user data

def updateUserdataToDatabase(userid, password):
    cookie = getSessionCookie(userid, password)
    studentDetailsHtml = getStudentDetails(cookie)
    student = parseStudentDetailsHtmlToStudent(studentDetailsHtml)

    data = {
            "password":password,
            "studentName":student.name,
            "phone":student.contact_no,
            "email":student.email,
            "roll":student.roll_no, 
            "address":student.address,
            "fatherName":student.father_name,
            "motherName":student.mother_name,
            "dob":student.dob,
            "gender":student.gender,
            "category":student.category,
            "studentId":student.student_id,
            "session":student.session,
            "enrollmentNo":student.enrollment_no,
            "admssionDate":student.admission_date,
            "studentType":student.student_type,
            }
    
    updateDataOfFirestore(userid, data)




def main():
    for i in range(300, 500):
        formatted = '{0:04}'.format(i)
        userid = "2023/" + formatted

        try:
            password = getPasswordFromFirestore(userid)
            print(f"Storing data of {userid}, {password}")
            updateUserdataToDatabase(userid, password)

        except Exception as e:
            print(f"Error: {str(e)}")




main()

