def addList () -> dict:
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