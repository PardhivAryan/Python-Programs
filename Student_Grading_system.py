class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 90:
            return 'A+'
        elif avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 60:
            return 'C'
        else:
            return 'Fail'
        
    def display_info(self):
        print(f"Name: {self.name}, Marks: {self.marks}, Grade: {self.calculate_grade()}")
        
class ScienceStudent(Student):
    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 85:
            return 'A+'
        elif avg >= 70:
            return 'A'
        elif avg >= 55:
            return 'B'
        elif avg >= 45:
            return 'C'
        else:
            return 'Fail'
        
class ArtStudent(Student):
    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 80:
            return 'A+'
        elif avg >= 65:
            return 'A'
        elif avg >= 50:
            return 'B'
        elif avg >= 40:
            return 'C'
        else:
            return 'Fail'
            
students = []
num = int(input("Enter number of students: "))

for _ in range(num):
    student_type = input("Enter student type (Science/Arts/Generic): ").strip().lower()
    name = input("Enter student name: ")
    marks_input = input("Enter marks separated by commas (e.g., 85,78,92): ")
    marks = list(map(int, marks_input.split(',')))

    if student_type == "science":
        students.append(ScienceStudent(name, marks))
    elif student_type == "arts":
        students.append(ArtStudent(name, marks))
    else:
        students.append(Student(name, marks))

print("\n===== STUDENT REPORT =====")
for student in students:
    print("===============")
    student.display_info()