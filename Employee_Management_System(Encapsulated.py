# Employee Class
class Employee:
    def __init__(self, emp_id, name, age, salary): # Here self → object. emp_id, name, age, salary → input values(parameters) to the constructer(__init__)
        self.__emp_id = emp_id # These inputs are stored in the object using self.__attribute_name
        self.__name = name # These inputs are stored in the object using self.__attribute_name
        self.__age = age # These inputs are stored in the object using self.__attribute_name
        self.__salary = salary # These inputs are stored in the object using self.__attribute_name
        
    def get_emp_id(self): #  get() → Read(Access) the value
        return self.__emp_id
    def get_name(self): #  get() → Read(Access) the value
        return self.__name
    def get_age(self): #  get() → Read(Access) the value
        return self.__age
    def get_salary(self): # get() →  Read(Access) the value
        return self.__salary
    
    def set_salary(self, new_salary): # set() → Change the value
        self.__salary = new_salary
    def set_emp_id(self, new_emp_id): # set() → Change the value
        self.__emp_id = new_emp_id
    def set_name(self, new_name): # set() → Change the value
        self.__name = new_name
    def set_age(self, new_age): # set() → Change the value
        self.__age = new_age      
        
    def display_info(self):
        print(f"ID: {self.__emp_id}, Name: {self.__name}, Age: {self.__age}, Salary: {self.__salary:2f}")
        
# Employee Management Class
class EmployeeManagementSystem():
    def __init__(self):
        self.employees = []
        
    def add_employee(self):
        emp_id = input("Enter Student ID: ")
        Name = input("Enter Student Name: ")
        Age = int(input("Enter Student Age: "))
        Salary = float(input("Enter Student Salary: "))
        emp = Employee(emp_id, Name, Age, Salary)
        self.employees.append(emp)
        print("Employee Added Successfully")
        
    def view_employee(self):
        if not self.employees:
            print("No Employees Found")
            return
        for emp in self.employees: # This line goes through each employee one by one in the list called self.employees
            emp.display_info()
        
    def search_employee(self):
        emp_id = input("Enter Student ID:")
        for emp in self.employees: # This line goes through each employee one by one in the list called self.employees
            if emp.get_emp_id() == emp_id: # This line checks if the current employee’s ID (from the list) is the same as the ID entered by the user
                print("Employee Found: ")
                emp.display_info()
                return
        print("Employee not Found")
                
    def update_employee(self):
        emp_id = input("Enter ID: ")
        for emp in self.employees:# This line goes through each employee one by one in the list called self.employees
            if emp.get_emp_id() == emp_id:# This line checks if the current employee’s ID (from the list) is the same as the ID entered by the user
                new_emp_id = int(input("Enter New Employee ID: "))
                new_name = input("New Employee Name: ")
                new_age = int(input("Enter Employee Age: "))
                new_salary = float(input("Enter Employee Salary: "))
                
                emp.set_emp_id(new_emp_id)
                emp.set_name(new_name)
                emp.set_age(new_age)
                emp.set_salary(new_salary)
                print(f"Updated salary for Employee ID {emp_id}.\n")
                return
        print("Employee not found!\n")
            
    def delete_employee(self):
        emp_id = input("Enter ID: ")
        for emp in self.employees:# This line goes through each employee one by one in the list called self.employees
            if emp.get_emp_id() == emp_id:# This line checks if the current employee’s ID (from the list) is the same as the ID entered by the user
                self.employees.remove(emp)
                print("Employee Removed Successfully")
                return
        print("Employee Not Found")
            
# Main Driver Program
if __name__ == "__main__":
    storage = EmployeeManagementSystem() # This line is used foe creating an object of the class EmployeeManagementSystem. storage is just a variable name that holds the object 
    
    while True:   
        print("\n----Employee Management System ----")    
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit.")
    
        choice = input("Select Operation(1/2/3/4/5/6): ")
    
        if choice == '1':
            storage.add_employee()
        elif choice == '2':
            storage.view_employee()
        elif choice == '3':
            storage.search_employee()
        elif choice == '4':
            storage.update_employee()
        elif choice == '5':
            storage.delete_employee()
        elif choice == '6':
            print("Exiting Employee Management System ")
            break
else:
    print("Enter Valid Function ")
