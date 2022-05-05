class Tree_File_System:
    def __init__(self):
        self.name = 'Home'
        self.directories = []
        self.childnames = []
        self.parent_directory = None

    def mkdir(self, directory):
        p = Tree_File_System()
        p.name = directory
        p.parent_directory = self
        self.directories.append(p)
        self.childnames.append(p.name)

    def touch(self, file):
        self.childnames.append(file)

    def ls(self, child=None):
        if child != None:
            for dir in self.directories:
                if dir.name == child:
                    for item in dir.childnames:
                        print(item)
                        return
            print('Directory does not exist.')
        else:
            for item in self.childnames:
                print(item)

    def cd(self, child):
        for dir in self.directories:
            if dir.name == child:
                return dir
        for string in child.split('/'):
            if string != '..':
                return False
        for x in range(len(child.split('/'))):
                self = self.parent_directory
        return self