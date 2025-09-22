from datetime import datetime

def addList (tasks:dict) -> dict:
    new_task = dict()
    description = input('Name of the task: ')
    #setid
    #todo check existance of tasks
    if tasks:
        new_task['id'] = len(tasks)
    else:
        new_task['id'] = 1
    #description
    new_task['description'] = description
    #status
    new_task['status'] = 'todo'
    #createdtime
    new_task['createdAt'] = datetime.now().strftime("%Y-%m-%d %H:%M%S")
    #updatedtime
    new_task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M%S")
    tasks[new_task['description']] = new_task
    return tasks