# Test code for practice.

student = ["Jeferson", "Jacob", 32, [65, 50, 75, 90, 66]]
subjects = ["A", "B", "C", "D", "E"]
MENU = "OptionsL\n1. View\n2. Change User Data\n3. Calculate Grade Average]\n0. Quit\n: "
EDIT_MENU = "What would you like to Edit?\n1. Name\n2. Age\n3. Grade\n0. Back\n: "

while True:
    print("Editing profile of user:" , student[0], student[1])
    user_option = int(input(MENU))
    if user_option == 1:
        user_str = f"Name: {student[0]} {student[1]}\nAge: {student[2]}\n"
        user_str += "Subject\tGrade\n"
        for subject, grade in zip(subjects, student[3]):
            user_str += f"{subject}\t\t{grade}\n"
        print(user_str)
    elif user_option == 2:
        while True:
            edit_option = input(EDIT_MENU)
            if edit_option == "1":
                name = input("Please enter a new name: (press enter to leave unchanged)\n")
                student[0] = name if name else student[0]
                surname = input("Please enter a new surnace: (please enter to leave unchanged)\n")
                student[1] = surname if surname else student[1]
                print("Name updated!")
            elif edit_option == "2":
                while True:
                    age = input("Please enter a new age: ")
                    if age.isnumeric():
                        age = int(age)        
                        student[2] = age
                        break
                    else:
                        print("Unfortunately you have entered an invalid value")
            elif edit_option == "3":
                print("Please choose a subject to edit")
                for i, subject in enumerate(subjects, 1):
                    print(f"{i}, {subject}")
                subject = input(": ")
                if subject.isnumeric() and 0 < int(subject) <= len(subjects):
                    subject = int(subject) - 1
                grade = input("Please enter a new grade: ")
                student_grades = student[3]
                student_grades[subject] = grade
            elif edit_option == "0":
                break
    elif user_option == 3:
        total = 0
        for grade in student[3]:
            total  += grade 
        average = total/len(subjects)
        print(f"Student grade average: {average}")
    
    elif user_option == 0:
        print("Goodbye")
        break
    
    else:
        print("No option selected")


        
    