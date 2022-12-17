"""
Advent of Code 2022
Day 7

"""
from helpers.io import read_input, split_list


class Dir:
    def __init__(self, name):
        self.children = []
        self.parent = []
        self.name = name
        self.size = 0

def changedir(newdir_name):
    found = False
    for dir in dirs:
        if dir.name == newdir_name:
            found = True
            return dir
    return Dir(newdir_name)


def add_size(dir, size):
    dir.size += size
    if dir.parent != []:
        add_size(dir.parent[0], size)

dirs = []
dir_name = '/'

def input_parser(lines):
    dir_name = '/'
    rootdir = Dir(dir_name)
    curdir = rootdir
    for idx, line in enumerate(lines):
        if 'cd' in line and len(line.split('cd ')) > 1:
            # if idx == 310:
            #     print(' wacht')
            # print(idx, line)
            dir_name = line.split('cd ')[1]
            if dir_name == '..':
                if curdir.name != '/':
                    newdir = curdir.parent[0]
            else:
                if dir_name != '/':
                    newdir = changedir(dir_name)
                    curdir.children.append(newdir)
                    if newdir.name != '/':
                        newdir.parent.append(curdir)
                else:
                    newdir = curdir
        elif line.split(' ')[0].isnumeric():
            size = int(line.split(' ')[0])
            add_size(curdir, size)
        curdir = newdir
    return rootdir


def sizes_at_most(dir, atmost):
    if dir.size <= atmost:
        dirsize = dir.size
    else:
        dirsize = 0
    for child in dir.children:
        dirsize = dirsize + sizes_at_most(child, atmost)
    return dirsize


def sizes_to_list(dir, to_clear):
    if dir.size < to_clear:
        sizes = []
    else:
        sizes = [dir.size]
    for child in dir.children:
        sizes.extend(sizes_to_list(child, to_clear))
    return sizes


test = False
# test = True
input_file = 'input' if not test else 'input_test3'
file_lines = read_input(input_file)
root_dir = input_parser(file_lines)
print(sizes_at_most(root_dir, 100000))


