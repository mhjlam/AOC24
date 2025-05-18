import sys

def trails1(topo, width, height, y, x):
    trail = [(y, x)]
    terminus = set()
    while trail:
        y, x = trail.pop()
        elevation = topo[y][x]
        if elevation == 9:
            terminus.add((y,x))
            continue
        if y > 0 and topo[y-1][x] == elevation+1:
            trail.append((y-1, x))
        if y < height-1 and topo[y+1][x] == elevation+1:
            trail.append((y+1, x))
        if x > 0 and topo[y][x-1] == elevation+1:
            trail.append((y, x-1))
        if x < width-1 and topo[y][x+1] == elevation+1:
            trail.append((y, x+1))
    return len(terminus)

def part1(verbose=False):
    with open('input/day10') as file:
        input = file.read().strip()
    topo = [[int(num) for num in row] for row in input.split('\n')]
    height, width = len(topo), len(topo[0])
    score = 0
    for y, x in [(i//width, i%width) for i, v in enumerate(input.replace('\n', '')) if v == '0']:
        val = trails1(topo, width, height, y, x)
        score += val
        if verbose:
            print(f'Start: ({y},{x}) -> {val}')
    return score

def trails2(y, x, topo, width, height):
    if (elevation := topo[y][x]) == 9:
        return 1
    rating = 0
    if y > 0 and topo[y-1][x] == elevation+1:
        rating += trails2(y-1, x, topo, width, height)
    if y < height-1 and topo[y+1][x] == elevation+1:
        rating += trails2(y+1, x, topo, width, height)
    if x > 0 and topo[y][x-1] == elevation+1:
        rating += trails2(y, x-1, topo, width, height)
    if x < width-1 and topo[y][x+1] == elevation+1:
        rating += trails2(y, x+1, topo, width, height)
    return rating

def part2(verbose=False):
    with open('input/day10') as file:
        input = file.read().strip()
    topo = [[int(num) for num in row] for row in input.split('\n')]
    height, width = len(topo), len(topo[0])
    rating_sum = 0
    for y, x in [(i//width, i%width) for i, v in enumerate(input.replace('\n', '')) if v == '0']:
        val = trails2(y, x, topo, width, height)
        rating_sum += val
        if verbose:
            print(f'Start: ({y},{x}) -> {val}')
    return rating_sum

if __name__ == '__main__':
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    part1 = part1(verbose)
    part2 = part2(verbose)
    print(f'{part1} {part2}')
