class Student:
    def __init__(self, password, student_name, category, phone, email, roll, address, father_name, mother_name, dob,
                 gender, student_id, session, student_type, enrollment_no, admission_date, time_taken):
        self.password = password
        self.student_name = student_name
        self.category = category
        self.phone = phone
        self.email = email
        self.roll = roll
        self.address = address
        self.father_name = father_name
        self.mother_name = mother_name
        self.dob = dob
        self.gender = gender
        self.student_id = student_id
        self.session = session
        self.student_type = student_type
        self.enrollment_no = enrollment_no
        self.admission_date = admission_date
        self.time_taken = time_taken

    def __repr__(self):
        return f"Student(password={self.password}, student_name={self.student_name}, category={self.category}, phone={self.phone}, email={self.email}, roll={self.roll}, address={self.address}, father_name={self.father_name}, mother_name={self.mother_name}, dob={self.dob}, gender={self.gender}, student_id={self.student_id}, session={self.session}, student_type={self.student_type}, enrollment_no={self.enrollment_no}, admission_date={self.admission_date}, time_taken={self.time_taken})"

    @staticmethod
    def from_dict(data: dict):
        return Student(
            password=data['password'],
            student_name=data['student_name'],
            category=data['category'],
            phone=data['phone'],
            email=data['email'],
            roll=data['roll'],
            address=data['address'],
            father_name=data['father_name'],
            mother_name=data['mother_name'],
            dob=data['dob'],
            gender=data['gender'],
            student_id=data['student_id'],
            session=data['session'],
            student_type=data['student_type'],
            enrollment_no=data['enrollment_no'],
            admission_date=data['admission_date'],
            time_taken=data['time_taken']
        )
