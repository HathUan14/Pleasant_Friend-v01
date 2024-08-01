import tkinter as tk
from tkinter import messagebox

quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Jupiter", "Saturn", "Mars", "Earth"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Go", "Au", "Ag", "Gd"],
        "answer": "Au"
    },
    {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "choices": ["China", "Japan", "South Korea", "Thailand"],
        "answer": "Japan"
    }
    # Add more questions here
]

# Function to display the current question and choices
def show_question():
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question +=1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")

# Configure the font size for the question and choice buttons

# Create the question label
qs_label = tk.Label(
    root,
    anchor="center",
    wraplength=500,
    padx=10,
    pady=10,
    font=("Helvetica", 20)
)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = tk.Button(
        root,
        command=lambda i=i: check_answer(i),
        font=("Helvetica", 16)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = tk.Label(
    root,
    anchor="center",
    padx=10,
    pady=10,
    font=("Helvetica", 20)
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = tk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padx=10,
    pady=10,
    font=("Helvetica", 20)
)
score_label.pack(pady=10)

# Create the next button
next_btn = tk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled",
    font=("Helvetica", 16)
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main event loop
root.mainloop()