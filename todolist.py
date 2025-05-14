def fun():
    tasks=[]
    while True:
        print("\n1. Add task\n2. View tasks\n3. Remove task\n4. Exit")
        choice=input("Enter choice : ")
        if choice=='1':
            task=input("Enter task: ")
            tasks.append(task)
            print("task added")
        elif choice=='2':
            for i,task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '3':
            num=int(input("Enter task number to remove: "))-1
            if 0<=num<len(tasks):
                tasks.pop(num)
                print("Task removed")
            else:
                print("invalid")
        elif choice=='4':
            print("thankss ")
            break
        else:
            print("invalid")
if __name__ == "__main__":
    fun()