records = {}
def takeattend():
    while True:
        print("== MARK ATTENDANCE ==")
        x = input("Student name (type STOP to go back): ").lower()

        if x == "stop":
            break

        y = input("Present or Absent? (p/a): ").lower()

        if y == "p":
            records[x] = "present"
        elif y == "a":
            records[x] = "absent"
        else:
            print("Wrong choice, try again")

def show_rec():
    print("== ATTENDANCE LIST ==")
    if len(records) == 0:
        print("No attendance added yet")
        return

    for i in records:
        print(i,' -->' ,records[i])

def analyse_records():
    print("\n== SUMMARY ==")
    t = len(records)

    if t == 0:
        print("No data to analyse")
        return

    pc = list(records.values()).count("present")
    ac = t - pc
    percentage = (pc/t)*100

    print("Total students :", t)
    print("Present        :", pc)
    print("Absent         :", ac)
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
            takeattend()
        elif opt == "2":
            show_rec()
        elif opt == "3":
            analyse_records()
        elif opt == "4":
            break
        else:
            print("Invalid option, Try again")
menu()

