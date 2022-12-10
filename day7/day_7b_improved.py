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
        self.path = []

    def __repr__(self):
        return(f"Directory {self.name}, size: {self.size}")


class Dirtree:
    def __init__(self, root_node: Dir):
        self.root_node = root_node


def get_node(root_node: Dir, node_name: str):
    node_found = False
    if root_node.name == node_name:
        dir_found = True
    else:
        for child in root_dir.children:
            if node_name_exists(child, dir_name):
                dir_found = True
    return dir_found


def changedir(newdir_name):
    if node_name_ex:
        if directory.name == newdir_name:
            return directory
    return Dir(newdir_name)


def add_size(directory, size):
    directory.size += size
    if directory.parent:
        add_size(directory.parent[0], size)


dirs = []


def input_parser(lines):
    dir_name = '/'
    rootdir = Dir(dir_name)
    curdir = rootdir
    for idx, line in enumerate(lines):
        if 'cd' in line and len(line.split('cd ')) > 1:
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
        print(dir.name)
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
dir_tree = Dirtree(root_dir)
total_size = root_dir.size
remaining = 70000000 - total_size
to_clear = 30000000 - remaining
sizes_list = sizes_to_list(root_dir, to_clear)
print(min(sizes_list))
