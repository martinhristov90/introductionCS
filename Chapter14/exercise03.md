In this exercise, you’ll write __str__ and __repr__ methods for several classes.
1. In class Student, write a __str__ method that includes all the Member information and in addition includes the student number, the list of courses taken, and the list of current courses.
2. Write __repr__ methods in classes Member, Student, and Faculty.
Create a few Student and Faculty objects and call str and repr on them to verify that your code does what you want it to.

## Answer for both sub tasks in this exercise : 
```python
class Member:
    """ A member of a university. """

    def __init__(self, name: str, address: str, email: str) -> None:
        """Create a new member named name, with home address and email address."""

        self.name = name
        self.address = address
        self.email = email
    
    def __repr__(self):
        return "{0}({1},{2},{3})".format(self.__class__.__name__,self.name,self.address,self.email)

class Faculty(Member):
    """ A faculty member at a university. """

    def __init__(self, name: str, address: str, email: str,
                 faculty_num: str) -> None:
        """Create a new faculty named name, with home address, email address,
        faculty number faculty_num, and empty list of courses.
        """

        super().__init__(name, address, email)
        self.faculty_number = faculty_num
        self.courses_teaching = []

    def __repr__(self):
        return "{0}({1},{2},{3},{4},{5})".format(self.__class__.__name__,self.name,self.address,self.email,self.faculty_number,self.courses_teaching)


class Student(Member):
    """ A student member at a university. """

    def __init__(self, name: str, address: str, email: str,
                 student_num: str) -> None:
        """Create a new student named name, with home address, email address,
        student number student_num, an empty list of courses taken, and an
        empty list of current courses."""
        

        super().__init__(name, address, email)
        self.student_number = student_num
        self.courses_taken = []
        self.courses_taking = []
    
    def __str__(self):
        return "Name of the student : {0} \nAddress : {1} \nemail : {2} \nStudent number : {3} \nCourses_taken : {4} \nCourses_taking : {5} \n".format(self.name,self.address,self.email,self.student_number,self.courses_taken,self.courses_taking)

    def __repr__(self):
        return "{0}({1},{2},{3},{4},{5},{6})".format(self.__class__.__name__,self.name,self.address,self.email,self.student_number,self.courses_taken,self.courses_taking)
        
#student1 = Student("Martin Hristov","Mladost Sofia","test@test.bg",1234567)
#student1.courses_taken = ["Computer Science 1","Synthesis and analyses of algorithms"]
#student1.courses_taking = ["Object oriented programing"]
```
