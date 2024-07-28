from modules.firestore_module import *
from modules.requests_module import *

def storeUserdataToDatabase(userid, password):
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
            "enrollmentNo.":student.enrollment_no,
            "admssionDate":student.admission_date,
            "studentType":student.student_type,
            }
    addDataToFirestore(userid, data)
