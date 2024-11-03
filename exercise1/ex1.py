import tkinter as tk
import random

DIFFICULTY_RANGES = { #Setting the parameters for the difficulty settings and a scores
    "Easy": (1, 9),
    "Moderate": (10, 99),
    "Advanced": (1000, 9999)
}
POINTS_FIRST_TRY = 10
POINTS_SECOND_TRY = 5
NUM_QUESTIONS = 10


class ArithmeticQuiz: #starting the main window and setting the variables
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Quiz")
        self.score = 0
        self.current_question = 0
        self.attempts = 0
        self.difficulty = None
        self.num1 = self.num2 = None
        self.operation = None
        #setting up the user inteface
        self.setup_ui()

    def setup_ui(self): # Clear the frame and display difficulty level options
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)
        self.displayMenu()

    def displayMenu(self): # Clear the frame and display difficulty level options
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        #creating a label to ask user to select difficulty
        tk.Label(self.main_frame, text="Select Difficulty Level:", font=("Arial", 16)).pack()
        for level in DIFFICULTY_RANGES: #Creating buttons for each difficulty
            button = tk.Button(self.main_frame, text=level, command=lambda l=level: self.start_quiz(l))
            button.pack(pady=5)

    def start_quiz(self, difficulty): #Starting the quiz with the user selected difficulty
        self.difficulty = difficulty
        self.score = 0
        self.current_question = 0
        self.attempts = 0
        self.ask_question()

    def ask_question(self):
        #Using a if statement to show the results if the questions are completed
        if self.current_question < NUM_QUESTIONS:
            #Generating random numbers to ask questions
            self.num1, self.num2 = self.randomInt()
            self.operation = self.decideOperation()
            self.correct_answer = self.num1 + self.num2 if self.operation == '+' else self.num1 - self.num2
            #clearing display to show new questions
            for widget in self.main_frame.winfo_children():
                widget.destroy()
            #displaying the questions to the user
            question = f"{self.num1} {self.operation} {self.num2} ="
            tk.Label(self.main_frame, text=f"Question {self.current_question + 1}: {question}",
                     font=("Arial", 16)).pack()
            self.answer_entry = tk.Entry(self.main_frame)
            self.answer_entry.pack(pady=10)
            tk.Button(self.main_frame, text="Submit", command=self.check_answer).pack()
        else:
            self.displayResults() #if the questions are finished show results

    def randomInt(self): # Generate two random integers within the difficulty range
        min_val, max_val = DIFFICULTY_RANGES[self.difficulty]
        return random.randint(min_val, max_val), random.randint(min_val, max_val)

    def decideOperation(self): # Randomly select addition or subtraction as the operation
        return '+' if random.choice([True, False]) else '-'

    def check_answer(self):
        try:  # Attempt to get the user's answer as an integer
            user_answer = int(self.answer_entry.get())
        except ValueError:  # Display error message if input is not a valid number
            tk.Label(self.main_frame, text="Please enter a valid number!", fg="red").pack()
            return
        # Check if the answer is correct
        if user_answer == self.correct_answer:
            # Award points based on the attempt count and update score
            points = POINTS_FIRST_TRY if self.attempts == 0 else POINTS_SECOND_TRY
            self.score += points
            tk.Label(self.main_frame, text="Correct!", fg="green").pack()
            self.current_question += 1
            self.attempts = 0
            self.ask_question()
        else:   # If the answer is incorrect, allow retry or show the correct answer
            if self.attempts == 0:
                self.attempts += 1
                tk.Label(self.main_frame, text="Incorrect, try again!", fg="red").pack()
            else: # Display the correct answer and move to the next question
                tk.Label(self.main_frame, text=f"Incorrect! The answer was {self.correct_answer}.", fg="red").pack()
                self.current_question += 1
                self.attempts = 0
                self.ask_question()

    def displayResults(self): # Clear the frame and display the user's score and grade
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        # Calculate and display the final grade
        grade = self.get_grade(self.score)
        result_text = f"Your score: {self.score}/{NUM_QUESTIONS * POINTS_FIRST_TRY}\nGrade: {grade}"
        tk.Label(self.main_frame, text=result_text, font=("Arial", 16)).pack(pady=10)
        # Display options to play again or quit
        tk.Button(self.main_frame, text="Play Again", command=self.displayMenu).pack()
        tk.Button(self.main_frame, text="Quit", command=self.root.quit).pack(pady=5)

    def get_grade(self, score):
        # calculting grade based on score
        if score >= 90:
            return "A+"
        elif score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "F"


root = tk.Tk()
app = ArithmeticQuiz(root)
root.mainloop()