#Convert Quiz Reader to OOP
import os #Imported the imports i used to make it "astig" in the Quiz Reader to here 
import colorama #Importing it because i seen it in my yt feed and i thought i could use it to satisfy the "astig" factor
import random #Importing it because i need it to randomize the questions 
from colorama import Fore #Importing Fore to change text color
import time #Importing it to make a delay in the terminal to make the flow more natural

class QuizReader: #Imported the get quiz file for it probably works the same in here
    def __init__(self): #Researched about __init__ and decided to use it 
        self.quiz_file = None #To store the opened file

        self.right_answer_list = [] #To store the right answers

        self.question_list = [] #To store the questions to randomize later


    def get_quiz_file(self): #Getting the quiz file

        quiz_number = str(input("Please input what quiz you are going to edit or create Ex.(quiz_#_1.txt): ")) #imported quiz_number from quiz creator oop

        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads") #imported downloads_folder from quiz creator oop

        file_path = os.path.join(downloads_folder, quiz_number) #imported file_path from quiz creator oop

        self.read_question_lines(file_path)

    def read_question_lines(self, file_path):
        if os.path.exists(file_path): #To check if the file is there or not
            with open(file_path, "r" ) as file:
                file_lines = file.readlines() 

        self.load_question_lines(file_lines)

    def load_question_lines(self, file_lines): #Imported tons of the part from Quiz Reader to here to make it have similar functions
        temporary_storage = "" #To temporary store the entire question

        for line in file_lines:
            line = line.strip() 

            if line.startswith("Question"): #To check if the line is the question
                temporary_storage += line + "\n" #To store the line in the temporary storage
    
            elif line.startswith("A:") or line.startswith("B:") or line.startswith("C:") or line.startswith("D:"): #To check if the line are the answers
                temporary_storage += line + "\n" #To store the line in the temporary storage

            elif line.startswith("Right Answer"): #To check if the line is the correct answer in the current question
                line = line.replace("Right Answer: ", "") #Removes the "Right Answer: " to make the answer remain 
                self.right_answer_list.append(line) #To store the answer in the list
                self.question_list.append(temporary_storage) #To store the question in the list
                temporary_storage = "" #To reset the temporary

        else:
            print("Quiz file not found")

class QuizGame:
    def __init__(self):
        self.user_score = 0

    def introduction(self):
        print("Welcome to the Quiz!") #To welcome the user
        user_countinue = input("Would you like to take the quiz? Yes/No: ").lower() #To see if the user would countinue with the quiz
        if user_countinue == "yes":
            print("Let's go to the quiz!")

        else:
            print("Exiting program...") #If the user inputted no to exit the program
            return

    def quiz_start(self, question_list, right_answer_list):
        random.shuffle(question_list, right_answer_list) #To shuffle the question list and right answer list to make it completely randomized

        for question_number in enumerate(question_list): #Using enumerate to get the question number and get the question and correct answer from quiz_data
            print(f"Question no.{question_number + 1}:\n {question_list}") #To prinnt the question
            user_answer = input("Please input your answer(Ex: A): ").lower() #using lower() to ensure every user input lines up with right answer

            if user_answer == right_answer_list[question_number]: #To line up to the question number
                print("Correct!")
                self.user_score += 1 #To add 1 point to the score
            
            else:
                print("Wrong!")

    def user_score_counter(self, question_list): #To see if the user passed or not

        if self.user_score == len(question_list): #To see if user did a perfect job
            print("You got a perfect score!", self.user_score,  "/",len(question_list)) 

        elif self.user_score >= len(question_list): #To see if user passed
            print("You passed!", self.user_score,  "/",len(question_list))

        else: #The user failed
            print("You failed, unfortunately", self.user_score,  "/",len(question_list))
            
reader = QuizReader()
reader.get_quiz_file()
game = QuizGame()
game.quiz_start(reader.question_list, reader.right_answer_list)
