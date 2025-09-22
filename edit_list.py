def editList () -> list:
    if not tasks:
        return print("you have no todo task right now! Please add a new list")
    print((task['description'] for task in tasks ))
    task_to_edit = input("please the fullname of the task you want to edit")
    #add checks to prevent wrong input 
    what_to_edit = input("what do you want to edit")
    