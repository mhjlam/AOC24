import re
import sys

def part1(verbose=False):
    with open('input/day03') as f:
        input = f.read()

    muls = re.findall(r'mul\(\d+,\d+\)', input)

    total = 0
    for mul in muls:
        x, y = [int(x) for x in re.findall(r'\d+', mul)]
        total += x*y
        if verbose:
            print(f'{mul} = {x*y}')

    return total

def part2(verbose=False):
    with open('input/day03') as f:
        input = f.read()

    # remove everything between don't and do (or EOF)
    input = re.sub(r'don\'t\(\).*?($|do\(\))', '', input, flags=re.DOTALL) # also match newlines
    muls = re.findall(r'(mul\(\d+,\d+\))', input)

    total = 0
    for mul in muls:
        x, y = [int(x) for x in re.findall(r'\d+', mul)]
        total += x*y
        if verbose:
            print(f'{mul} = {x*y}')

    return total

if __name__ == '__main__':
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    part1 = part1(verbose)
    part2 = part2(verbose)
    print(f'{part1} {part2}')
