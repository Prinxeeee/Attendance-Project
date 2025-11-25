# Attendance Tracker in Python

This is a small command-line program that helps in recording and viewing the attendance of students. It will be able to mark each student as present or absent, view the full list, and give a short summary displaying totals and a percentage.

## How it works

The program runs in a simple menu format. You can:

- Add attendance for any number of students  
- View all the records you added  
- Get a summary showing present count, absent count, and overall attendance percentage  

The data is stored in a dictionary during the course of program execution.

## How to run

- Install Python on your system.  
- Save the script in a file  
- Open your terminal or command prompt.  
- Run it using:

python attendance.py

## Menu options

Once the program has started, you should see:

== MENU ==

Add attendance

Show all attendance

Attendance Summary

Quit

Please choose an option by typing its number.

## Attendance inclusion

- Enter a student’s name  
- Type `p` for present or `a` for absent  
- Type `STOP` when you want to return to the main menu  

## Viewing records

The “Show all attendance” option lists each student and their status.

## Summary

The summary option shows:

- Total students  
- How many are present  
- How many are absent  
- Attendance percentage  

## Example output

== LIST OF ATT
rahul --> present
neha --> absent

== SUMMARY ==
Total students : 2
Present : 1
Absent : 1
Attendance % : 50.0

