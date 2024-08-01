class StudentNotFoundException(Exception):
    def __init__(self):
        self.message = "No student data found"
        super().__init__(self.message)