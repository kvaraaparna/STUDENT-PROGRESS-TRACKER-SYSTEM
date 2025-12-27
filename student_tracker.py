#ENTERING THE STUDENT DETAIL BY USER
print("**----------------------------------**")
print("STUDENT PROGRESS TRACKER SYSTEM")
print("**----------------------------------**")           
print("\n")
name=input("Enter student name              : ")           #ENTER STUDENT NAME
classname=input("Enter class name                :")        #ENTER STUDENT CLASS NAME
roll_no=input("Enter student roll no           :")          #ENTER STUDENT ROLL NO
subject=int(input("Enter how many subject user want:"))     #ENTER HOW MANY SUBJECT USER WANT
overall_marks=subject*100
print("The overall marks for semester:",overall_marks)         #OVERALL MARKS OF SEMESTER
print("\n")
#CREATE A FUNCTION NAME TO PRINT THE USER (STUDENT) DETAILS EASILY
def student_details():
    failed_subject=0              #DECLARATION OF THE WANTED  OBJECTS
    passed_subject=0
    total_marks=0
    highest_marks=0
    lowest_marks=0
    gets_marks=[]
    marks_percentage=0
    marks=0
    for i in range(1,subject+1):               #USING FOR LOOP TO PRINT SUBJECTS AND THEIR MARKS
        while True:
            marks=int(input(f"The subject-{i} marks:"))
            
            #USING IF CONDITION TO CHECK ENTERED MARKS ARE LESSTHEN 100 AND GREATER THAN 0 AND SUBJECT PASS OR FAIIL

            if marks==0 or marks<100:   
                
                total_marks+=marks                            #TOTAL_MARKS ARRE USED TO CALCULATE THE HOW MANY MARKS USER GET NY OVERALL MARKS
                marks_percentage=total_marks/overall_marks*100
                gets_marks.append(marks)       
                print()
            
                if marks<35:
                    failed_subject=True
                else:
                    passed_subject=True
                break
            else:
                print("Enter a valid subject marks:")
                marks=int(input(f"The subject-{i} marks:"))
                gets_marks.append(marks)
            break
    average_marks=total_marks/subject               #CALCULATE THE AVERAGE MARKS OF THE STUDENT
    highest_marks=max(gets_marks)                    #CALCULATE THE HIGHEST MARKS OF AMONG THE SUBJECTS
    lowest_marks=min(gets_marks)                      #CALCULATE THE LOWEST MARKS OF AMONG THE SUBJECTS
    print("\n")
    
    #PRINNTING THE USER WANTS TO VIEW
         
    print("The student total marks:",total_marks)         #PRINTING THE TOTALMARKS OF THE STUDENT SUBJECT
    print("The student average marks:",average_marks)        #PRINTING THE AVERAGE MARKS OF THE STUDENT SUBJECT
    print("The highest marks subject is:",highest_marks)        #PRINTING THE HIGHEST MARKS OF THE STUDENT SUBJECT
    print("The lowest marks subject is:",lowest_marks)           #PRINTING THE LOWEST MARKS OF THE STUDENT SUBJECT
    print("The student marks percentage is:",marks_percentage)     #PRINTING THE  MARKS PERCENTAGE OF THE STUDENT SUBJECT
    print("\n")
    
 #CHECK THE GRADE CALCULATION
 
    print("GRADE CALCULATION:")     
    if average_marks>=90 :            #CHECK THE AVERAGE MARKS GREATER THAN OR EQAUL TO 90
        print("Grade-A")               
    elif average_marks>=75 :             #CHECK THE AVERAGE MARKS GREATER THAN OR EQAUL TO 75
        print("Grade-B")
    elif average_marks>=50 :                           #CHECK THE AVERAGE MARKS GREATER THAN OR EQAUL TO 50
                
        print("Grade-C")
    elif average_marks>=35 :             #CHECK THE AVERAGE MARKS GREATER THAN OR EQAUL TO 35
        print("Grade-D")
    else: 
        print("Fail")                  #CHECK THE AVERAGE MARKS WILL BE FAIL

    #PASS/FAIL LOGIC
    if failed_subject==True:
        result="FAIL"
    else:
        result="PASS"
#RETURN THE OBJECT SUED IN THE WHILE :TRUE CONDITION FOR  ACCESING IT
    
    return marks,total_marks,average_marks,gets_marks,marks_percentage,overall_marks,highest_marks,lowest_marks,passed_subject,failed_subject,result
marks,total_marks,average_marks,gets_marks,marks_percentage,overall_marks,highest_marks,lowest_marks,passed_subject,failed_subject,result=student_details()
print("\n")
#TAKE ANOTHER FUNCTION DEF STUDENT REPORT TO PRINT THE REPORT CARD
def student_report():

    print("*------------------*")
    print("STUDENT REPORT:")
    print("*------------------*")
    print("NAME            :",name.upper())          #PRINTING THE STUDENT NAME USING UPPER CASE
    print("CLASS_NAME      :",classname.upper())        #PRINTING THE STUDENT CLASS NAME USING UPPER CASE
    print("ROLL_NO         :",roll_no)                    #PRINTING THE STUDENT ROLL NO  
    print("TOTAL MARKS     :",total_marks)               #PRINTING THE TOTAL MARKS
    print("AVERAGE MARKS   :",average_marks)                #PRINTING THE AVERAGE MARKS
    print("MARKS PERCENTAGE:",marks_percentage)          #PRINTING THE MARKS PERCENTAGE
    print("RESULT       :",result)                     #PRINTING THE RESULT OF THE STUDENT PASS OR FAIL
    #USING RETURN STATEMENT TO CALL THE FUNCTION OBJECTS
    return name,classname,roll_no,total_marks,average_marks,marks_percentage,result
name,classname,roll_no,total_marks,average_marks,marks_percentage,result=student_report()
print("\n")
while True:
#PRINTING THE WHAT THE USER WANT TO DO NEXT.....?
    print("------------------------")
    print("What do you want to do next?")
    print("1. Enter marks again")
    print("2. View report again")
    print("3. Exit")
 
    choice=int (input("Enter your chioce between 1/2/3:"))         #CHOOSING THE CHOICE AMOND THE THREE STATEMENT BY USER
    if choice==1:                                 # IF USER CHOOSE 1 ITS AGAIN ASK  THE SUBJECT MARKS

        marks,total_marks,average_marks,gets_marks,marks_percentage,overall_marks,highest_marks,lowest_marks,passed_subject,failed_subject,result=student_details()
    elif choice==2:                                 # IF USER CHOOSE 2 ITS VEIW THE STUDENT REPORT AGAIN
        name,classname,roll_no,total_marks,average_marks,marks_percentage,result=student_report()
    elif choice==3:                                #IF USER CHOOSE THE 3 THE PROGRAM IS EXIT
        print("Exiting.... thank you")
        break
    else:                                #ELSE ASK THE USER VALID ENTER VALUE .......
        print("Enter a valid chioce:")