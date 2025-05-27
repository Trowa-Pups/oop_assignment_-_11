#Convert Quiz Creator to OOP
import os 

class QuizCreator:
    def get_quiz_file(self): #Getting the quiz file
        self.quiz_file = None #To store the opened file

        quiz_number = str(input("Please input what quiz you are going to edit or create Ex.(quiz_#_1.txt): ")) #imported quiz_number from quiz creator

        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads") #imported downloads_folder from quiz creator

        file_path = os.path.join(downloads_folder, quiz_number) #imported file_path from quiz creator

        if os.path.exists(file_path): #Imported from quiz creator to check if the file is there or not
            print(f"{quiz_number}" + " will be opened")
            self.quiz_file = open(file_path, "a") #Changed to this for the previous one was not working


        else:
            print(f"{quiz_number}" + " does not exist") #If the file doesn't exist, then it will create it
            print("creating the file...")
            self.quiz_file = open(file_path, "w") 


    def questions_and_answers(self): #Imported the question and options in my quiz creator
        while True: #To make it a loop so that the user can put how much questions they want in the file
            question = str(input(f"Please input the new question, if done, type 'exit': ")) #Ask the user to input their question 

            if question.lower() == "exit": #If the user inputs "exit", make the program break and update the file with the new inputs of the user
                print("Exiting...")
                break

            #Ask the user to input four options, and input the correct answer
            option_a = input("Input option A of the question: ")
            option_b = input("Input option B of the question: ")
            option_c = input("Input option C of the question: ")
            option_d = input("Input option D of the question: ")

            if option_a == option_b or option_a == option_c or option_a == option_d or option_b == option_c or option_b == option_d or option_c == option_d:
                same_answer_detector = str(input("Same answer detected! Do you want to continue? Yes/No: "))
                if same_answer_detector.lower() == "no":
                    print("Exiting...")
                    break
                
            right_answer = input("Input the right answer Ex.(A): ").lower() #Used lower() to make sure that the letter is always the same

quiz_creator = QuizCreator()
quiz_creator.get_quiz_file()
quiz_creator.questions_and_answers()