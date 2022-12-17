"""
Advent of Code 2022
Day 11

"""
from helpers.io import read_input, split_list
import numpy as np
import copy
import os
import time


class MonkeyBunch:
    def __init__(self):
        self.monkeys = {}

    def __repr__(self):
        return f"{self.monkeys}"

    def add_monkey(self, monkey_num, starting_items, wl_op, wl_op_txt, test_op, test_op_txt, divider, throw_to_false,
                   throw_to_true, throw_to):
        new_monkey = Monkey(monkey_num, starting_items, wl_op, wl_op_txt, divider, test_op, test_op_txt, throw_to_false,
                            throw_to_true, throw_to, self)
        self.monkeys[monkey_num] = new_monkey

    def get_monkey_business(self):
        inspected_items = [monkey.inspected for monkey in self.monkeys.values()]
        inspected_items.sort(reverse=True)
        monkey_business = 1
        for item in inspected_items[:2]:
            monkey_business *= item
        return monkey_business


class Monkey:
    def __init__(self, monkey_num, starting_items, wl_op, wl_op_txt, divider, test_op, test_op_txt, throw_to_false,
                 throw_to_true, throw_to_op, monkey_bunch):
        self.monkey_num = monkey_num
        self.starting_items = starting_items
        self.wl_op = wl_op
        self.wl_op_txt = wl_op_txt
        self.test_op = test_op
        self.divider = divider
        self.test_op_txt = test_op_txt
        self.last_test_result = None
        self.throw_to_false = throw_to_false
        self.throw_to_true = throw_to_true
        self.throw_to_op = throw_to_op
        self.inspected = 0
        self.bunch = monkey_bunch

    def __repr__(self):
        return f"Monkey {self.monkey_num}: items={len(self.starting_items)}, wl_op={self.wl_op_txt}, " \
               f"test_op={self.test_op_txt}, throw_to_false={self.throw_to_false}, throw_to_true={self.throw_to_true}," \
               f"inspected={self.inspected}"
        # return f"Monkey {self.monkey_num}: items={len(self.starting_items)}, inspected={self.inspected}"

    def inspect_items(self):
        items_to_remove  = []
        for idx, item in enumerate(self.starting_items):
            self.inspect_item(idx)
            items_to_remove.append(item)
        for item in items_to_remove:
            self.starting_items.remove(item)

    def inspect_item(self, idx):
        item = self.starting_items[idx]
        wlevel = self.wl_op(item)
        test_result = self.test_op(wlevel)
        throw_to_monkey = self.throw_to_op(wlevel)
        if test_result:
            # wlevel = self.wl_op(item) // self.divider
            # dummy = self.wl_op(item) / self.divider
            dummy2 = self.divider
            dummy3 = 0
        if self.last_test_result is None or self.last_test_result == test_result:
            self.last_test_result = test_result
        # else:
        #     print(f"Monkey {self.monkey_num}, item:{item}: different test result")
        self.bunch.monkeys[throw_to_monkey].starting_items.append(wlevel)
        self.inspected += 1


def get_int(char):
    return int(char)


def get_operation(op_op2, op_num2, itself):
    if op_op2 == '*':
        if itself:
            operation2 = lambda old: old * old
        else:
            operation2 = lambda old: old + op_num2
    elif op_op2 == '+':
        if itself:
            operation2 = lambda old: old + old
        else:
            operation2 = lambda old: old + op_num2
    elif op_op2 == '-':
        if itself:
            operation2 = lambda old: 0
        else:
            operation2 = lambda old: old - op_num2
    else:
        print('UNKNOWN op_op')
        operation2 = lambda old: 0
    return operation2


def get_test(test_num3):
    test3 = lambda x: x % test_num3 == 0
    return test3


def get_throw_to(test_num2, true_test_monkey2, false_test_monkey2):
    return lambda x: true_test_monkey2 if x % test_num2 == 0 else false_test_monkey2


def read_monkeys(file_lines):
    read_debug = False
    line_num = 0
    test_op = ""
    start_items = []
    operation = lambda x: x

    monkey_bunch = MonkeyBunch()

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
                op_num = monkey_num
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
                throw_to_func = get_throw_to(test_num, true_test_monkey, false_test_monkey)
        elif file_line == '':
            monkey_bunch.add_monkey(monkey_num, start_items, operation, op_complete, test_op, test_complete, test_num,
                                    false_test_monkey, true_test_monkey,  throw_to_func)
            if read_debug:
                print(f'monkey {monkey_num} read')
                print()
    return monkey_bunch

# ======================================
# MAIN
# ======================================

test = False
test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)
monkey_bunch = read_monkeys(file_lines)

calc_debug = True
inspected_debug = True
for mround in range(1, 100):
    inspected_debug = True if mround in [1, 20] else False
    if inspected_debug:
        print(mround)
    debug_times = False
    if debug_times:
        round_st = time.time()
    for mnum, monkey_obj in monkey_bunch.monkeys.items():
        if debug_times:
            read_monkey_st = time.time()
        monkey_obj = monkey_bunch.monkeys[mnum]
        if debug_times:
            read_monkey_end = time.time()
            read_monkey_elapsed_time = read_monkey_end - read_monkey_st
            print(f"   read monkey {mnum}, tijdsduur: {read_monkey_elapsed_time}")
        if debug_times:
            monkey_st = time.time()
        monkey_obj.inspect_items()
        if debug_times:
            monkey_end = time.time()
            monkey_elapsed_time = monkey_end - monkey_st
            print(f"   monkey {mnum}, tijdsduur: {monkey_elapsed_time}")
    if debug_times:
        round_end = time.time()
        round_elapsed_time = round_end - round_st
        print(f" round {mnum}, tijdsduur: {round_elapsed_time}")
    if calc_debug:
        for monkey in monkey_bunch.monkeys.values():
            print(f"round {mround}:", end="")
            print(monkey)
    if inspected_debug:
        for monkey in monkey_bunch.monkeys.values():
            print(f"  Monkey {monkey.monkey_num} inspected items: {monkey.inspected}")
print(f"Level of Monkey business: {monkey_bunch.get_monkey_business()}")

print('finished')
