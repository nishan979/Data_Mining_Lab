class Student:
    def __init__(self, studentName, marks):
        self.studentName = studentName
        self.marks = marks

    def modify_attributes(self, new_name, new_marks):
        self.studentName = new_name
        self.marks = new_marks

student = Student("Nishan", 85)

# Print original values
print(f"Original Name: {student.studentName}, Original Marks: {student.marks}")

# Modify the attribute values
student.modify_attributes("Shahadat Hosen Nishan", 92)

print(f"Modified Name: {student.studentName}, Modified Marks: {student.marks}")