from file_system import Tree_File_System

def terminal():
    curdir = Tree_File_System()
    while True:
        command = input(curdir.name+': ')
        if command == 'EXIT':
            break
        else:
            command_list = command.split()
            if command_list[0] == 'cd':
                curdir = curdir.cd(command_list[1])

            elif command_list[0] == 'mkdir':
                curdir.mkdir(command_list[1])

            elif command_list[0] == 'touch':
                curdir.touch(command_list[1])

            elif command_list[0] == 'ls':
                curdir.ls()

            else:
                print('ERROR: Command does not exist.')


terminal()