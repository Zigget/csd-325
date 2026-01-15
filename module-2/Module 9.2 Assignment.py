# Made by: Samuel Sidzyik
# Module 9.2 Assignment.py
# Start Date December 7, 2025
# 
# This is our first assignment creating classes. We create a student and get a GPA for the created student
# I've taken Python course previously. I may be plagerizing myself a little on thi assignment, lol. Not wholesale, just refreshing my memory on how to write it out.


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.total_credits = 0
        self.total_points = 0

    def add_course(self, credits, grade):

        grade_points = self.convert_grade_to_points(grade)
        self.total_credits += credits
        self.total_points += grade_points * credits

    def convert_grade_to_points(self, grade):
        #Convert letter grade to GPA points. I'm not doing + and - courses even though google says that can affect gpa.
        grade = grade.upper()
        grade_translation = {
            "A": 4.0,
            "B": 3.0,
            "C": 2.0,
            "D": 1.0,
            "F": 0.0
        }
        return grade_translation.get(grade, 0.0)

    def calculate_gpa(self):
        """Calculate cumulative GPA."""
        if self.total_credits == 0:
            return 0.0
        return self.total_points / self.total_credits

    def display_gpa(self):
        print(f"{self.first_name} {self.last_name}'s cumulative GPA is: {self.calculate_gpa():.2f}")

def main():
    # Main program
    first = input("Enter the student's first name: ")
    last = input("Enter the student's last name: ")

    student = Student(first, last)

    while True:
        credits = input("Enter course credits (or type 'done' to finish): ")
        if credits.lower() == "done":
            break
        try:
            credits = float(credits)
        except ValueError:
            print("Invalid input for credits. Please enter a number.")
            continue
        
        # Couldn't think of how to to the break above with the letter grade... This is janky but it works
        grade = "z"
        while grade == "z":
            grade = input("Enter the course grade (A, B, C, D, F): ")
            if grade.upper not in ("A", "B", "C", "D", "F"):
                print("This was not a valid course grade.")
                grade = "z"               
                
        student.add_course(credits, grade)

    # Display GPA
    student.display_gpa()

if __name__ == "__main__":
    # I did this a few programs ago and have left it in. It doesn't hurt but I don't think it's necessary unless this program is getting called..
    main()