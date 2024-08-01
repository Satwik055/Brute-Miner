class Student:
    def __init__(self, password, studentName, category, phone, email, roll, address, fatherName, motherName, dob, gender, studentId, session, studentType, enrollmentNo, admissionDate, timeTaken):
        self.password = password
        self.studentName = studentName
        self.category = category
        self.phone = phone
        self.email = email
        self.roll = roll
        self.address = address
        self.fatherName = fatherName
        self.motherName = motherName
        self.dob = dob
        self.gender = gender
        self.studentId = studentId
        self.session = session
        self.studentType = studentType
        self.enrollmentNo = enrollmentNo
        self.admissionDate = admissionDate
        self.timeTaken = timeTaken

    def __repr__(self):
        return f"Student(password={self.password}, studentName={self.studentName}, category={self.category}, phone={self.phone}, email={self.email}, roll={self.roll}, address={self.address}, fatherName={self.fatherName}, motherName={self.motherName}, dob={self.dob}, gender={self.gender}, studentId={self.studentId}, session={self.session}, studentType={self.studentType}, enrollmentNo={self.enrollmentNo}, admissionDate={self.admissionDate}, timeTaken={self.timeTaken})"


    @staticmethod
    def from_dict(data: dict):
        return Student(
            password=data['password'],
            studentName=data['studentName'],
            category=data['category'],
            phone=data['phone'],
            email=data['email'],
            roll=data['roll'],
            address=data['address'],
            fatherName=data['fatherName'],
            motherName=data['motherName'],
            dob=data['dob'],
            gender=data['gender'],
            studentId=data['studentId'],
            session=data['session'],
            studentType=data['studentType'],
            enrollmentNo=data['enrollmentNo'],
            admissionDate=data['admissionDate'],
            timeTaken=data['timeTaken']
        )  