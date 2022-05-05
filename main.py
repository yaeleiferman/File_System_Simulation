from file_system import Tree_File_System


def terminal():
    curdir = Tree_File_System()
    while True: 
        command = input(curdir.name+': ')
        
        if command == 'EXIT':
            return False
        
        command_list = command.split()
            
        if len(command_list) == 0:
            curdir

        elif len(command_list) == 1:
            if command_list[0] == 'ls':
                curdir.ls()
            elif command_list[0] == 'cd':
                while curdir.name != 'Home':
                    curdir = curdir.cd('..')
            elif command_list[0] == 'mkdir':
                print('Need directory name.')
            elif command_list[0] == 'touch':
                print('Need file name.')
            else:
                print('Not valid command.')

        elif len(command_list) == 2:  
            if command_list[0] == 'ls':
                curdir.ls(command_list[1])
            elif command_list[0] == 'cd':
                if curdir.cd(command_list[1]) == False:
                    print('Directory does not exist.')
                else:
                    curdir = curdir.cd(command_list[1]) 
            elif command_list[0] == 'mkdir':
                curdir.mkdir(command_list[1])

            elif command_list[0] == 'touch':
                curdir.touch(command_list[1])
            else:
                print('Not valid command.')

        else:
            print('Not valid command.')

#If running test comment out below
# terminal()