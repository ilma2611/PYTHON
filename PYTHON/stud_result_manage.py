student = {}

while True:
    print("\n----STUDENT MANAGER APP-----")
    print("1. add student")
    print("2. add View Student")
    print("3. cheak result")
    print("4. add exit")

    choice = input("enter your choice: ")

    #add student
    if choice == "1":
        name = input("enter student name:")
        marks = int(input("enter marks: "))
        student[name] = marks
        print(f"{name}added") 

    #view student
    elif choice == "2":
        if not student:
            print("no student found!")
        else:
            for name, marks in student.iteams():
                print(name, ":", marks)

    #cheack result
    elif choice == "3":
        name = input("enter name:")
        if name in student:
            marks = student[name]

            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")

        else:
            print("NOT FOUND!")
    #exit
    elif choice == "4":
        print("Exiting....")
        break
    else: 
        print("invalid") 
        