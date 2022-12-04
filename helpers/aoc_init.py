import os
os.getcwd()

AOC_FIRST_DAY = 1
AOC_LAST_DAY = 25


def create_aoc_folder(day_num):
    folder_name = f'day{day_num}'
    os.makedirs(folder_name)
    print(f'Folder {folder_name} created')


def init_folders(day_num):
    """
    Create single or all aoc folders
    """
    if day_num:
        create_aoc_folder(day_num)
    else:
        for day_num in range(AOC_FIRST_DAY,AOC_LAST_DAY):
            create_aoc_folder(day_num)


def create_python_file_in_aoc_folder(filename, day_num):
    os.chdir(f'day{day_num}')
    with open(filename, 'w') as f:
        f.write(f'# Day {day_num}')
    os.chdir('..')


def init_files(day_num):
    if day_num:
        create_python_file_in_aoc_folder(f'day{day_num}a.py', day_num)
    else:
        for day_num_2 in range(AOC_FIRST_DAY,AOC_LAST_DAY):
            create_python_file_in_aoc_folder(f'day{day_num_2}a.py', day_num)

init_files(2)