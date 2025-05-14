# Interact with the operating system, allowing the script to check file existence.
import os

#Show task function 
def showtasks(tasks):
    if not tasks:
        print("No tasks found")
    else:
        for i, task in enumerate(tasks,1): # enumerate used to iterate over a sequence 
            print(f"{i}. {task}") # f-string making it easier to include variables and expressions within the string itself


#Add task
def addtask(tasks,newtask):
    tasks.append(newtask) # append method is used to add a single element to the end of a list.
    print("Task added successfuly")


#Update task
def updated(tasks,index,update):
    if 1 <= index <= len(tasks):
        tasks[index-1] = update
        print("Task updated")
    else:
        print("invalid index")



#Delete task
def delete(tasks,index):
    if 1 <= index <= len(tasks):
        delete = tasks.pop(index-1) # pop method is used to remove an element
        print(f"Task '{delete}' deleted")
    else:
        print("invalid index")




#Saving file
def save(file_path,tasks):
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")



#Read file
def load_task_from_file(file_path):
    task = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            task = file.read().splitlines()
    return task




#Function calling
def main():
    file_path = "todolist.txt"
    tasks = load_task_from_file(file_path)

    #Loop until number 5 or saved
    while True:

        print("...TODO...")
        print("1.Show tasks")
        print("2.Add tasks")
        print("3.Update tasks")
        print("4.Delete tasks")
        print("5.Save & Exit")

        #Conditions 
        choise = input("What do you want to do 1-5 ? ")
        if choise == "1":
            showtasks(tasks)
        elif choise == "2":
            newtask = input("Enter the task")
            addtask(tasks,newtask) 
        elif choise == "3":
            index = int(input("Enter the task u update"))
            update = input("Enter the update task")
            updated(tasks,index,update)
        elif choise ==  "4":
            index = int(input("Enter the task u delete"))
            delete(tasks,index)
        elif choise == "5":
            save(file_path,tasks)
            print("Tasks saved")

            break

        else:
            print("Invalid choise")



#This allow to import functions and classes from the script without executing the main program logic.
if __name__ == "__main__": 
    main()