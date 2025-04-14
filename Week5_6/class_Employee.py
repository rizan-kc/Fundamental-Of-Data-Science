'''
The program has a class called Employee with different attributes. 
This allows to add multiple employees data to be taken as input and save it in a csv file called
employees.csv
This data can also later be viewed to see the list of employees and their details.
'''
import csv
import os

class Employee:
    '''
    Class to represent an employee with their data

    Attributes:
    empid: identity of the employee, datatype = int
    name: name of the employee, datatype = str
    Address: Address of the employee, datatype = str
    contact_number: Contact number of the employee, datatype = str
    number_of_child: Number of children, datatype = int
    salary: identity of the employee, dattype = int

    Methods: 
    save_csv(): saves the data to a csv file named 'employees.csv'
    '''
    def __init__(self, id, name, address, contact, spouse, noc, salary):
        self.empid = id
        self.name = name
        self.address = address
        self.contact_number = contact
        self.spouse_name = spouse
        self.number_of_child = noc
        self.salary = salary
        
    def save_csv(self):
        try:
            file_exist = os.path.isfile("employees.csv")
            with open("employees.csv",mode = "a", newline="") as csv_file:
                lt = [self.empid,self.name,self.address,self.contact_number,self.spouse_name,self.number_of_child,self.salary]
                writer = csv.writer(csv_file)
                if not file_exist:
                    writer.writerow(["Employee ID","Name","Address","Contact","Spouse","Children","Salary"])
                writer.writerow(lt)
                print("File Saved Successfully!")
        except Exception as e:
            return ("Error:",e)


def read_csv():
    try:
        file_exist = os.path.isfile("employees.csv")
        if file_exist:
            with open("employees.csv",mode = "r") as csv_file:
                content = csv.reader(csv_file)
                rows = list(content)
                if rows:
                    col_width = [max(len(item) for item in col) for col in zip(*rows)]
                    for row in rows:
                        formatted_row = " | ".join(item.ljust(col_width[i]) for i, item in enumerate(row))
                        print(formatted_row)
    except Exception as e:
        print("Error:",e)

def input_data():
    try:
        id = int(input("Enter your ID: "))
        n = input("Enter your name: ")
        a = input("Enter your address: ")
        c = input("Enter your contact number: ")
        s = input("Enter your spouse name: ")
        nc = int(input("Enter the number of children, if no children's enter 0: "))
        sa = int(input("Enter your salary:"))
        return [id, n, a, c, s, nc, sa]
    except:
        return "Invalid Input"

print(__doc__)
while True:
    print(f"{'Employment Directory':>75}")
    print(f"{'1. Enter your Credentials':>77} ")
    print(f"{'2. List the Credentials':>77} ")
    print(f"{'3. Exit':>70}")
    init_ch = int(input("Enter 1,2,3 based on your preference: "))
    if init_ch == 1:
        x = input_data()
        if isinstance(x, list):
            emp = Employee(*x)

            ch_save = input("Do you want to save this in a file? ")
            if ch_save == 'Y' or ch_save == 'y':
                emp.save_csv()
    elif init_ch == 2:
        read_csv()
    elif init_ch == 3:
        print("Exiting the program.")
        break
    else:
        print("Invalid Option. Try again!")

