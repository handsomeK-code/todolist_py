def showList (tasks) -> dict:
    #check tasks empty or not
    if not tasks:
        return print('you dont have any task right now! please make one!')
    choose_progress =input("Filter: ")
    #todo: add check
    #show not done
    if choose_progress== 1:
        print((not_done for not_done in tasks ))
    #show in-progress
    if choose_progress == 2:
        print((in_progress for in_progress in tasks))
    #show done
    if choose_progress == 3:
        print((done for done in tasks))