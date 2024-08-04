import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from abc import ABC, abstractmethod
from model.student import Student


class StudentDatabase(ABC):
    @abstractmethod
    def addStudentData(self, userid: str, data: dict):
        pass

    @abstractmethod
    def updateStudentData(self, userid: str, data: dict):
        pass

    @abstractmethod
    def getStudentData(self, userid) -> Student:
        pass
