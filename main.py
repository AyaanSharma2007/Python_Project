import random
import copy
#issues 
# do you want to exit again aanf again
#some desgin issue
#
questions_db=["Enter your CGPN"]
option_2_q_db={}
ans_2_q_db={"Enter your CGPN":"4"}#for mutiple correct and single correct only (to use the quesiton string as a key)
questions_db_marks=["4"]
question_types={"N":"Numerical","S":"Single Correct","M":"Multiple Choices","A":"Short Answer"}

def question_mode():
    #2 modes see the quesitons sorted and input questions
    N=int(input("Select Mode:"))
    if(N==1):   #display all the questions in the data base
        for index in range(len(questions_db)):
            print("--------------------- Questions-------------------------------")
            print(f" {index+1}.",end="")
            print(questions_db[index][:-1])
            print(" ")
            print(f"({question_types.get(questions_db[index][-1])})")
            
            if (questions_db[index][-1]=="S" or questions_db[index][-1]=="M"):# its is unable to get that tupple so either its not storing it or its being made
                print("--------------------- Options-------------------------------")
                option_list=option_2_q_db.get(questions_db[index])   
                for j in range(len(option_list)):
                    print(f"{j+1}. {option_list[j]}")
            print("--------------------- Answers-------------------------------")
            if (questions_db[index][-1]=="S" or questions_db[index][-1]=="M"):
                ans_list=ans_2_q_db.get(questions_db[index])
                for j in range(len(ans_list)):
                    print(f"{j+1}. {ans_list[j]}")
            else :
                print(f"{ans_2_q_db.get(questions_db[index])}")    
            print("----------------------------------------------------")    
            print(" ")   
    elif(N==2):
        # add a mode to edit questions too
        run="Y"
        while(run=="Y") :
            question_type=input("Choose a Question Type :(N,S,M,A)").upper()#add a fail safe for junk values
            question_text=input("Enter Question Text :")# a check for repeat questions
            question_marks=input("Enter Marks :")# a check for repeat questions
            questions_db.append(question_text+question_type.upper())
            if(question_type=="S" or question_type=="M"):# For S and M case 
                no_of_options=int(input("Enter the Number of options"))
                temp_options=[]
                for i in range(no_of_options):#gets all of the option
                    print("enter option num ",end="")
                    print(i+1)
                    option=input()
                    temp_options.append(option)
                options=(temp_options)
                option_2_q_db[question_text+question_type.upper()]=options
                no_of_ans=int(input("Enter the correct options"))   
                temp_options=[]
                for i in range(no_of_ans):# getes the correct options (as a tuple)(run a loop to check each value)
                    print(f"Enter Option No.{i+1} ")
                    option=input()
                    temp_options.append(option)
                ans_2_q_db[question_text+question_type.upper()]=temp_options
            else:#keep the same for (Numberic case too)
                invalid=1
                while(invalid):
                    temp_answer=input("Enter the correct answer :").lower()
                    if (question_type=="N") :
                        if (temp_answer.isdigit() is True):
                            invalid=0
                        else:
                            print("Please enter a number")
                    else:
                        invalid=0
                    if(invalid==0):
                        ans_2_q_db[question_text+question_type.upper()]=temp_answer
            runt=1
            while(runt):#ask for time 
                question_time=input("Set time limt")# add a number to ask for no time limit in that question
                if(question_time.isdigit()):
                    question_time=int(question_time)
                    runt=0
            # code getting the answer part
                else:
                    print("Input a valid value")            
            questions_db_marks.append(question_marks)
            print(" ")
            run=input("Do you want continue (Press Y for yes)").upper()
    else:#this is trigger need
        print("Please select a Valid mode ")
def answer_mdoe():
    #make a deepcopy of all the questions
    question_non_random=copy.deepcopy(questions_db)
    marks_non_random=copy.deepcopy(questions_db_marks)
    question_random=[]
    marks_random=[]
    answer_submitted={}
    while(len(question_non_random)):# makes a list of random questiions
        i=random.randint(0,len(question_non_random)-1)
        marks_random.append(marks_non_random[i])
        question_random.append(question_non_random[i])
        del question_non_random[i]
        del marks_non_random[i]
    for i in range(len(question_random)):# displays the questions and asks for answers
        current_question=question_random[i]
        print(f"Q{i+1}. {current_question[:-2]}")
        print(f"{question_types.get(current_question[-1])}          Marks={marks_random[i]}")   
        if(current_question[-1]=="N"or current_question[-1]=="A"):
            invaid=1
            while(invaid):
                ans=input("Enter your answer").lower()
                if (current_question[-1]=="N") :
                    if (ans.isdigit() is True):
                            invaid=0
                    else:
                            print("Please enter a number")
                else:
                        invaid=0
                if (invaid==0):
                    answer_submitted[current_question]=ans
        else :# for s and M case
            print(question_types.get(current_question[-1])) 
            option_list=[]
            option_list=option_2_q_db.get(current_question)#weird way the code is storting    
            for j in range(len(option_list)):
                print(f"{j+1}. {option_list[j]}")
            temp_options=[]
            for j in range(len(ans_2_q_db.get(current_question))): #for now you the correct number of answers
                print(f"Enter Option No.{j+1} ")
                temp_options.append(input())
            temp_options=tuple(temp_options)
            answer_submitted[current_question]=temp_options
    #after all the questions are done show the answer
    for k,v in answer_submitted.items():
        print(f"Q{question_random.index((k))+1}. Your answer is {v} ({marks_random[i]})")
        print(" ")
    #  do you wish to submit 
def main_menu():
    Running=1
    while(Running):
        N=input("Select a Mode")
        if (N=="1"):
            print("========================Questions Mode===========================")
            question_mode()
        elif (N=="2"):
            print("========================Answering Mode===========================")
            answer_mdoe()
        else:
            print("Input a valid mode")
        R=input("Do you want to exit ?").lower()
        if (R=="y"):
            Running=0
main_menu()
