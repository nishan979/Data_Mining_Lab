class Student:
    def __init__(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName

    def add_attribute(self, attribute_name, value):
        setattr(self, attribute_name, value)

    def remove_attribute(self, attribute_name):
        if hasattr(self, attribute_name):
            delattr(self, attribute_name)

    def display_attributes(self):
        attributes = self.__dict__
        for key, value in attributes.items():
            print(f"{key}: {value}")

# Example usage
student = Student(1, "Shahadat Hosen")
student.display_attributes()

student.add_attribute("studentSemester", "8th Semester")
print("Attributes after adding studentClass:")
student.display_attributes()

student.remove_attribute("studentName")
print("\nAttributes after removing studentName:")
student.display_attributes()