# A Empty Dictionary to store students records
students = {}

# Adding Student
def add_student():
    roll_no = int(input("Enter roll no: "))
    name = input("Enter Name: ")
    Age = int(input("Enter Age: "))
    Grade = input("Enter Grade: ")
    
    students[name] = {
        "roll_no" : roll_no,
        "Age" : Age,
        "Grade" : Grade 
    }
    print(f"Students with {name} added successfully!\n") 
    
# Viewing Student 
def view_student():
    if not students:
        print(f"No students record found")
        return
    for name, details in students.items():
        print(f"Name: {name}")
        for key, value in details.items():
            print(f" {key}: {value}")
        print()
        
# Searching student
def search_student():
    name = input("Enter name:")
    if name in students:
        print(f"The students with the {name} was found")
        for key, value in students[name].items():
            print(f"{key}: {value}")
        print()
    else:
        print(f"The student with {name} not found")
        
# Updating Student
def update_student():
    name = input("Enter name:")
    if name in students:
        print("Enter new details:")
        roll_no = int(input("Enter roll no: "))
        Age = input("Enter Age: ")
        Grade = input("Enter Grade: ")
                
        students[name] = {
            "roll_no": roll_no,
            "Age": Age,
            "Grade": Grade
        }
        print("Student details updated successfully\n")
    else:
        print("Student details not found") 
        
# Deleting student
def delete_student():
            name = input("enter name: ")
            if name in students:
                del students[name]
                print("Students record deleted successfully\n")
            else:
                print("Student not found\n")
                
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice(1-6): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting Student Management System. GoodBye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")
        
        
        
            
        
    
                
                
                
                
                    
