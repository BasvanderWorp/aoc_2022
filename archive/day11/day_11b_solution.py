"""
Advent of Code 2022
Day 11

wow het wiskundige trucje:


The problem here is that with the Part 1 solution, the worry scores get very, very fast.
This solution is going to take too long. We need a way to make these scores smaller.
A≡B(mod C)
A is congruent to B mod C.
≡ means "is congruent to". I.e. that it belongs in the same remainder class, or bucket.
Numbers are "congruent modulo n" if they have the same remainder after division.
If a≡b(mod M) and b=d(mod m) then a≡d(mod m)
If a≡b(mod m), then a+c≡b+c(mod m)
If a≡b(mod m), then ax≡bx(mod mx)

Modulo congruence is preserved with addition and multiplication (in our worry op).
And we're not dividing any more, which would break conguence.
So we only need to maintain a number which preserves the remainder, not the actual worry score.
So, we can just store %w(mod n). And for n, we can use the LCM of all our divisors.

"""
from helpers.io import read_input
import math

throw_debug = True


class MonkeyBunch:
    def __init__(self):
        self.monkeys = {}

    def __repr__(self):
        return f"{self.monkeys}"

    def add_monkey(self, monkey_num, starting_items, wl_op, wl_op_txt, test_op, divisor, test_op_txt, throw_to_false,
                   throw_to_true, throw_to):
        new_monkey = Monkey(monkey_num, starting_items, wl_op, wl_op_txt, test_op, divisor, test_op_txt, throw_to_false,
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
    def __init__(self, monkey_num, starting_items, wl_op, wl_op_txt, test_op, divisor, test_op_txt, throw_to_false,
                 throw_to_true, throw_to_op, monkey_bunch):
        self.monkey_num = monkey_num
        self.starting_items = starting_items
        self.wl_op = wl_op
        self.wl_op_txt = wl_op_txt
        self.test_op = test_op
        self.divisor = divisor
        self.test_op_txt = test_op_txt
        self.throw_to_false = throw_to_false
        self.throw_to_true = throw_to_true
        self.throw_to_op = throw_to_op
        self.inspected = 0
        self.bunch = monkey_bunch

    def __repr__(self):
        return f"Monkey {self.monkey_num}: items={self.starting_items}, wl_op={self.wl_op_txt}, " \
               f"test_op={self.test_op_txt}, throw_to_false={self.throw_to_false}, throw_to_true={self.throw_to_true}," \
               f"inspected={self.inspected}"

    def inspect_items(self, lcm=None):
        items_to_remove  = []
        for idx, item in enumerate(self.starting_items):
            self.inspect_item(idx, lcm)
            items_to_remove.append(item)
        for item in items_to_remove:
            self.starting_items.remove(item)

    def inspect_item(self, idx, lcm=None):
        item = self.starting_items[idx]
        wlevel = self.wl_op(item)
        wlevel_bored = wlevel % lcm
        throw_to_monkey = self.throw_to_op(wlevel_bored)
        self.bunch.monkeys[throw_to_monkey].starting_items.append(wlevel_bored)
        self.inspected += 1


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
            monkey_bunch.add_monkey(monkey_num, start_items, operation, op_complete, test_op, test_num, test_complete,
                                    false_test_monkey, true_test_monkey,  throw_to)
            if read_debug:
                print(f'monkey {monkey_num} read')
                print()
    return monkey_bunch

# ======================================
# MAIN
# ======================================

test = False
# test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)
monkey_bunch = read_monkeys(file_lines)

lcm = math.lcm(*[monkey.divisor for monkey in monkey_bunch.monkeys.values()])
inspected_debug = True
calc_debug = True

if calc_debug:
    print('Initial monkeys:')
    for monkey_obj in monkey_bunch.monkeys.values():
        print('    ', end="")
        print(monkey_obj)
for mround in range(1, 10001):
    calc_debug = True if mround in [1, 20, 1000, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 10000] else False
    inspected_debug = True if mround in [1, 20, 1000, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 10000] else False
    if calc_debug:
        print(f'Round {mround}')
    for mnum, monkey_obj in monkey_bunch.monkeys.items():
        monkey_obj = monkey_bunch.monkeys[mnum]
        if calc_debug:
            print('    ', end="")
            print(monkey_obj)
        monkey_obj.inspect_items(lcm)
    if inspected_debug:
        for monkey in monkey_bunch.monkeys.values():
            print(f"  Monkey {monkey.monkey_num} inspected items: {monkey.inspected}")

print(f"Level of Monkey business: {monkey_bunch.get_monkey_business()}")

print('finished')
