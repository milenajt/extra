import os
import time


def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper


class CommandPrompt:
    def __init__(self):
        self.current_dir = os.getcwd()

    @execution_time_decorator
    def show_current_dir(self):
        return self.current_dir

    @execution_time_decorator
    def list_files(self):
        entries = os.listdir(self.current_dir)
        return entries

    @execution_time_decorator
    def change_directory(self, new_directory):
        try:
            if new_directory == '...':
                os.chdir(os.path.abspath(
                    os.path.join(self.current_dir, os.pardir)))
                self.current_dir = os.getcwd()
            else:
                os.chdir(new_directory)
                self.current_dir = os.getcwd()
        except FileNotFoundError:
            raise Exception('Directory not found!')
        except TypeError:
            raise Exception('Invalid directory argument!')

    @execution_time_decorator
    def create_folder(self, folder):
        os.mkdir(os.path.join(self.current_dir, folder))

    @execution_time_decorator
    def delete_folder(self, folder):
        try:
            os.rmdir(os.path.join(self.current_dir, folder))
        except NotADirectoryError:
            print("Please enter the name of directory of use command delete <filename> for a file")

    @execution_time_decorator
    def rename_file(self, source, destination):
        os.rename(os.path.join(self.current_dir, source),
                  os.path.join(self.current_dir, destination))

    @execution_time_decorator
    def read_file(self, filename):
        file = os.path.join(self.current_dir, filename)
        if os.path.isfile(file):
            with open(file, 'r', encoding='utf-8') as file:
                return file.read()
        else:
            print("It's not a file")

    @execution_time_decorator
    def create_file(self, filename):
        try:
            with open(os.path.join(self.current_dir, filename), 'x', encoding='utf-8') as file:
                return file.write(input('Enter data:'))
        except FileExistsError:
            print('This file already exists')
    
    @execution_time_decorator
    def delete_file(self, filename):
        try:
            os.remove(os.path.join(self.current_dir, filename))
        except FileNotFoundError:
            print('This file not found')


cmd = CommandPrompt()
start = time.time()
commands = ['cd', 'dir', 'exit', 'mkdir', 'rmdir', 'delete', 'rename', 'read', 'create']
while True:
    request = input(cmd.current_dir + '>').split()
    if len(request) == 1:
        if request[0] == 'cd':
            print(cmd.show_current_dir())
        elif request[0] == 'dir':
            print(cmd.list_files())
        elif request[0] == 'exit':
            print('Exiting command prompt. Goodbye!')
            end = time.time()
            print(f'Execution time of run: {end - start} seconds')
            break
    elif len(request) > 1:
        if request[0] == 'cd':
            cmd.change_directory(request[1])
        elif request[0] == 'mkdir':
            cmd.create_folder(request[1])
        elif request[0] == 'rmdir':
            cmd.delete_folder(request[1])
        elif request[0] == 'delete':
            cmd.delete_file(request[1])
        elif request[0] == 'rename':
            cmd.rename_file(request[1], request[2])
        elif request[0] == 'read':
            print(cmd.read_file(request[1]))
        elif request[0] == 'create':
            cmd.create_file(request[1])
    elif request[0] not in commands:
        continue
