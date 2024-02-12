# Registrar office is asking you to help programming a new system. In the new system, students records will be stored as objects of Student class 
# and teacher records will be stored as objects of Teacher class. The pervious programmer has written the Person class, from which both Student 
# and Teacher classes inherit. The definition of Person class is given in regmod.py file so you should be able to import the class using the following command:

# from regmod import Person
# Write two classes in Python, Student and Teacher classes.

# In Student class, override __init__ function so it takes 3 inputs: firstname, lastname, and student_id. 
# These inputs should be stored as instance variables (you should called Person.__init__ function to store firstname and lastname variables).
#  And override __str__ function so it appends a spacebar and the student_id surrounded by a square bracket to the result of Person.__str__ function, 
# e.g., My name is Sarun Gulyanon [9999123456].

# In Teacher class, override __init__ function so it takes 3 inputs: firstname, lastname, and email. These inputs should be stored as instance variables
#  (you should called Person.__init__ function to store firstname and lastname variables).

from regmod import Person as Ps
class Student(Ps):
    def __init__(self,firstname,lastname,student_id):
        self.student_id = student_id
        Ps.__init__(self,firstname,lastname)
    def __str__(self):
        return f'My name is {self.firstname} {self.lastname} [{self.student_id}]'
class Teacher(Ps):
    def __init__(self,firstname,lastname,email):
        Ps.__init__(self,firstname,lastname)
        self.email = email
    def __str__(self):
        return f'My name is {self.firstname} {self.lastname} [{self.email}]'