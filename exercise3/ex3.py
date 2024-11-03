import tkinter as tk
from tkinter import messagebox
import csv


# Class to represent a Student
class Student:
    def __init__(self, code, name, coursework_marks, exam_mark):
        # Initialize the student with their code, name, coursework marks, and exam mark
        self.code = int(code)  # Ensure the student code is an integer
        self.name = name  # Store the student's name
        self.coursework_marks = list(map(int, coursework_marks))  # Convert coursework marks to integers
        self.exam_mark = int(exam_mark)  # Ensure the exam mark is an integer

    def total_coursework(self):
        # Calculate and return the total coursework marks
        return sum(self.coursework_marks)

    def overall_score(self):
        # Combine the total coursework marks and exam mark for the overall score
        return self.total_coursework() + self.exam_mark

    def percentage(self):
        # Calculate the percentage score based on the overall score
        return (self.overall_score() / 160) * 100  # Assume total possible score is 160

    def grade(self):
        # Determine the letter grade based on the percentage
        percent = self.percentage()
        if percent >= 70:
            return 'A'
        elif percent >= 60:
            return 'B'
        elif percent >= 50:
            return 'C'
        elif percent >= 40:
            return 'D'
        else:
            return 'F'  # Fail if below 40%


# Class to manage the Student application
class StudentApp:
    def __init__(self, root):
        # Set up the main application window and initialize student data
        self.root = root
        self.students = []  # This will hold all the student records
        self.load_students()  # Load student data from a file

        self.root.title("Student Management System")  # Set the window title
        self.root.geometry("400x400")  # Define the size of the window

        self.main_menu()  # Display the main menu for user interaction

    def load_students(self):
        # Load student data from a CSV file
        with open('studentMarks.txt', 'r') as file:
            reader = csv.reader(file)
            num_students = int(next(reader)[0])  # Read the number of students
            for row in reader:
                # Unpack student details from the row and create a Student object
                code, name, *coursework_marks, exam_mark = row
                student = Student(code, name, coursework_marks, exam_mark)
                self.students.append(student)  # Add the student to the list

    def main_menu(self):
        # Create a frame for the main menu
        menu_frame = tk.Frame(self.root)
        menu_frame.pack()

        # Display the title of the application
        tk.Label(menu_frame, text="Student Management System", font=("Arial", 16)).pack(pady=10)

        # Buttons for various actions the user can take
        tk.Button(menu_frame, text="1. View all student records", command=self.view_all_records).pack(fill='x')
        tk.Button(menu_frame, text="2. View individual student record", command=self.view_individual_record).pack(
            fill='x')
        tk.Button(menu_frame, text="3. Show student with highest total score", command=self.highest_score_student).pack(
            fill='x')
        tk.Button(menu_frame, text="4. Show student with lowest total score", command=self.lowest_score_student).pack(
            fill='x')

    def view_all_records(self):
        # Create a new window to display all student records
        records_window = tk.Toplevel(self.root)
        records_window.title("All Student Records")

        total_percent = 0  # To calculate the average percentage
        for student in self.students:
            total_percent += student.percentage()  # Accumulate the percentage for average calculation
            self.display_student_info(student, records_window)  # Show each student's info

        # Calculate and display the average percentage and total number of students
        avg_percent = total_percent / len(self.students)
        tk.Label(records_window, text=f"\nTotal students: {len(self.students)}, Average %: {avg_percent:.2f}",
                 font=("Arial", 10)).pack()

    def view_individual_record(self):
        # Create a new window to view an individual student's record
        individual_window = tk.Toplevel(self.root)
        individual_window.title("Individual Student Record")

        # Prompt for the student code
        tk.Label(individual_window, text="Enter student code:").pack(pady=5)
        student_code_entry = tk.Entry(individual_window)
        student_code_entry.pack()

        def show_student():
            # Retrieve the student code and search for the corresponding student
            student_code = int(student_code_entry.get())
            student = next((s for s in self.students if s.code == student_code), None)
            if student:
                # If the student is found, display their information
                self.display_student_info(student, individual_window)
            else:
                # Show an error message if the student is not found
                messagebox.showinfo("Error", "Student not found")

        tk.Button(individual_window, text="Show Record", command=show_student).pack(pady=10)

    def highest_score_student(self):
        # Find and display the student with the highest total score
        highest_student = max(self.students, key=lambda s: s.overall_score())
        self.show_top_student("Highest Score Student", highest_student)

    def lowest_score_student(self):
        # Find and display the student with the lowest total score
        lowest_student = min(self.students, key=lambda s: s.overall_score())
        self.show_top_student("Lowest Score Student", lowest_student)

    def show_top_student(self, title, student):
        # Create a new window to display information about a top student
        top_student_window = tk.Toplevel(self.root)
        top_student_window.title(title)
        self.display_student_info(student, top_student_window)

    def display_student_info(self, student, window):
        # Display detailed information about a student in a given window
        tk.Label(window, text=f"Name: {student.name}").pack()
        tk.Label(window, text=f"Student Number: {student.code}").pack()
        tk.Label(window, text=f"Total Coursework Mark: {student.total_coursework()}").pack()
        tk.Label(window, text=f"Exam Mark: {student.exam_mark}").pack()
        tk.Label(window, text=f"Overall %: {student.percentage():.2f}%").pack()
        tk.Label(window, text=f"Grade: {student.grade()}").pack()
        tk.Label(window, text="-" * 30).pack()  # Separator line for better readability


# Check if this script is being run directly
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    app = StudentApp(root)  # Instantiate the StudentApp class
    root.mainloop()  # Start the GUI event loop