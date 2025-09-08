import time

bugs = {}
assignments = {}

# Example developer pools
developers = {
    'senior': ['Dev1', 'Dev2'],
    'mid': ['Dev3', 'Dev4'],
    'junior': ['Dev5', 'Dev6']
}

def create_bug_report(bug_id):
    if bug_id in bugs:
        print("BUG ID ALREADY EXISTS")
        return
    else:
        project_id = input("ENTER PROJECT ID : ")
        print("SELECT THE TYPE OF BUG")
        bug_type = type_of_bug()
        severity = bug_severity()  # Get the severity
        description = input("ENTER THE DESCRIPTION OF THE BUG: ")
        print()
        status = "REPORTED"
        currtime = time.asctime()
        bugs[bug_id] = {
            'project_id': project_id,
            'bug_type': bug_type,
            'severity': severity,  # Storing severity
            'description': description,
            'status': status,
            'currtime': currtime
        }

        # Automatically assign the bug to a developer
        severity = bugs[bug_id]['severity']
        dev_id = find_developer(severity)  # Use decision tree to find the developer based on severity
        if dev_id:
            start_time = time.asctime()
            assignments[bug_id] = {
                'dev_id': dev_id,
                'start_time': start_time,
                'end_time': None
            }
            print(f"BUG {bug_id} ASSIGNED TO DEVELOPER {dev_id}\n")
        else:
            print(f"NO AVAILABLE DEVELOPER FOR {severity} LEVEL BUGS. BUG {bug_id} WILL REMAIN UNASSIGNED.\n")

def find_developer(severity):
    # Decision Tree Logic to Assign Developer Based on Severity
    if severity == 'HIGH':
        available_devs = developers['senior']
    elif severity == 'MID':
        available_devs = developers['mid']
    else:
        available_devs = developers['junior']

    # Find the developer with the least assigned bugs in their category
    dev_load = {dev: 0 for dev in available_devs}
    
    for bug_id, details in assignments.items():
        dev_id = details['dev_id']
        if dev_id in dev_load:
            dev_load[dev_id] += 1
    
    min_load_dev = min(dev_load, key=dev_load.get, default=None)
    
    return min_load_dev

def display_bugs(bug_id):
    if bug_id in bugs:
        bug_details = bugs[bug_id]
        print(f"\nBUG ID                : {bug_id}")
        print(f"BUG TYPE              : {bug_details['bug_type']}")
        print(f"RISK                  : {bug_details['severity']}")  # Display severity
        print(f"DESCRIPTION           : {(bug_details['description']).upper()}")
        print(f"STATUS                : {bug_details['status']}")
        print(f"PROJECT               : {(bug_details['project_id']).upper()}")
        print(f"TIME OF CREATION      : {(bug_details['currtime']).upper()}")

        if bug_id in assignments:
            assignment_details = assignments[bug_id]
            print(f"ASSIGNED TO DEVELOPER : {(assignment_details['dev_id']).upper()}")
            print(f"START TIME            : {(assignment_details['start_time']).upper()}")
            if assignment_details['end_time']:
                print(f"END TIME              : {(assignment_details['end_time']).upper()}")
            else:
                print("END TIME              : BUG NOT YET FIXED")
    else:
        print(f"BUG {bug_id} DOES NOT EXIST")
    print()

def generate_bug_summary(project_id):
    total_bugs = 0
    assigned_count = 0
    for bug_id, bug_details in bugs.items():
        if bug_details['project_id'] == project_id:
            total_bugs += 1
            if bug_id in assignments:
                assigned_count += 1
    print(f"BUG SUMMARY FOR PROJECT: {project_id}")
    print(f"TOTAL BUGS REPORTED    : {total_bugs}")
    print(f"TOTAL BUGS ASSIGNED    : {assigned_count}")
    print()

def update_bug(bug_id, upd_time):
    if bug_id in assignments:
        if bug_id in bugs:
            print("->1.FIXED\n->2.IN PROCESS\n")
            cho = int(input("ENTER YOUR CHOICE: "))
            if cho == 1:
                status_update = "FIXED"
                end_time = upd_time
                assignments[bug_id]['end_time'] = end_time
                bugs[bug_id]['status'] = status_update
            elif cho == 2:
                status_update = "IN PROCESS"
            else:
                print("ENTER CORRECT CHOICE")
            bugs[bug_id]['status'] = status_update
            print(f"BUG '{bug_id}' STATUS UPDATED SUCCESSFULLY.\n")
        else:
            print(f"BUG WITH ID {bug_id} NOT FOUND.")
    else:
        print("BUG NOT YET ASSIGNED")

def delete_bug(bug_id):
    if bug_id in bugs:
        del bugs[bug_id]
        if bug_id in assignments:
            del assignments[bug_id]
        print(f"BUG WITH ID {bug_id} DELETED SUCCESSFULLY.")
    else:
        print(f"BUG WITH ID {bug_id} NOT FOUND.")

