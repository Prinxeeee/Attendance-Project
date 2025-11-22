records = {}

def take_attendance():
    while True:
        print("\n== MARK ATTENDANCE ==")
        stu = input("Student name (type STOP to go back): ").strip().lower()

        if stu == "stop":
            break

        mark = input("Present or Absent? (p/a): ").strip().lower()

        if mark == "p":
            records[stu] = "present"
        elif mark == "a":
            records[stu] = "absent"
        else:
            print("Wrong choice, try again.")

def show_records():
    print("\n== ATTENDANCE LIST ==")
    if len(records) == 0:
        print("No attendance added yet.")
        return

    for i in records:
        print(i,' -->' ,records[i])

def analyse_records():
    print("\n== SUMMARY ==")
    total = len(records)

    if total == 0:
        print("No data to analyse.")
        return

    present_count = list(records.values()).count("present")
    absent_count = total - present_count
    percentage = (present_count / total) * 100

    print("Total students :", total)
    print("Present        :", present_count)
    print("Absent         :", absent_count)
    print("Attendance %   :", round(percentage, 2))

def menu():
    while True:
        print("\n== MENU ==")
        print("1. Add attendance")
        print("2. Show all attendance")
        print("3. Attendance summary")
        print("4. Quit")

        opt = input("Choose between 1-4: ")

        if opt == "1":
            take_attendance()
        elif opt == "2":
            show_records()
        elif opt == "3":
            analyse_records()
        elif opt == "4":
            break
        else:
            print("Invalid option. Try again.")

menu()