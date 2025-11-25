#Attendance Tracker (Python)

This is a small command-line program that helps record and view student attendance. It lets you mark each student as present or absent, shows the full list, and gives a short summary with totals and percentage.

How it works

The program runs in a simple menu format. You can:

Add attendance for any number of students

View all the records you added

Get a summary showing present count, absent count, and overall attendance percentage

The data is stored in a dictionary while the program is running.

How to run

Install Python on your system.

Save the script in a file

Open your terminal or command prompt.

Run it using:

python attendance.py

Menu options

When the program starts, you will see:

== MENU ==
1. Add attendance
2. Show all attendance
3. Attendance summary
4. Quit


Choose an option by typing the number.

Adding attendance

Enter a student’s name

Type p for present or a for absent

Type STOP when you want to return to the main menu

Viewing records

The “Show all attendance” option displays each student along with their status.

Summary

The summary option shows:

Total students

How many are present

How many are absent

Attendance percentage

Example output
== ATTENDANCE LIST ==
rahul --> present
neha --> absent

== SUMMARY ==
Total students : 2
Present        : 1
Absent         : 1
Attendance %   : 50.0