def type_of_bug():
    while True:
        print("->1.SYNTAX ERROR\n->2.RUNTIME ERROR\n->3.LOGICAL ERROR\n->4.NAME ERROR\n->5.TYPE ERROR\n->6.INDEX ERROR\n->7.ATTRIBUTE ERROR")
        choice = int(input("ENTER YOUR CHOICE: "))
        print()
        if choice == 1:
            return "SYNTAX ERROR"
        elif choice == 2:
            return "RUNTIME ERROR"
        elif choice == 3:
            return "LOGICAL ERROR"
        elif choice == 4:
            return "NAME ERROR"
        elif choice == 5:
            return "TYPE ERROR"
        elif choice == 6:
            return "INDEX ERROR"
        elif choice == 7:
            return "ATTRIBUTE ERROR"
        else:
            print("INVALID CHOICE...TRY AGAIN")

def bug_severity():
    while True:
        print("->1.LOW\n->2.MID\n->3.HIGH")
        choice = int(input("ENTER YOUR CHOICE: "))
        print()
        if choice == 1:
            return "LOW"
        elif choice == 2:
            return "MID"
        elif choice == 3:
            return "HIGH"
        else:
            print("INVALID CHOICE...TRY AGAIN")

def disp_dev_status():
    fix_count = 0
    inp_count = 0
    rep_count = 0
    flag = False
    d_id = input("ENTER DEVELOPER ID: ")
    for bug_id, dev_details in assignments.items():
        if d_id == dev_details['dev_id']:
            flag = True
            break
    if flag:
        print("BUG_ID  DEV_ID \tSTART TIME\t\t\tEND TIME\t\t\t\tSTATUS")
        for bug_id, dev_details in assignments.items():
            if d_id == dev_details['dev_id']:
                status = bugs.get(bug_id, {}).get('status', 'Bug not found')
                print(f"{bug_id}\t{dev_details['dev_id']}\t{dev_details['start_time']}\t{dev_details['end_time'] if dev_details['end_time'] else 'Bug not fixed yet'}\t{status}")
                if status == "FIXED":
                    fix_count += 1
                elif status == "IN PROCESS":
                    inp_count += 1
                elif status == "REPORTED":
                    rep_count += 1
        print(f"NUMBER OF BUGS FIXED = {fix_count}")
        print(f"NUMBER OF BUGS IN PROCESS = {inp_count}")
        print(f"NUMBER OF BUGS REPORTED = {rep_count}")
    else:
        print("DEVELOPER NOT ASSIGNED WITH ANY BUG")

print("\n*SOFTWARE BUG TRACKER\n")
while True:
    print("-------------------------------------------------------")
    print("|\t\t1. CREATE A NEW BUG                   |")
    print("-------------------------------------------------------")
    print("|\t\t2. DISPLAY BUG DETAILS                |")
    print("-------------------------------------------------------")
    print("|\t\t3. GENERATE BUG SUMMARY               |")
    print("-------------------------------------------------------")
    print("|\t\t4. UPDATE BUG STATUS                  |")
    print("-------------------------------------------------------")
    print("|\t\t5. DELETE A BUG                       |")
    print("-------------------------------------------------------")
    print("|\t\t6. DISPLAY DEVELOPER STATUS           |")
    print("-------------------------------------------------------")
    print("|\t\t7. EXIT                               |")
    print("-------------------------------------------------------")
    ch = int(input("ENTER YOUR CHOICE: "))
    print()
    if ch == 1:
        try:
            bug_id = int(input("ENTER BUG ID     : "))
            create_bug_report(bug_id)
        except ValueError:
            print("BUG ID SHOULD BE OF TYPE INTEGER")
    elif ch == 2:
        try:
            bug_id = int(input("ENTER BUG ID : "))
            display_bugs(bug_id)
        except ValueError:
            print("BUG ID SHOULD BE OF TYPE INTEGER")
    elif ch == 3:
        project_id = input("ENTER THE PROJECT ID: ")
        generate_bug_summary(project_id)
    elif ch == 4:
        try:
            bug_id = int(input("ENTER THE BUG ID TO BE UPDATED: "))
            upd_time = time.asctime()
            update_bug(bug_id, upd_time)
        except ValueError:
            print("BUG ID SHOULD BE OF TYPE INTEGER")
    elif ch == 5:
        try:
            bug_id = int(input("ENTER THE BUG ID TO BE DELETED: "))
            delete_bug(bug_id)
        except ValueError:
            print("BUG ID SHOULD BE OF TYPE INTEGER")
    elif ch == 6:
        disp_dev_status()
    elif ch == 7:
        print("EXITING PROGRAM")
        break
    else:
        print("INVALID CHOICE...TRY AGAIN")
