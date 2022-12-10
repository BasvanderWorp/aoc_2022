import os
os.getcwd()

AOC_ROOT_DIR = r"/Users/basvanderworp/PycharmProjects/aoc_2022"
AOC_FIRST_DAY = 1
AOC_LAST_DAY = 25


def create_aoc_folder(day_num):
    folder_name = os.path.join(AOC_ROOT_DIR, f'day{day_num:02d}')
    try:
        os.makedirs(folder_name)
        print(f'Folder {folder_name} created')
    except FileExistsError as Err:
        print(f'Folder {folder_name} exists, skipped')


def init_folders(start_day_num: int = AOC_FIRST_DAY, last_day_num: int = AOC_LAST_DAY):
    """
    Create single or all aoc folders
    """
    for day_num in range(start_day_num, last_day_num+1):
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


init_folders(11, 13)
# init_files(2)