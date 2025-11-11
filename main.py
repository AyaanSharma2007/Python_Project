import random
import copy

questions_db=["Enter your CGPN"]
option_2_q_db={}
ans_2_q_db={"Enter your CGPN":"4"}#for mutiple correct and single correct only (to use the quesiton string as a key)
questions_db_marks=["4"]
question_types={"N":"Numerical","S":"Single Correct","M":"Multiple Choices","A":"Short Answer"}
def printQ(a):#can i use a lambda here
    print(a[:-2],end=" ")
def question_mode():
    #2 modes see the quesitons sorted and input questions
    N=int(input("Sele ct Mode:"))
    if(N==1):   #display all the questions in the data base
        for index in range(len(questions_db)):
            print(f" {index+1}.",end="")
            printQ(questions_db[index])
            print(" ")
            print(f"({question_types.get(questions_db[index][-1])})")
            print("----------------------------------------------------")
            print(" ")
        pass#display mode
    if(N==2):
        # add a mode to edit questions too
        run="Y"
        while(run=="Y") :
            question_type=input("Choose a Question Type :(N,S,M,A)")#add a fail safe for junk values
            question_text=input("Enter Question Text :")# a check for repeat questions
            if(question_type=="S" or question_type=="M"):
                no_of_options=int(input("Enter the Number of options"))
                temp_options=[]
                for i in range(no_of_options):
                    print(f"Enter Option No.{i+1} ")
                    temp_options[i]=input()
                temp_options=tuple(temp_options)
                option_2_q_db[question_text]=temp_options
                no_of_ans=int(input("Enter the correct options"))
                temp_options=[]
                for i in range(no_of_options):
                    print(f"Enter Option No.{i+1} ")
                    temp_options[i]=input()
                temp_options=tuple(temp_options)
                ans_2_q_db[question_text]=temp_options
            else:#keep the same for (Numberic case too)
                temp_answer=input("Enter the correct answer :").lower()
                ans_2_q_db[question_text]=temp_answer
            runt=1
            while(runt):#ask for time 
                question_time=input("Set time limt")# add a number to ask for no time limit in that question
                if(question_time.isdigit()):
                    question_time=int(question_time)
                    runt=0
            # code getting the answer part
                else:
                    print("Input a valid value")
            questions_db.append(question_text+question_type.upper())
            print(" ")
            run=input("Do you want continue (Press Y for yes)").upper()
    else:
        print("Please select a Valid mode ")
def answer_mdoe():
    #make a deepcopy of all the questions
    question_non_random=copy.deepcopy(questions_db)
    marks_non_random=copy.deepcopy(questions_db_marks)
    question_random=[]
    marks_random=[]
    answer_submitted={}
    while(len(question_non_random)):
        i=random.randint(0,len(question_non_random)-1)
        marks_random.append(marks_non_random[i])
        question_random.append(question_non_random[i])
        del question_non_random[i]
        del marks_non_random[i]
    for i in range(len(question_random)):
        print(f"Q{i+1}. {question_random[i][:-2]}")
        print(question_types.get(question_random[i][-1]))    
        ans=input("Enter your answer")#for n and A case
        answer_submitted[question_random[i]]=ans
1
