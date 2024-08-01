from modules.firestore_module import *
from modules.requests_module import *


# Setting all the feilds of students with INVAILID_USERNAME to null



data = {
    "password":None,
    "studentName":None,
    "phone":None,
    "email":None,
    "roll":None, 
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
    }

def main():
    for i in range(1, 635):
        formatted = '{0:04}'.format(i)
        userid = "2023/" + formatted

        try:
            if(isStudentValid(userid)):
                print(f"Student {userid} is valid")
            else:
                print(f"Student invalid student {userid} to null...")
                updateDataOfFirestore(userid, data)
        except Exception as e:
            print(f"Error: {str(e)}")
        

