#Convert Quiz Reader to OOP
import os #Imported the imports i used to make it "astig" in the Quiz Reader to here 
import colorama #Importing it because i seen it in my yt feed and i thought i could use it to satisfy the "astig" factor
import random #Importing it because i need it to randomize the questions 
from colorama import Fore #Importing Fore to change text color
import time #Importing it to make a delay in the terminal to make the flow more natural

class Quiz: #Imported the get quiz file for it probably works the same in here
    def get_quiz_file(self): #Getting the quiz file
        self.quiz_file = None #To store the opened file

        quiz_number = str(input("Please input what quiz you are going to edit or create Ex.(quiz_#_1.txt): ")) #imported quiz_number from quiz creator oop

        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads") #imported downloads_folder from quiz creator oop

        file_path = os.path.join(downloads_folder, quiz_number) #imported file_path from quiz creator oop

