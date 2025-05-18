import sys
import operator

def part1(verbose=False):
    with open('input/day02') as f:
        input = f.read().splitlines()

    num_safe = 0

    for line in input:
        levels = []
        [levels.append(int(x)) for x in line.split()]

        test_difference = all(abs(j-i) > 0 and abs(j-i) < 4 for i,j in zip(levels, levels[1:]))
        test_increasing = all(i < j for i, j in zip(levels, levels[1:]))
        test_decreasing = all(i > j for i, j in zip(levels, levels[1:]))

        test = test_difference and (test_increasing or test_decreasing)

        if test:
            num_safe += 1

        if verbose:
            print(f'{levels}: {'Safe' if test else 'Unsafe'}')

    return num_safe

def test_report(levels):
    # first check if levels are increasing or decreasing
    op = operator.gt if (levels[0] - levels[-1]) > 0 else operator.lt

    correct = 0
    for i,j in zip(levels, levels[1:]):
        if op(i,j) and 1 <= abs(j-i) <= 3:
            correct += 1
    return correct == len(levels)-1

def part2(verbose=False):
    with open('input/day02') as f:
        input = f.read().splitlines()

    num_safe = 0

    for line in input:
        levels = []
        [levels.append(int(x)) for x in line.split()]

        safe = test_report(levels)
        if safe:
            num_safe += 1
        else: # try again with one less element popped out
            for i in range(len(levels)):
                popped = levels.pop(i)
                safe = test_report(levels)
                levels.insert(i, popped)
                if safe:
                    num_safe += 1
                    break

        if verbose:
            print(f'{levels}: {'Safe' if safe else 'Unsafe'}')

    return num_safe

if __name__ == '__main__':
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    part1 = part1(verbose)
    part2 = part2(verbose)
    print(f'{part1} {part2}')
