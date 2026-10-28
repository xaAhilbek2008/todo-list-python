tasks = []

while True:
    print("---Menu---")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
    elif choice == 2:
        new_task = input("Enter your new task: ")
        tasks.append(new_task)
        print("Task added!")
    elif choice == 3:
        print("Bye!")
        break
    else:
        print("Invalid choice! Try again.")