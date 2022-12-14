def set_type(dtype='string', val='string'):
    if dtype == 'string':
        return str(val)
    elif dtype == 'int':
        return int(val)
    elif dtype == 'float':
        return float(val)


def read_input(input_file='input', remove_newlines=True, split_on_comma=False, split_on_space=False,
               dtype='string', sublists_on_newline=False):
    with open(input_file, 'r') as f:
        file_lines = f.readlines()
    if remove_newlines:
        # remove new lines
        file_lines = [line.split('\n')[0] for line in file_lines]
    if split_on_comma:
        file_lines = [line.split(',') for line in file_lines]
    if split_on_space:
        file_lines = [line.split(' ') for line in file_lines]
    if sublists_on_newline:
        file_lines_sublists = []
        sublist = []
        for line in file_lines:
            if line != '':
                sublist.append(set_type(dtype, line))
            else:
                file_lines_sublists.append(sublist)
                sublist = []
        file_lines = file_lines_sublists
    return file_lines


def split_list(list_to_split: list, split_value: str, include_split_value: str=None):
    list_of_lists = []
    sublist = []
    for item in list_to_split:
        if item == split_value:
            if sublist:
                list_of_lists.append(sublist)
                sublist = []
        else:
            sublist.append(item)
    # Add last sublist
    if sublist:
        list_of_lists.append(sublist)
    return list_of_lists


def convert_ranges_to_sets(list_of_range_pairs):
    set_pairs = []
    for range_pair in list_of_range_pairs:
        set_pair = []
        for hyphen_range in range_pair:
            spaces_list = []
            for x in range(int(hyphen_range.split('-')[0]), int(hyphen_range.split('-')[1]) + 1):
                spaces_list.append(x)
            set_pair.append(set(spaces_list))
        set_pairs.append(set_pair)
    return set_pairs


# import requests
# url = 'https://adventofcode.com/2022/day/2/input'
# r = requests.get(url, allow_redirects=True)
# open('input2', 'wb').write(r.content)