import random
import copy
import threading
import time

# invisible timer settings
TIME_LIMIT = 15  # seconds per question

# issues 
# do you want to exit again and again
# some design issue
#
questions_db = ["Enter your CGPA N", "sun sets in the S", "animals are : M", "Our college is : A"]
option_2_q_db = {
    "animals are : M": ["cow", "chair", "dog", "cat"],
    "Our college is : A": ["iitb", "iiitb", "reyansh college of hotel management", "baua don memorial"],
    "sun sets in the S": ["north", "south", "east", "west"]
}
ans_2_q_db = {
    "Enter your CGPA N": "4",
    "sun sets in the S": [4],
    "animals are : M": [1, 3, 4],
    "Our college is : A": "iiitb"
}  # for multiple correct and single correct only (to use the question string as a key)
questions_db_marks = ["4", "4", "4", "4"]
question_types = {"N": "Numerical", "S": "Single Correct", "M": "Multiple Choices", "A": "Short Answer"}


# ============ invisible timer helper ============

def input_with_timeout(prompt, timeout):
    """
    Asks for input but only waits timeout seconds.
    - Returns the input string if answered in time.
    - Returns None if time is up.
    No visible countdown, so no flicker.
    """
    answer = [None]
    done = threading.Event()

    def get_input():
        try:
            answer[0] = input(prompt)
        finally:
            done.set()

    t = threading.Thread(target=get_input, daemon=True)
    t.start()

    done.wait(timeout)

    if not done.is_set():
        print("\nTime's up!")
        return None

    return answer[0]


# ============ question mode ============

def question_mode():
    # 2 modes see the questions sorted and input questions
    print("1. View Question Database")
    print("2. Add Questions")
    # N = int(input("Select Mode: "))
    N = int(input("Select Mode:"))
    if (N == 1):   # display all the questions in the data base
        for index in range(len(questions_db)):
            print("--------------------- Questions-------------------------------")
            print(f" {index+1}.", end="")
            print(questions_db[index][:-1])
            print(" ")
            print(f"({question_types.get(questions_db[index][-1])})")

            if (questions_db[index][-1] == "S" or questions_db[index][-1] == "M"):
                print("--------------------- Options-------------------------------")
                option_list = option_2_q_db.get(questions_db[index])
                for j in range(len(option_list)):
                    print(f"{j+1}. {option_list[j]}")
            print("--------------------- Answers-------------------------------")
            if (questions_db[index][-1] == "S" or questions_db[index][-1] == "M"):
                ans_list = ans_2_q_db.get(questions_db[index])
                for j in range(len(ans_list)):
                    print(f"{j+1}. {ans_list[j]}")
            else:
                print(f"{ans_2_q_db.get(questions_db[index])}")
            print("----------------------------------------------------")
            print(" ")
    elif (N == 2):
        # add a mode to edit questions too
        run = "Y"
        while (run == "Y"):
            question_type = input("Choose a Question Type :(N,S,M,A)").upper()  # add a fail safe for junk values
            question_text = input("Enter Question Text :")  # a check for repeat questions
            question_marks = input("Enter Marks :")  # a check for repeat questions
            questions_db.append(question_text + question_type.upper())
            if (question_type == "S" or question_type == "M"):  # For S and M case 
                no_of_options = int(input("Enter the Number of options"))
                temp_options = []
                for i in range(no_of_options):  # gets all of the option
                    print("enter option num ", end="")
                    print(i+1)
                    option = input()
                    temp_options.append(option)
                options = (temp_options)
                option_2_q_db[question_text + question_type.upper()] = options
                no_of_ans = int(input("Enter the correct options"))
                temp_options = []
                for i in range(no_of_ans):  # gets the correct options (as a tuple)(run a loop to check each value)
                    print(f"Enter Option No.{i+1} ")
                    option = input()
                    temp_options.append(option)
                ans_2_q_db[question_text + question_type.upper()] = temp_options
            else:  # keep the same for (Numeric case too)
                invalid = 1
                while (invalid):
                    temp_answer = input("Enter the correct answer :").lower()
                    if (question_type == "N"):
                        if (temp_answer.isdigit() is True):
                            invalid = 0
                        else:
                            print("Please enter a number")
                    else:
                        invalid = 0
                    if (invalid == 0):
                        ans_2_q_db[question_text + question_type.upper()] = temp_answer
            runt = 1
            while (runt):  # ask for time 
                question_time = input("Set time limt")  # not used yet, but stored if you want later
                if (question_time.isdigit()):
                    question_time = int(question_time)
                    runt = 0
                else:
                    print("Input a valid value")
            questions_db_marks.append(question_marks)
            print(" ")
            run = input("Do you want continue (Press Y for yes)").upper()
    else:  # this is trigger need
        print("Please select a Valid mode ")


# ============ answer mode ============

def answer_mode():
    # make a deepcopy of all the questions
    question_non_random = copy.deepcopy(questions_db)
    marks_non_random = copy.deepcopy(questions_db_marks)
    question_random = []
    marks_random = []
    answer_submitted = {}

    # makes a list of random questions
    while (len(question_non_random)):
        i = random.randint(0, len(question_non_random)-1)
        marks_random.append(marks_non_random[i])
        question_random.append(question_non_random[i])
        del question_non_random[i]
        del marks_non_random[i]

    # displays the questions and asks for answers
    for i in range(len(question_random)):
        current_question = question_random[i]
        print(f"\nQ{i+1}. {current_question[:-2]}")
        print(f"{question_types.get(current_question[-1])}          Marks={marks_random[i]}")
        print(f"You have {TIME_LIMIT} seconds to answer this question.")  # <<< time limit message

        qtype = current_question[-1]

        if (qtype == "N" or qtype == "A"):
            # one timed attempt
            ans = input_with_timeout("Enter your answer: ", TIME_LIMIT)
            if ans is None:
                print("No answer submitted in time. Moving to next question.")
                continue

            ans = ans.lower()
            if qtype == "N" and not ans.isdigit():
                print("Invalid input (not a number). This will be treated as wrong.")
            answer_submitted[current_question] = ans

        else:  # for S and M case
            print(question_types.get(qtype))
            option_list = list(option_2_q_db.get(current_question))  # list of options    
            for j in range(len(option_list)):
                print(f"{j+1}. {option_list[j]}")
            print(f"there is/are {len(ans_2_q_db.get(current_question))} correct answer(s).")
            print("Enter your option numbers separated by spaces (e.g. 1 3 4).")

            ans_line = input_with_timeout("Your options: ", TIME_LIMIT)
            if ans_line is None:
                print("No answer submitted in time. Moving to next question.")
                continue

            temp_options = tuple(ans_line.split())
            answer_submitted[current_question] = temp_options

    # after all the questions are done show the answer
    for k, v in answer_submitted.items():
        print(f"Q{question_random.index((k))+1}. Your answer is {v} [ {marks_random[i]} marks ]", end=" ")
        print(" ")


# ============ main menu ============

def main_menu():
    Running = 1
    while (Running):
        N = input("Select a Mode")
        if (N == "1"):
            print("========================Questions Mode===========================")
            question_mode()
        elif (N == "2"):
            print("========================Answering Mode===========================")
            answer_mode()
        else:
            print("Input a valid mode")
            R = input("Do you want to exit ?(y/n)").lower()
            if (R == "y"):
                Running = 0


main_menu()
