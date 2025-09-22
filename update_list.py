def updateList (tasks:dict) -> dict:
    if not tasks:
        return print("you have no task right now. Please create one!")
    print((task['description'] for task in tasks))
    task_name = input('input the task you want to update')
    #todo: check function
    progress_type = input('status: ')
    #change to todo
    if progress_type == 0:
        tasks[task_name]['status'] = 'todo'
        return tasks
    #change to in-progress
    elif progress_type == 1:
        tasks[task_name]['status'] = 'in-progress'
        return tasks
    #change to done
    elif progress_type == 2:
        tasks[task_name]['status'] = 'done'
        return tasks