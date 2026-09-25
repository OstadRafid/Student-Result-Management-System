def Display_Student_Information(Student_Name,Student_ID,Departmnet):
    print()
    print("-----------------------------------------")
    print("<===== Student Information =====>")
    print(f"Student Name -> {Student_Name}")
    print(f"Student ID -> {Student_ID}")
    print(f"Department -> Department of {Departmnet}")
    print("-----------------------------------------")

def Display_Subject_Marks(Marks):
    print()
    print("-----------------------------------------")
    print("<===== Subject Marks =====>")
    for key, val in Marks.items():
        print(f"{key} => {val}")

def Display_Calculate_Result(Marks):
    print()
    print("<===== Calculate Result =====>")
    Total_Marks = 0
    for i in List:
        Total_Marks = Total_Marks+i

    print(f"Total Marks -> {Total_Marks}")

    Avg_mark = Total_Marks / count

    print(f"Average Marks -> {Avg_mark:.2f}")

    print(f"Highest Mark -> {Max_Mark}")

    print(f"Lowest Marks -> {Minimum_Marks}")
    print()
    print("-----------------------------------------")

def Grade_Calculation(Marks):
    print()
    print("-----------------------------------------")
    print("<===== Grade Calculation =====>")
    Total_Marks = 0

    for i in List:
        Total_Marks = Total_Marks+i

    Avg_Mark = Total_Marks/count_3

    if (Avg_Mark >= 80 and Avg_Mark <= 100):
        print("Grade Point => A+")
    elif(Avg_Mark >= 70 and Avg_Mark <=79):
        print("Grade Point => A")
    elif(Avg_Mark >= 60 and Avg_Mark <=69):
        print("Grade Point => A-")
    elif(Avg_Mark >= 50 and Avg_Mark <=59):
        print("Grade Point => B")
    elif(Avg_Mark >= 40 and Avg_Mark <=49):
        print("Grade Point => C")
    else:
        print("Grade Point => C")
    print()
    print("-----------------------------------------")

def Status_of_Passing(Marks):
    print()
    print("-----------------------------------------")
    print("<===== Status of Passing =====>")

    found = 0
    
    for i in List_1:
        if (i < 40):
            found = 1
            break

    if found == 0:
        print(f"Student ID |( {Student_ID} )|-> is Passed")
    elif found == 1:
        print(f"Student ID |( {Student_ID} )|-> Is Failed")
    else:
        print("Absent In Examination.")
    print()
    print("-----------------------------------------")
    
while True:
    print()
    print("<========== Student Result Management System ==========>")
    print()
    print("1.Student Information")
    print("2.Subject Marks")
    print("3.Calculate Result")
    print("4.Grade Calculation")
    print("5.Pass or Fail")
    print("6.Password Verification")
    print("7.String Operations")
    print("8.Set Example")
    print("9.Tuple Example")
    print("10.Final Report")
    print()

    Number = int(input("Enter Case Number -> "))

    match Number:

        case 1:
            Student = {}

            print()

            Student_Name = input("Enter Student Name -> ")

            Student_ID = input("Enter Student ID -> ")

            Department = input("Enter Department Name -> ")

        case 2:
            List = ["Python", "Math", "English", "Physics", "ICT"]

            Marks = {}

            print()

            print("<===== Enter All Subject's Mark =====>")

            print()

            for marks in List:
                Marks[marks] = int(input(f"{marks} => "))

        case 3:

            List = list(Marks.values())

            Count_1 = list(Marks.keys())

            count = 0

            for i in Count_1:
                count+=1

            Max_Mark = max(Marks.values())

            Minimum_Marks = min(Marks.values())

        case 4:

            List = list(Marks.values())
            
            Count_2 = list(Marks.keys())
            
            count_3 = 0
            
            for i in Count_1:
                count_3+=1

        case 5:

            List_1 = list(Marks.values())

        case 6:
            while True:
                User_Input = input("ENTER PASSWORD => ")
                
                if User_Input == "python123":
                    print("Correct Password.✔️")
                    break
                else:
                    print("Invalid Password❌ |Try Again.")

        case 7:
            print()
            print("<====== String Operations ======>")
            print()
            print("1.Student Name In Uppercase")
            print("2.Student Name In Lowercase")
            print("3.Length of The Student Name")
            print("4.First Three Characters")
            print("5.Last Three Characters")
            print()

            Choice = int(input("ENTER YOUR CHOICE -> "))

            match Choice:

                case 1:
                    print()
                    print(f"Student Name In Uppercase -> {Student_Name.upper()}")
                case 2:
                    print()
                    print(f"Student Name In Lowercase -> {Student_Name.lower()}")
                case 3:
                    print()
                    Length = len(Student_Name)
                    print(f"Length of The Student Name -> {Length}")
                case 4:
                    print()
                    print(f"Frist Three Character -> {Student_Name[:3]}")
                case 5:
                    print()
                    print(f"Last Three Characters -> {Student_Name[-3:]}")

        case 8:
            print()
            print("<====== Set Example ======>")
            print()
            sports = {"Football", "Cricket", "Badminton"}
            clubs = {"Programming", "Cricket", "Photography"}

            Result_1 = sports.union(clubs)
            print(f"Common Items -> {Result_1}")

            Result_2 = sports.intersection(clubs)
            print(f"All Unique Item's -> {Result_2}")

        case 9:
            print()
            print("<====== Tuple Example ======>")
            print()
            Days = ("Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday")

            for i in Days:
                New_tuple = Days[0]
                break
            print(f"First Day -> {New_tuple}")

            for i in Days:
                New_tuple_1 = Days[6]
                break
            print(f"Last Day -> {New_tuple_1}")

            Langth = len(Days)

            print(f"Total Number of Days -> {Langth}")
        case 10:
            print("========================================")
            print("|           STUDENT REPORT             |")
            print("========================================")
            Display_Student_Information(Student_Name,Student_ID,Department)
            Display_Subject_Marks(Marks)
            Display_Calculate_Result(Marks)
            Grade_Calculation(Marks)
            Status_of_Passing(Marks)
"""
Md.Rafid Al Mahmud
Department of Software Engineer
Daffodil International Univarsity
Contact: rezaulkhansha@gmail.com
"""