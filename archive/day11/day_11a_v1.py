"""
Advent of Code 2022
Day 11

"""
from helpers.io import read_input, split_list
import numpy as np
import copy


class Monkey:
    def __init__(self, monkey_num):
        self.monkey_num = monkey_num


def get_int(char):
    return int(char)


def get_operation(op_op2, op_num2, itself):
    if op_op2 == '*':
        if itself:
            operation2 = lambda old: old * old
        else:
            operation2 = lambda old: old * op_num2
    elif op_op2 == '+':
        if itself:
            operation2 = lambda old: old + old
        else:
            operation2 = lambda old: old + op_num2
    elif op_op2 == '-':
        if itself:
            operation2 = lambda old: old - old
        else:
            operation2 = lambda old: old - op_num2
    else:
        print('UNKNOWN op_op')
        operation2 = lambda x: x
    return operation2


def get_test(test_num3):
    test3 = lambda x: x % test_num3 == 0
    return test3


def get_throw_to(test_num2, true_test_monkey2, false_test_monkey2):
    test2 = lambda x: true_test_monkey2 if x % test_num2 == 0 else false_test_monkey2
    return test2


def read_monkeys(file_lines):
    read_debug = False
    monkeys = {}
    line_num = 0
    test_op = ""
    start_items = []
    operation = lambda x: x
    for file_line in file_lines:
        line_num += 1
        if read_debug:
            print(f'reading line {line_num}: ', end="")
        if file_line[0:6] == 'Monkey':
            monkey_num = int(file_line.split()[1].split(':')[0])
            if read_debug:
                print(f'Monkey num: {monkey_num}')
        elif file_line[0:7] == '  Start':
            start_items = [int(item) for item in file_line.split(':')[1].strip().split(',')]
            if read_debug:
                print(f'start_items: {start_items}')
        elif file_line[0:11] == '  Operation':
            op_complete = file_line.split(':')[1].strip()
            op = op_complete.split('=')[1].strip()
            op_op = op.split()[1]
            op_operand = op.split(op_op)[1].strip()
            if op_operand == 'old':
                op_num = get_int(monkey_num)
                itself = True
            else:
                op_num = get_int(op_operand)
                itself = False
            operation = get_operation(op_op, op_num, itself)
            if read_debug:
                print(f'Operation: {op_op} {op_num}')
        elif file_line[0:6] == '  Test':
            test_complete = file_line.split(':')[1].strip()
            test_op = test_complete.split('by')[0].strip()
            test_num = int(test_complete.split('by')[1])
            if read_debug:
                print(f'Test: {test_op} {test_num}')
        elif file_line[0:11] == '    If true':
            true_test_complete = file_line.split(':')[1]
            true_test_monkey = int(true_test_complete.split('to monkey')[1])
            if read_debug:
                print(f'true test: {true_test_monkey}')
        elif file_line[0:12] == '    If false':
            true_test_complete = file_line.split(':')[1].split('\n')[0]
            false_test_monkey = int(true_test_complete.split('to monkey')[1])
            if read_debug:
                print(f'false test: {false_test_monkey}')
            if test_op == 'divisible':
                test_op = get_test(test_num)
                throw_to = get_throw_to(test_num, true_test_monkey, false_test_monkey)
        elif file_line == '':
            monkeys[monkey_num] = {'start_items': start_items,
                                   'op': operation,
                                   'test': test_op,
                                   'throw_to': throw_to,
                                   'inspected': 0}
            if read_debug:
                print(f'monkey {monkey_num} read')
                print()
    return monkeys


test = False
# test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)
monkeys = read_monkeys(file_lines)

calc_debug = True
for mround in range(20):
    for mnum, monkey in monkeys.items():
        items_to_remove = []
        for item in monkey['start_items']:
            wlevel = monkey['op'](item)
            wlevel_bored = int(np.floor(wlevel / 3))
            new_monkey = monkey['throw_to'](wlevel_bored)
            items_to_remove.append(item)
            monkey['inspected'] += 1
            monkeys[new_monkey]['start_items'].append(wlevel_bored)
            if calc_debug:
                print(f"Round {mround+1} Monkey {mnum}: item={item}, wlevel={wlevel}, wlevel_bored={wlevel_bored},"
                      f"test={monkey['test'](wlevel_bored)}, "
                      f"throw to={new_monkey},"
                      f"new monkey start items after={monkeys[new_monkey]['start_items']},"
                      f"inspected={monkey['inspected']}")

                # print(f"Monkey {mnum}:")
                # print(f"  Monkey inspects an item with worry level of {item}.")
                # print(f"    Worry level to {wlevel}")
                # print(f"    worry level bored : {wlevel_bored}")
                # print(f"    Divisible ? {monkey['test'](wlevel_bored)}")
                # print(f"    Throw to {new_monkey}")
        for item in items_to_remove:
            monkey['start_items'].remove(item)
        print(f"           start_items_after={monkey['start_items']}")
    for mnum, monkey in monkeys.items():
        print(f"Monkey {mnum}, items: {monkey['start_items']}")

for mnum, monkey in monkeys.items():
    print(f"Monkey {mnum}, inspected: {monkey['inspected']}")

inspected_items = [monkey['inspected'] for monkey in monkeys.values()]
inspected_items.sort(reverse=True)
product = 1
for item in inspected_items[:2]:
    product *= item
print(f"Level of Monkey business: {product}")

print('finished')
