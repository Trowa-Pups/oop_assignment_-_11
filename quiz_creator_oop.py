#Convert Quiz Creator to OOP
import os 

class QuizCreator:
    def get_quiz_file(self): #Getting the quiz file 
        quiz_number = str(input("Please input what quiz you are going to edit or create Ex.(quiz_#_1.txt): ")) #imported quiz_number from quiz creator

        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads") #imported downloads_folder from quiz creator

        file_path = os.path.join(downloads_folder, quiz_number) #imported file_path from quiz creator

        if os.path.exists(file_path): #Imported from quiz creator to check if the file is there or not
            print(f"{quiz_number}" + " will be opened")
            with open(file_path, "a") as file:

        else:
            print(f"{quiz_number}" + " does not exist") #If the file doesn't exist, then it will create it
            print("creating the file...")
            with open(file_path, "w") as file: