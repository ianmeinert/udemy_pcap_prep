import string
import sys
from typing import List
import uuid


class Task:
    def __init__(self, title=None, deadline=None, id=None) -> None:
        self.UUID = id if self.is_valid_uuid(id) else str(uuid.uuid4())
        self.title = title.strip(string.whitespace)
        self.deadline = deadline.strip(string.whitespace)

    def __str__(self) -> str:
        return f"{self.UUID} | {self.title} | {self.deadline}"

    def is_valid_uuid(self, val):
        try:
            uuid.UUID(str(val), version=4)
            return True
        except ValueError:
            return False


class TodoList:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.tasks: List[Task] = []
        self.load_file(filename)

    def add_task(self, task):
        with open(self.filename, "a") as f:
            f.write(str(task) + "\n")

        self.tasks.append(task)

    def complete_task(self, task):
        with open(self.filename, "r") as f:
            lines = f.readlines()

        with open(self.filename, "w") as f:
            for line in lines:
                if line.strip("\n") != str(task):
                    f.write(line)

        self.tasks.remove(task)

    def load_file(self, filename):
        try:
            with open(filename, "r") as f:
                lines = f.readlines()

                for line in lines:
                    id, title, deadline = line.split(" | ")
                    task = Task(id=id, title=title, deadline=deadline)
                    self.tasks.append(task)
        except FileNotFoundError:
            with open(filename, "w") as file:
                pass


def display_menu():
    menu = """== TODO LIST ==
[1] show tasks
[2] add task
[3] complete task
[4] exit

Your choice: """

    while True:
        selection = input(menu)

        if selection.isalpha() or int(selection) < 1 or int(selection) > 4:
            continue
        else:
            return int(selection)


def add_task(todolist: TodoList):
    print("[ADD TASK]")

    title = input("What is the task? ")
    deadline = input("What is the deadline? ")
    task_test = Task(title=title, deadline=deadline)
    todolist.add_task(task_test)

    print()


def show_tasks(todolist: TodoList):
    print("[YOUR TASKS]")

    if not todolist.tasks:
        print("Empty list\n")
        return

    for task in todolist.tasks:
        print(task)

    print()


def complete_task(todolist: TodoList):
    print("[COMPLETE TASK]\n")
    show_tasks(todolist)

    if not todolist.tasks:
        print("No tasks to complete\n")
        return

    while True:
        id_to_delete = input("Enter id to complete: ")

        try:
            uuid.UUID(str(id_to_delete), version=4)
        except ValueError:
            print("Invalid ID.\n")
            continue
        else:
            for task in todolist.tasks:
                if task.UUID == id_to_delete:
                    todolist.complete_task(task)
                    print()
                    return


def run_program():
    todolist = TodoList("todo.txt")

    while True:
        selection = display_menu()
        print()

        match selection:
            case 1:
                show_tasks(todolist)
            case 2:
                add_task(todolist)
            case 3:
                complete_task(todolist)
            case 4:
                sys.exit()


run_program()
