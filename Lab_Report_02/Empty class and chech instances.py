class Student:
    pass

class Marks:
    pass

# Create instances
student_instance = Student()
marks_instance = Marks()

# Check instances
print(isinstance(student_instance, Student)) 
print(isinstance(marks_instance, Marks))     

# Check if the classes are subclasses of the built-in object class
print(issubclass(Student, object))  
print(issubclass(Marks, object)) 