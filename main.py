ALL_TASKS = []

def add_task():
    task = input("Enter the Task: ")
    priority = input("Enter the priority (low/medium/high): ").lower()
    ALL_TASKS.append(f"Task : {task} | Priority : {priority} | Completed: False")
    print("Task Added Successfully!")

def view_task():
    print(" To-Do List: ")
    for x, task in enumerate(ALL_TASKS, start=1):
        task_info = task.split("|")
        completion_status = task_info[-1].strip()
        emoji = "✅" if completion_status == "Completed: True" else "🟡"
        print(f"{x} . {emoji} {task}")

def mark_comp():
    view_task()
    task_ind = int(input("Enter the task number to mark it as complete: ")) - 1
    if 0 <= task_ind < len(ALL_TASKS):
        task_info = ALL_TASKS[task_ind].split("|")
        task_info[-1] = " Completed: True"
        ALL_TASKS[task_ind] = " |".join(task_info)
        print("Task marked as completed! ✅")
    else:
        print("Invalid task number. ❌ ")

def main():
    while True:
        print("\n Menu: ")
        print("1. Add Task")
        print("2. View Task/Tasks")
        print("3. Mark Task as complete")
        print("4. Quit! ")
        choice = input("Select an option (1/2/3/4): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            mark_comp()
        elif choice == "4":
            print("Ok Goodbye!")
            break
        else:
            print("Invalid Input. Please try again!")

if __name__ == "__main__":
    print("Welcome to the To-Do List APP! ")
    main()
