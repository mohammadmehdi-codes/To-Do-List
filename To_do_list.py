import json
tasks = []

def add_task():
    task_name = input("Enter your Task: ")
    task = {
        "name" : task_name,
        "completed" : False
    }
    if not task_name.strip():
        print("Task cannot be empty")
    else:
        tasks.append(task)
        print("Task added successfully")
        save_file()

def view_task():
    if len(tasks) == 0:
        print("No task found")
    else:
        for x, task in enumerate(tasks, start=1):
            if task["completed"]:
                print(x, task["name"],"✅")
            else:
                print(x, task["name"],"❌")
            
def delete_task():
    print("Total tasks are given")
    for x, task in enumerate(tasks, start=1):
        print(x, task["name"])
    try:        
        erase = int(input("Please enter task no. for deletion"))
    except ValueError:
        print("invalid keyword")
        return
    if erase <= len(tasks) and erase >= 1:    
        del tasks[erase - 1]
        save_file()
        print("Task deleted successfully.\nRemaining tasks are follows:")
        for x, task in enumerate(tasks, start=1):
            print(x, task["name"])    
    else:
        print("invalid keyword")

def mark_as_complete():
        if not tasks:
            print("no task found")
        else:
            for x, task in enumerate(tasks, start=1):
                if task["completed"]:
                    print(x, task["name"],"✅")
                else:
                    print(x, task["name"],"❌")
            try:        
                task_complete = int(input("Please enter task no for task completion: "))
            except ValueError:
                print("invalid keyword")
                return    
            if task_complete >=1 and task_complete <= len(tasks):
                tasks[task_complete-1]["completed"] = True
                print("Task mark completed successfully")
                save_file()
            else:
                print("invalid input")

def save_file():
    with open("To_do_list.txt", "w") as f:
        json.dump(tasks,f)
                
def load_file():
    global tasks
    try:
        with open("To_do_list.txt", "r") as f:
            tasks = json.load(f)            
    except FileNotFoundError:
          print("no task available")   
    
load_file()
while True:
    print("-----TO DO LIST------")
    print("1. Add task")
    print("2. View task")
    print("3. Delete task")
    print("4. Mark task as complete")
    print("5. Exit")

    try:
        choice = int(input("Select given option: "))
    except ValueError:
        print("Invalid keyword")
        continue
    if choice == 1:
        add_task()

    elif choice == 2:
        view_task()

    elif choice == 3:
        delete_task()

    elif choice == 4:
        mark_as_complete()    

    elif choice == 5:
        print("Good bye")
        break        
    else:
        print("invalid selection, please try again")