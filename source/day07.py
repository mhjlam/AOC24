import sys
from itertools import product

def op_add(a,b): return a+b

def op_mul(a,b): return a*b

def part1(verbose=False):
    def test(target, numbers):
        combinations = list(product([op_add, op_mul], repeat=len(numbers)-1))
        for operators in combinations:
            result = numbers[0]
            for i, op in enumerate(operators):
                result = op(result, numbers[i+1])
            if result == target:
                return target
        return 0

    with open('input/day07') as file:
        equations = [(int(key), list(map(int, value.split()))) for key, value in [line.split(':') for line in file.read().splitlines()]]

    total = 0
    for target, numbers in equations:
        val = test(target, numbers)
        total += val
        if verbose:
            print(f'{target}, {numbers} -> {val}')
    return total

def op_cat(a,b): return int(str(a) + str(b))

def part2(verbose=False):
    def test(target, numbers):
        combinations = list(product([op_add, op_mul, op_cat], repeat=len(numbers)-1))
        for operators in combinations:
            result = numbers[0]
            for i, op in enumerate(operators):
                result = op(result, numbers[i+1])
            if result == target:
                return target
        return 0

    with open('input/day07') as file:
        equations = [(int(key), list(map(int, value.split()))) for key, value in [line.split(':') for line in file.read().splitlines()]]

    total = 0
    for target, numbers in equations:
        val = test(target, numbers)
        total += val
        if verbose:
            print(f'{target}, {numbers} -> {val}')
    return total

if __name__ == '__main__':
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    part1 = part1(verbose)
    part2 = part2(verbose)
    print(f'{part1} {part2}')
