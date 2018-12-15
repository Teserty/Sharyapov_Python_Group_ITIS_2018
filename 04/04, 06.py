import os, shutil,re
def valid_cd(linux_cd):
    def accept_argument(command):
        if len(command)==2:
            linux_cd(command[1])
    return accept_argument
def valid_append(append):
    def accept_argument(command):
        if len(command) == 2:
            append(command[1])
    return accept_argument
@valid_cd
def cd(path):
    os.chdir(path)
@valid_append
def append(path):
    with open(path, 'a') as file:
        file.write(input('Введите строку: '))
def remove(pattern):
    files = os.listdir()
    a = list()
    for file in files:
        if pattern in file:
            a.append(file)
    if len(a):
        print("Founded {0} files, with name {1}".format(len(a), a))
        if input("You want to delete it? Y/N") == "Y":
            for file in a:
                os.remove(file)
if __name__ == '__main__':
    while True:
        command = input("\n" + os.path.abspath(os.curdir) + "$ ").split(' ')
        if command[0] == 'cd':
            cd(command)
        elif command[0] == 'append':
            append(command)
        elif command[0] == 'rm':
            remove(command[1])
        elif command[0] == 'exit':
            break
        else:
            print("cd/append/rm/exit")