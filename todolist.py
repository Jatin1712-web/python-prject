Add_task = []
Completed_task = []

def show_task():
    if not Add_task:
        print("No Task Available.")
    else:
        print("Pending Tasks:")
        for task in Add_task:
            print(f"- {task}")
    
    if not Completed_task:
        print("No Completed Tasks.")
    else:
        print("Completed Tasks:")
        for task in Completed_task:
            print(f"- {task}")

while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Show Task")
    print("4. Delete Task")
    print("5. Add Completed Task")
    print("6. Remaining Task")
    print("7. Exit")
    
    try:
        choice = int(input("Enter The Choice No.: "))
    except ValueError:
        print("Invalid input, please enter a number between 1 and 7.")
        continue  
    
    if choice == 1: 
        try:
            task_count = int(input("How many tasks would you like to add? "))
            for _ in range(task_count):
                task = input("Enter task: ")
                Add_task.append(task)
                print("Task Added")
        except ValueError:
            print("Please enter a valid number for task count.")
    
    elif choice == 2:  
        show_task()
        update_to_task = input("Enter the task you want to change: ")
        
        if update_to_task in Add_task:
            print("A. Rename Task")
            print("B. Replace Task")
            select = input("Enter A or B: ").upper()
            
            if select == "A":
                new_name = input("Enter the new name for the task: ")
                index = Add_task.index(update_to_task)
                Add_task[index] = new_name
                print("Renamed Successful")
            
            elif select == "B":
                replacement = input("Enter the new task details: ")
                index = Add_task.index(update_to_task)
                Add_task[index] = replacement
                print("Task replaced.")
            
            else:
                print("Invalid option, please select A or B.")
        else:
            print("Task not found.")
    
    elif choice == 3:  
        show_task()
    
    elif choice == 4: 
        task_to_delete = input("Enter the task you want to delete: ")
        
        if task_to_delete in Add_task:
            Add_task.remove(task_to_delete)
            print("Task deleted.")
        else:
            print("Task not found.")
    
    elif choice == 5:  
        show_task()
        completed_task = input("Enter the task you have completed: ")
        
        if completed_task in Add_task:
            Add_task.remove(completed_task)
            Completed_task.append(completed_task)
            print("completed task added.")
        else:
            print("Task not found.")
    
    elif choice == 6:  
        print(f"Remaining tasks: {len(Add_task)}")
    
    elif choice == 7:  
        print("Exiting To-Do List.")
        break  
    
    else:
        print("Invalid choice, please select a number between 1 and 7.")
        break
