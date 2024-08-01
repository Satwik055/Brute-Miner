from abc import ABC, abstractmethod
from Student import *

class StudentDatabase(ABC):
    @abstractmethod
    def addStudentData(self, userid:str, data:dict):
        pass

    @abstractmethod
    def updateStudentData(self, userid:str, data:dict):
        pass

    @abstractmethod
    def getStudentData(self, userid) -> Student:
        pass
