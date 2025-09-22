def showList (tasks) -> dict:
    #check tasks empty or not
    if not tasks:
        return print('you dont have any task right now! please make one!')
    choose_progress =input("Filter: ")
    #todo: add check
    if choose_progress== 1:
        