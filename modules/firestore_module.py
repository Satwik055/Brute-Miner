import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import platform


PRIVATE_KEY = {
  "type": "service_account",
  "project_id": "bruteit-c9a85",
  "private_key_id": "115fa9d695f20a76c000ea89b0ef0d415190387f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDp+1av93hndyXo\n5YcTbRvcu+AkcIxumYF5NAKezHIPIv80hzgotVzgLSrKvWrOYubgEodSNQY3gds+\n9Tz/bSFyGbGo5D+3RPywK3lwYqXTaQdwRS28sEcIyZL9Trlki71op9WhXftSs3zL\n+7Q26OIp0buj5kHgFlxMHKxF2d1XduVzjJK6XdN0b3hzAS1+ZBJBmSKV0Vjgx5C1\nT4EbAafaIkTUjHeLzp9YX9Q+pieOKGvVzutGGaQL3YtrammolZaOqtIQU9zqxv5I\nfxmfdmIPh6iZKbLeU/Nj9mbG7wlnwW7iEl9IjQv3hdMSuqz/dnKJNrms9tlA9u2q\n72CibJqnAgMBAAECggEAZR6VKTk3FOf+Pzeq969Iwk2DodvuJQI8XUgn9b7/cCE8\nz9O8ZoNy3wNGIhZYaVd+1cnMJ6/4vtZlDUFpGi5srOYDzKzQCIFM/0naksJfTg1v\nBIsxKAG6wUZ0Ovrhzl1B/0/BWJrIOcaOIY3nJW/iBha5FC03vQOM4evmW827Bcft\n37Yauwfd9GEN3KcLNrGjp3H9HdNepHYoOVdUUf0UVjv0EJr7+Hp5fF5oM531tuc2\nGmzRRzxsXwJGvbthk9KGlx0gDlgN9nfjsWBwxFucxKNmW+T5hRMol4WvJTtlQUWT\nMdC0heLIW/EfymMxlfZjfKhxweoPtikhXnvujPjLSQKBgQD8Rt7t+MZTBmDFNWaO\n0VeFt4plLEl6PgVeozQm3V3wDNl2EK0gWxGNslMG1rN7KVo6gBu0s1mA9TzyYrC0\nAIGjCGXGmP646jzeW+BB23h9h4AXlQ1osQL3epPLwkkXo8iJOfFAxJT3mHYmFWck\nV+XqrGDC2kk+Z4Nkj8j3M2nxDQKBgQDtb1jd3F4klilcoGDo3fnq1D/i/MGFybd6\niaMfzazFjkhl8tYkpHSiTbwjB0UMUlJ7QXH+TrqSpdaD5ttSQeCuPzhMgOvpHGgn\n/kx7XavnCrU+NfuAx1iLFfhVMiAh+KjkbtpMfU4LG/jyM9RC+9KSVoOQif3Ow9wL\nQ+b/LUUFgwKBgQDdACjjSABVU00K9hD2JCYMGhG/N+DWmeaSVV6mfV6BoIAQkeNY\naO8jtohNgWCSEFPe08NxtXw/IJdXr2UlCxyF+iFOrVDYJTtVgB8hEmancUChaA3r\nHMaAjn1TDsyBTRWsQXo7RvtJO+Kk0jMc/3OG9aN+j0OCy6OrQNrI092HMQKBgQDW\nrtwiVpPE7wVdHCIjzDmhy+IsIi/1AUvl/zdAlV6HjjwF+kkH/q765eCbp4IWPwUX\nLzicIaFu4YYR45YhTTGTO9Ry0Ar+ztGaf8O1tB+vmy3/nx3V9ekocWgF2HnXXZeQ\nXG8DxDThtJwmmxhsrHdcG99/vFWCM/PtN6tQxSTocwKBgQDz/sXSm0jzwyr/LEXe\nvRl/ngEb9DA75yL2CmY4NDnWUcAuZSNPPPP2nhwtiQ8Z5TTcRvjCEfp+a4/2LRuW\n8lzWvGORaeKrPpHi6FH+ci2niY8b67p0sCDjj8Kk1Bis1E4bFjieEhkBNIfW885W\njzg+j5itP03LgXpkA41vVjOdEg==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-21o6a@bruteit-c9a85.iam.gserviceaccount.com",
  "client_id": "111017131315253178779",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-21o6a%40bruteit-c9a85.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

cred = credentials.Certificate(PRIVATE_KEY)
firebase_admin.initialize_app(cred)

database = firestore.client()
collection_students = database.collection("Students")


def initStudentToFirestore(userId):
    fuserId = userId.replace("/", "-")
    data = { 
        "Password":"working...",
        "Node": platform.node()
        }
    collection_students.document(fuserId).set(data)

def addDataToFirestore(userId, data:dict):
    fuserId = userId.replace("/", "-")
    collection_students.document(fuserId).set(data)

def getPasswordFromFirestore(userid) -> str:

    fuserId = userid.replace("/", "-")
    doc_ref = collection_students.document(fuserId).get()
    password = doc_ref.to_dict().get('password')

    if(password is None):
        raise Exception("Username doesn't exists")
    else:
        return password

def findFirestoreStudent(userid):

    fuserId = userid.replace("/", "-")
    doc_ref = collection_students.document(fuserId).get()
    return doc_ref.exists

def updateDataOfFirestore(userId, data:dict):
    fuserId = userId.replace("/", "-")
    collection_students.document(fuserId).update(data)

#-------------------------TEMP-----------------------------#

def getStudentFamilyFromFirestore(userId:str):
    fuserId = userId.replace("/", "-")
    doc_ref = collection_students.document(fuserId).get()

    if(doc_ref.exists is False):
        raise Exception("Document not found")
    
    student_name = doc_ref.to_dict().get("studentName")
    father_name = doc_ref.to_dict().get("fatherName")
    mother_name = doc_ref.to_dict().get("motherName")


    if(student_name is None):
        raise Exception("Student not found")
    
    return student_name, father_name, mother_name

def setStudentFamilyToFirestore(userId:str, student_name:str, father_name:str, mother_name:str):
    fuserId = userId.replace("/", "-")
    data =  {
        "studentName":student_name,
        "fatherName": father_name,
        "motherName": mother_name
    }
    collection_students.document(fuserId).update(data)

def isStudentValid(userid) -> bool:
    fuserId = userid.replace("/", "-")
    doc_ref = collection_students.document(fuserId).get()
    password = doc_ref.to_dict().get('password')

    if(password is not None):
        return True
    else:
        return False

def isCategoryAvailable(userid):
    fuserId = userid.replace("/", "-")
    doc_ref = collection_students.document(fuserId).get()
    category = doc_ref.to_dict().get('category')

    if(category is None):
        return False
    else:
        return True



#------------------------CONFIG-------------------------#

def getUserRangeConfig():
    collection = database.collection("Config")
    doc_ref = collection.document("uid_range_config").get()
    
    startuid = doc_ref.to_dict().get('startuid')
    stopuid = doc_ref.to_dict().get('stopuid')

    return startuid, stopuid
