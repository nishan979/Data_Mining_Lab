class Student:
    def __init__(self, studentId, studentName, studentClass):
        self.studentId = studentId
        self.studentName = studentName
        self.studentClass = studentClass

    def display_attributes(self):
        print(f"Student ID: {self.studentId}")
        print(f"Student Name: {self.studentName}")
        print(f"Student Class: {self.studentClass}")


student = Student(1, "Shahadat Hosen", "Under Graduation")
student.display_attributes()