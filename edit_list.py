def editTask (tasks:list) -> list:
    if not tasks:
        return print("you have no todo task right now! Please add a new list")
    print((task['description'] for task in tasks ))
    task_to_edit = input("please the fullname of the task you want to edit")
    #add checks to prevent wrong input 
    prop_to_edit = input("what do you want to edit")
    #change task name
    if prop_to_edit == 0:
        name = input('Please input the new task name you want to change to: ')
        tasks[task_to_edit]['description'] = name
        tasks[name] = tasks.pop(task_to_edit)
        return tasks
    elif