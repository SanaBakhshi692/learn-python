import json  
def Task_validation(id, title, done, description):
    if not isinstance(id, int) or isinstance(id, bool) or id <= 0:
        raise ValueError('invalid Id')
    if not isinstance(title, str) or title.strip() == "":
        raise ValueError("invalid title")
    if not isinstance(done, bool):
        raise ValueError("invalid status")
    if not isinstance(description, str):
        raise ValueError("invalid description")

def User_validation(id, name):
    if not isinstance(id, int) or isinstance(id, bool) or id <= 0:
        raise ValueError('invalid Id')
    if not isinstance(name, str) or name.strip() == "":
        raise ValueError("invalid name")
    
class Task:
    def __init__(self, id, title, done, description):
        Task_validation(id, title, done, description)
        self.id = id
        self.title = title
        self.done = done
        self.description = description

    def task_info(self):
        return f"task id: {self.id}, title: {self.title}, done: {self.done}"

class User:
    def __init__(self,id, name):
        User_validation(id, name)
        self.id  = id
        self.name = name
    def user_info(self):
        return f"user id: {self.id} , user name: {self.name}"

class Manager:
    def __init__(self):
        self.task_list = []

    def add_task(self,task):
        if not isinstance(task, Task):
            raise ValueError("invalid task")
        for t in self.task_list:
            if t.id == task.id:
                raise ValueError("fail to add a new task")
        self.task_list.append(task)
        return "new task added successfully!"

    def find_task(self, id):
        if not isinstance(id, int) or isinstance(id, bool) or id <= 0:
            raise ValueError("invalid id")
        for task in self.task_list:
            if task.id == id:
                return task
        raise ValueError("task not found")
            

    def change_status(self, id):
        if not isinstance(id, int) or isinstance(id, bool) or id <= 0:
            raise ValueError("invalid id")
        try:
            task = self.find_task(id)
            if task:
                task.done = not task.done
                return "task status changed successfully!"
        except ValueError:
            raise ValueError("failed to change the status")
        
    def delete_task(self,id):
        if not isinstance(id, int) or isinstance(id, bool) or id <= 0:
            raise ValueError("invalid id")
        task = self.find_task(id)
        if task:
            self.task_list.remove(task)
            return "task removed successfully!"

    def view_completed(self):
        completed = []
        for task in self.task_list:
            if task.done:
                completed.append(task)
        return completed

    def save_tasks(self):
        data = []
        for task in self.task_list:
            data.append({"id": task.id, "title": task.title, "done": task.done, "description": task.description})
        with open("task_manager.json", "w") as file:
            json.dump(data, file)

    def load_tasks(self):
        load_data = []
        try:
            with open("task_manager.json","r") as file:
                data = json.load(file)
                for d in data:
                    task = Task(d["id"], d["title"], d["done"], d["description"])
                    load_data.append(task)
                    
        except FileNotFoundError as e:
                load_data = []
                print(e)
        self.task_list = load_data
        print(self.task_list)
