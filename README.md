🐞 Software Bug Tracker

A simple Python-based console application to manage and track software bugs.
It allows reporting, assigning, updating, and deleting bugs while maintaining developer workload balance.

🚀 Features

Create Bug Reports: Add new bugs with details like project ID, type, severity, and description.

Assign Bugs: Automatically assigns developers based on severity using a decision-tree logic.

Display Bug Details: View full information about a specific bug.

Bug Summary by Project: Generate a summary of total and assigned bugs for a project.

Update Bug Status: Mark bugs as FIXED or IN PROCESS.

Delete Bugs: Remove bugs permanently from the tracker.

Developer Status: See the workload and status of bugs assigned to a developer.

Developer Balancing: Automatically assigns bugs to the developer with the least workload in their tier (senior, mid, junior).

🧑‍💻 Developer Allocation Rules

HIGH severity bugs → Assigned to Senior Developers

MID severity bugs → Assigned to Mid-level Developers

LOW severity bugs → Assigned to Junior Developers

Within each tier, the developer with minimum assigned bugs is selected.

📋 Menu Options
-------------------------------------------------------
|    1. CREATE A NEW BUG                              |
-------------------------------------------------------
|    2. ASSIGN A BUG                                  |
-------------------------------------------------------
|    3. DISPLAY BUG DETAILS                           |
-------------------------------------------------------
|    4. GENERATE BUG SUMMARY                          |
-------------------------------------------------------
|    5. UPDATE BUG STATUS                             |
-------------------------------------------------------
|    6. DELETE A BUG                                  |
-------------------------------------------------------
|    7. VIEW DEVELOPER LIST                           |
-------------------------------------------------------
|    8. DISPLAY DEVELOPER STATUS                      |
-------------------------------------------------------
|    9. EXIT                                          |
-------------------------------------------------------

⚙️ Requirements

Python 3.x

No external libraries required (uses only standard library time).

▶️ How to Run

Save the script as bug_tracker.py

Open a terminal in the same directory.

Run:

python bug_tracker.py


Follow the menu prompts to manage bugs.

📊 Example Console Flow
1️⃣ Creating a Bug
ENTER BUG ID     : 101
ENTER PROJECT ID : P001
SELECT THE TYPE OF BUG
->1.SYNTAX ERROR
->2.RUNTIME ERROR
->3.LOGICAL ERROR
...
ENTER YOUR CHOICE: 2

->1.LOW
->2.MID
->3.HIGH
ENTER YOUR CHOICE: 3

ENTER THE DESCRIPTION OF THE BUG: Application crashes on login

2️⃣ Assigning the Bug
ENTER THE BUG ID : 101
BUG 101 ASSIGNED TO DEVELOPER DEV1

3️⃣ Displaying Bug Details
BUG ID                : 101
BUG TYPE              : RUNTIME ERROR
RISK                  : HIGH
DESCRIPTION           : APPLICATION CRASHES ON LOGIN
STATUS                : REPORTED
PROJECT               : P001
TIME OF CREATION      : MON SEP  8 17:15:21 2025
ASSIGNED TO DEVELOPER : DEV1
START TIME            : MON SEP  8 17:16:05 2025
END TIME              : BUG NOT YET FIXED

4️⃣ Updating Bug Status
ENTER THE BUG ID TO BE UPDATED: 101
->1.FIXED
->2.IN PROCESS

ENTER YOUR CHOICE: 1
BUG '101' STATUS UPDATED SUCCESSFULLY.

5️⃣ Developer Status
ENTER DEVELOPER ID: Dev1
BUG_ID  DEV_ID   START TIME                 END TIME                   STATUS
101     Dev1     Mon Sep  8 17:16:05 2025   Mon Sep  8 17:20:44 2025   FIXED
NUMBER OF BUGS FIXED = 1
NUMBER OF BUGS IN PROCESS = 0
NUMBER OF BUGS REPORTED = 0

🗑️ Known Limitations

Data is stored in memory only (resets when program exits).

Input validation is basic (integer checks for IDs and menu choices).

Developer list in menu option 7 currently displays assigned bug IDs, not actual developer names (can be improved).

📌 Future Improvements

Add persistent storage (JSON or database).

Improve developer list view.

Provide analytics dashboards (e.g., bug fix time trends).
