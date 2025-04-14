class Student:
    '''
    This class represents the blueprint for student object.

    Attributes:
    id: The id of the student, datatype = int
    name: The full name of the student, datatype = str
    address: The address of the student, datatype = str
    admission_year: The year the student was admitted, datatype = int
    level: The level/year of the student, datatype = int
    section: The section assigned to the student, datatype = str

    Methods:
    display(): This method displays all the attributes of the Student

    '''
    def __init__(self, id, name, address, admit_year, level, section):
        self.id = id
        self.name = name
        self.address = address
        self.admission_year = admit_year
        self.level = level
        self.section = section
    def display(self):
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

#print(Student.__doc__)
s_id = int(input("Enter your Student ID: "))
name = input("Enter your Name: ")
address = input("Enter your Address: ")
admit = int(input("Enter Admission Year: "))
level = int(input("Enter Level: "))
sec = input("Enter Section: ")
s1 = Student(s_id,name,address,admit,level,sec)
print()
s1.display()
