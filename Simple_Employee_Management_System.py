# Employee class to represent employee details
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        
    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}")
        
# Management class to handle operations
class EmployeeManagementSystem:
    def __init__(self):
        self.employee_list = []
        
    def add_employee(self):
        emp_id = input("Enter ID: ")
        name = input("Enter name: ")
        department = input("Enter Department: ")
        salary = input("Enter Salary: ")
        emp = Employee(emp_id, name, department, salary)
        self.employee_list.append(emp)
        print("Employee Added Successfully")
        
    def view_employee(self):
        if not self.employee_list:
            print("Employee not exist")
            return
        print("Employee Details: ")
        for emp in self.employee_list:
            emp.display_info()
            
    def search_student(self):
        search_student = input("Enter Employee ID: ")
        for emp in self.employee_list:
            if emp.emp_id == search_student:
                print("Employee found:")
                emp.display_info()
                return
        print("Employee not found.")
                
    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        for emp in self.employee_list:
            if emp.emp_id == emp_id:
                self.employee_list.remove(emp)
                print("Employee deleted successfully.")
                return
        print("Employee not found.")

                
# Main Program
if __name__ == "__main__":
    System = EmployeeManagementSystem()
    
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice:")
        
        if choice == '1':
            System.add_employee()
        elif choice == '2':
            System.view_employee()
        elif choice == '3':
            System.search_student()
        elif choice == '4':
            System.delete_student()
        elif choice == '5':
            print("EmployeeManagementSystem is exiting")
        else:
            print("Invalid choice. Please try again.")
        
        
        
        
        
                
            
        
