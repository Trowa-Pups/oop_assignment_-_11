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

        quiz_number = str(input(Fore.WHITE + "Please input what quiz you are going to edit or create Ex.(quiz_#_1.txt): ")) #imported quiz_number from quiz creator oop

        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads") #imported downloads_folder from quiz creator oop

        file_path = os.path.join(downloads_folder, quiz_number) #imported file_path from quiz creator oop

        self.read_question_lines(file_path)

    def read_question_lines(self, file_path):
        if os.path.exists(file_path): #To check if the file is there or not
            with open(file_path, "r" ) as file:
                print(Fore.WHITE, "Opening file...")
                time.sleep(1)
                file_lines = file.readlines() #Reads the lines of the file

            self.load_question_lines(file_lines)

        else:
            (Fore.RED , "File does not exit") #if the file doesnt exist

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

class QuizGame:
    def __init__(self):
        self.user_score = 0

    def introduction(self):
        print(Fore.LIGHTMAGENTA_EX + "Welcome to the Quiz!") #To welcome the user
        time.sleep(2)

        user_countinue = input("Would you like to take the quiz? Yes/No: ").lower() #To see if the user would countinue with the quiz
        time.sleep(0.5)

        if user_countinue == "yes":
            print(Fore.LIGHTCYAN_EX + "Let's go to the quiz!")

        else:
            print(Fore.LIGHTWHITE_EX + "Exiting program...") #If the user inputted no to exit the program
            return

    def quiz_start(self, question_list, right_answer_list):
        quiz_data = list(zip(question_list, right_answer_list)) #Using list(zip()) to correctly pair the question and answer and put it on a lis
        random.shuffle(quiz_data) 

        for question_number, (question, correct_answer) in enumerate(quiz_data): #Using enumerate to get the question number and get the question and correct answer from quiz_data
            print(Fore.WHITE + f"Question no.{question_number + 1}:\n {question}") #To prinnt the question
            user_answer = input("Please input your answer(Ex: A): ").lower() #using lower() to ensure every user input lines up with right answer

            if user_answer == correct_answer: #To line up to the question number
                print(Fore.LIGHTGREEN_EX + "Correct!")
                self.user_score += 1 #To add 1 point to the score
                time.sleep(1)
            
            else:
                print(Fore.LIGHTRED_EX + "Wrong!")
                time.sleep(1)

    def user_score_counter(self, question_list): #To see if the user passed or not
        print(Fore.LIGHTYELLOW_EX + "Calculating Score...")
        time.sleep(2)

        if self.user_score == len(question_list): #To see if user did a perfect job
            print(Fore.YELLOW + "\nYou got a perfect score!", Fore.GREEN + "💯 Congratulations!", Fore.YELLOW , self.user_score,  "/",len(question_list)) 

        elif self.user_score >= len(question_list): #To see if user passed
            print(Fore.YELLOW + "\nNice try! ❤ Better luck next time! 🍀", self.user_score,  "/",len(question_list))

        else: #The user failed
            print(Fore.YELLOW + "\nYou tried your best! Keep studying! 📖", self.user_score,  "/",len(question_list))
            
reader = QuizReader()
reader.get_quiz_file()
game = QuizGame()
game.quiz_start(reader.question_list, reader.right_answer_list)
game.user_score_counter(reader.question_list)