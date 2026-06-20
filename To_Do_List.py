my_tasks=[]

def add_task(task):
    my_tasks.append(task)

def view_task():
    if not my_tasks:
        print("No tasks yet!")
        return
    for i,task in enumerate(my_tasks,1):
        print(f"{i}.{task}")

def main():
    while True:
        print("\n 1.Add Task \n 2.View Task \n 3.Quit")
        choice:int=int(input("Enter the choice (1-3):"))

        if(choice==1):
            task:str=str(input("Enter the task: "))
            add_task(task)
        
        elif(choice==2):
            view_task()

        elif(choice==3):
            print("Thank you!")
            break
        else:
            print("Invalid choice!")
            continue

if __name__=="__main__":
    main()