import datetime
import calendar
import os

class Task:
    def __init__(self, title, description, due_date, recurring=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.recurring = recurring

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nRecurring: {self.recurring}\n"

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' removed successfully.")
                return
        print(f"Task '{title}' not found.")

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task.title}|{task.description}|{task.due_date}|{task.recurring}\n")

    def load_tasks(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    data = line.strip().split('|')
                    title, description, due_date, recurring = data
                    due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
                    recurring = True if recurring == "True" else False
                    self.tasks.append(Task(title, description, due_date, recurring))
            print("Tasks loaded successfully.")
        else:
            print("No saved tasks found.")

def main():
    scheduler = TaskScheduler()

   
    scheduler.load_tasks("tasks.txt")

    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Save Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            recurring = input("Is task recurring? (True/False): ").capitalize()
            task = Task(title, description, due_date, recurring)
            scheduler.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            print("\nList of Tasks:")
            scheduler.list_tasks()
        elif choice == "3":
            title = input("Enter task title to remove: ")
            scheduler.remove_task(title)
        elif choice == "4":
            scheduler.save_tasks("tasks.txt")
            print("Tasks saved successfully.")
        elif choice == "5":
            print("Exiting Task Scheduler.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
