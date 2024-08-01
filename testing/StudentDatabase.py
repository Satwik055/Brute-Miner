from abc import ABC, abstractmethod
from Student import *

class StudentDatabase(ABC):
    @abstractmethod
    def addStudentData(self, username:str, data:dict):
        pass

    @abstractmethod
    def updateStudentData(self, username:str, data:dict):
        pass

    @abstractmethod
    def getStudentData(self, username) -> Student:
        pass
