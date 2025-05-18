import sys

def part1(verbose=False):
    list1 = []
    list2 = []

    with open('input/day01') as f:
        lines = f.read().splitlines()

    for line in lines:
        values = line.split('   ')
        list1.append(int(values[0]))
        list2.append(int(values[1]))

    list1.sort()
    list2.sort()

    total_distance = 0
    for (item1, item2) in zip(list1, list2):
        distance = abs(item1 - item2)
        total_distance += distance
        if verbose:
            print(f'|{item1} - {item2}| = {distance}')

    return total_distance

def part2(verbose=False):
    list1 = []
    list2 = []

    with open('input/day01') as f:
        lines = f.read().splitlines()

    for line in lines:
        values = line.split('   ')
        list1.append(int(values[0]))
        list2.append(int(values[1]))

    list1.sort()
    list2.sort()

    similarity_score = 0
    for item1 in list1:
        occurrences = list2.count(item1)
        similarity_score += item1 * occurrences
        if verbose:
            print(f'{item1} * {occurrences} = {item1 * occurrences}')

    return similarity_score

if __name__ == '__main__':
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    part1 = part1(verbose)
    part2 = part2(verbose)
    print(f'{part1} {part2}')
