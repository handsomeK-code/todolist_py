def addList () -> dict:
    new_task = dict()
    description = input('Name of the task: ')
    if tasks:
        new_task['id'] = len(tasks)
    else:
        new_task['id'] = 1