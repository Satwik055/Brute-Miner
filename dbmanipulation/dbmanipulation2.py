from modules.firestore_module import *
from modules.requests_module import *


def main():
    for i in range(187, 628):
        formatted = '{0:04}'.format(i)
        userid = "2023/" + formatted

        print(f"Converting family of {userid} to lowercase")
        try:
            student_name, father_name, mother_name = getStudentFamilyFromFirestore(userid)

            student_name_lowercase = student_name.lower()
            father_name_lowercase = father_name.lower()
            mother_name_lowercase = mother_name.lower()

            setStudentFamilyToFirestore(userid,student_name_lowercase, father_name_lowercase, mother_name_lowercase)

        except Exception as e:
            print(f"Error: {str(e)} ")

