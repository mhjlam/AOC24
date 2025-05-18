import sys

def show(garden):
    for row in range(len(garden)):
        for col in range(len(garden[row])):
            print(garden[row][col], end='')
        print()
    print()

def perimeter(garden, height, width, r, c):
    type = garden[r][c]
    region = set()
    fence = 0
    plants = [(r,c)]
    while plants:
        r, c = plants.pop()
        if (r, c) in region:
            continue
        if r not in range(height) or c not in range(width) or garden[r][c] != type:
            fence += 1
            continue
        region.add((r,c))
        if (r-1, c) not in region:
            plants.append((r-1, c))
        if (r+1, c) not in region:
            plants.append((r+1, c))
        if (r, c-1) not in region:
            plants.append((r, c-1))
        if (r, c+1) not in region:
            plants.append((r, c+1))
    cost = len(region) * fence
    return region, cost

def part1(verbose=False):
    with open('input/day12') as file:
        input = file.read().splitlines()
    garden = [list(i) for i in input]
    height = len(garden)
    width = len(garden[0])
    price = 0
    visited = set()
    for r in range(height):
        for c in range(width):
            if (r, c) not in visited:
                region, cost = perimeter(garden, height, width, r, c)
                visited |= region
                price += cost
                if verbose:
                    print(f'Region: {region}, Cost: {cost}')
    return price

def part2(verbose=False):
    pass

if __name__ == '__main__':
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    part1 = part1(verbose)
    part2 = part2(verbose)
    print(f'{part1} ?')
