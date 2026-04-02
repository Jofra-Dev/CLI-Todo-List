import os
import json

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def showTasks():
    tasks = load_tasks()
    clearTerminal()
    
    if not tasks:
        print("No tasks found.")
    else:
        print("--- CURRENT TASKS ---")
        for t in tasks:
            status = "[✔]" if t["checked"] else "[ ]"
            print(f"{t['id']}: {status} {t['task']}")
    
    input("\nPress Enter to continue...")
    clearTerminal()

def reindex_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        task["id"] = index
    return tasks

def editTasks():
    tasks = load_tasks()
    
    clearTerminal()
    print("1) Add task\n2) Mark as done\n3) Delete task\n4) Back")
    option = input("\nChoose: ")

    match option:
        case "1":
            clearTerminal()
            desc = input("New task: ")
            
            tasks.append({"id": 0, "task": desc, "checked": False})
            tasks = reindex_tasks(tasks) 
            clearTerminal()

        case "2":
            clearTerminal()
            for t in tasks:
                status = "[✔]" if t["checked"] else "[ ]"
                print(f"{t['id']}: {status} {t['task']}")
            print("------------------------------------")
            
            try:
                task_id = int(input("ID to mark as done: "))
                found = False
                for t in tasks:
                    if t["id"] == task_id:
                        t["checked"] = True
                        found = True
                if not found:
                    print("ID not found.")
            except ValueError:
                print("Invalid input! Please enter a numeric ID.")
            
        case "3":
            clearTerminal()
            for t in tasks:
                status = "[✔]" if t["checked"] else "[ ]"
                print(f"{t['id']}: {status} {t['task']}")
            print("------------------------------------")
            
            try:
                task_id = int(input("ID to delete: "))
                
                new_tasks = [t for t in tasks if t["id"] != task_id]
                
                if len(new_tasks) < len(tasks): 
                    tasks = reindex_tasks(new_tasks) 
                else:
                    print("ID not found.")
            except ValueError:
                print("Invalid input! Please enter a numeric ID.")

        case "4":
            clearTerminal()
            return
            
        case _:
            clearTerminal()
            print("Invalid Option")
            return

    save_tasks(tasks)
    print("Action completed and IDs updated!")
    input("Press Enter to continue...")
    clearTerminal()