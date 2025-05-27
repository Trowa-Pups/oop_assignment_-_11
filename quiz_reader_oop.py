#Convert Quiz Reader to OOP
import os #Imported the imports i used to make it "astig" in the Quiz Reader to here 
import colorama #Importing it because i seen it in my yt feed and i thought i could use it to satisfy the "astig" factor
import random #Importing it because i need it to randomize the questions 
from colorama import Fore #Importing Fore to change text color
import time #Importing it to make a delay in the terminal to make the flow more natural

class Quiz_Reader: #Imported the get quiz file for it probably works the same in here
    def get_quiz_file(self): #Getting the quiz file
        self.quiz_file = None #To store the opened file

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
        right_answer_list = [] 
        question_list = [] #To store the questions to randomize later
        temporary_storage = "" #To temporary store the entire question

        for line in file_lines:
            line = line.strip() 

            if line.startswith("Question"): #To check if the line is the question
                temporary_storage += line + "\n" #To store the line in the temporary storage
    
            elif line.startswith("A:") or line.startswith("B:") or line.startswith("C:") or line.startswith("D:"): #To check if the line are the answers
                temporary_storage += line + "\n" #To store the line in the temporary storage

            elif line.startswith("Right Answer"): #To check if the line is the correct answer in the current question
                line = line.replace("Right Answer: ", "") #Removes the "Right Answer: " to make the answer remain 
                right_answer_list.append(line) #To store the answer in the list
                question_list.append(temporary_storage) #To store the question in the list
                temporary_storage = "" #To reset the temporary