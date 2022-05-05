import main 
import file_system

# Tests that 'mkdir' input with no specified directory will return 'Need directory name.'
# Tests that 'EXIT' terminates the program (as do all the other tests)
def test_directory_name():
    inputs = ['mkdir', 'EXIT']
    output = []
 
    def mock_input(s):
        output.append(s)
        return inputs.pop(0)
    main.input = mock_input
    main.print = lambda s : output.append(s)
  
    main.terminal()
    assert output == [
       'Home: ', 
       'Need directory name.',
       'Home: '
    ]

# Tests that 'touch' input with no specified file name will return 'Need file name.'
def test_file_name():
    inputs = ['touch', 'EXIT']
    output = []
 
    def mock_input(s):
        output.append(s)
        return inputs.pop(0)
    main.input = mock_input
    main.print = lambda s : output.append(s)
  
    main.terminal()
    assert output == [
       'Home: ', 
       'Need file name.',
       'Home: '
    ]

# Tests that 'Not valid command.' is returned when anything that's not cd, ls, mkdir, or touch is inputted
def test_invalid_input():
    inputs = ['patrick', 'EXIT']
    output = []
 
    def mock_input(s):
        output.append(s)
        return inputs.pop(0)
    main.input = mock_input
    main.print = lambda s : output.append(s)
  
    main.terminal()
    assert output == [
       'Home: ', 
       'Not valid command.',
       'Home: '
    ]

# Tests that the mkdir command does indeed create a new directory by showing it using the ls command
# Tests the ls command
# Tests that cd will change the directory to the specified one (since it has been made already)
# Tests that mkdir can make another directory within a created directory
# Tests that cd followed by '..' will go back to the previous directory
# Tests that cd command by itself will change the current directory to Home
# Tests that ls command followed by child directory will show the sub-directories of that one
def test_new_directories():
    inputs = ['mkdir new1', 'ls', 'cd new1', 'mkdir new2', 'cd new2', 'cd ..', 'cd', 'ls new1',  'EXIT']
    output = []
 
    def mock_input(s):
        output.append(s)
        return inputs.pop(0)
    main.input = mock_input
    main.print = lambda s : output.append(s)
    file_system.print = lambda s : output.append(s)
    
    main.terminal()
    print(output)
    assert output == [
       'Home: ', 
       'Home: ',
       'new1',
       'Home: ',
       'new1: ',
       'new1: ',
       'new2: ',
       'new1: ',
       'Home: ',
       'new2',
       'Home: '
    ]


# Tests that ls followed by a directory that does not exist will return 'Directory does not exist.'
def test_fake_directory():
    inputs = ['ls new3', 'EXIT']
    output = []
 
    def mock_input(s):
        output.append(s)
        return inputs.pop(0)
    main.input = mock_input
    main.print = lambda s : output.append(s)
    file_system.print = lambda s : output.append(s)
  
    main.terminal()
    assert output == [
       'Home: ', 
       'Directory does not exist.',
       'Home: ' 
    ]

# Tests that any command (in this case mkdir) followed by two separate words/strings will return 'Not valid command.'
def test_three_words():
    inputs = ['mkdir another one', 'EXIT']
    output = []
 
    def mock_input(s):
        output.append(s)
        return inputs.pop(0)
    main.input = mock_input
    main.print = lambda s : output.append(s)
  
    main.terminal()
    assert output == [
       'Home: ', 
       'Not valid command.',
       'Home: ' 
    ]

# Tests that touch creates a file, and shows it with ls
# Tests that trying to navigate to a file will return 'Directory does not exist.'
def test_file_directory():
    inputs = ['touch firstfile.txt', 'ls', 'cd firstfile', 'EXIT']
    output = []
 
    def mock_input(s):
        output.append(s)
        return inputs.pop(0)
    main.input = mock_input
    main.print = lambda s : output.append(s)
    file_system.print = lambda s : output.append(s)
  
    main.terminal()
    print(output)
    assert output == [
       'Home: ', 
       'Home: ',
       'firstfile.txt',
       'Home: ',
       'Directory does not exist.',
       'Home: ' 
    ]


test_directory_name()
test_file_name()
test_invalid_input()
test_new_directories()
test_fake_directory()
test_three_words()
test_file_directory()
