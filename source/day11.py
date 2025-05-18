import sys
from collections import Counter, defaultdict

def part1(verbose=False):
    with open('input/day11') as file:
        input = file.read().strip()
    stones = list(map(int, input.split()))
    if verbose:
        print(stones)
    blinks = 0
    while blinks < 25:
        new_stones = []
        for i in range(len(stones)):
            digits = str(stones[i])
            if stones[i] == 0:
                new_stones.append(1)
            elif len(digits) % 2 == 0:
                half = len(digits)//2
                new_stones.append(int(digits[:half]))
                new_stones.append(int(digits[half:]))
            else:
                new_stones.append(stones[i] * 2024)
        stones = new_stones
        if verbose:
            print(stones)
        blinks += 1
    return len(stones)

def mutate(stone):
    if stone == 0:
        return [1]
    digits = str(stone)
    half, remainder = divmod(len(digits), 2)
    if remainder == 0:
        return map(int, (digits[:half], digits[half:]))
    return [stone * 2024]

def part2(verbose=False):
    with open('input/day11') as file:
        input = file.read().strip()
    stones = Counter(int(num) for num in input.split())
    for _ in range(75):
        new_stones = defaultdict(int)
        for stone, num in stones.items():
            for child in mutate(stone):
                new_stones[child] += num
        stones = new_stones
        if verbose:
            print(dict(stones))
    return sum(stones.values())

if __name__ == '__main__':
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    part1 = part1(verbose)
    part2 = part2(verbose)
    print(f'{part1} {part2}')
