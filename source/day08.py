import sys
from copy import deepcopy
from itertools import combinations
from collections import defaultdict

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __hash__(self):
        return hash((self.x, self.y))
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __add__(self, other):
        p = Point(self.x + other.x, self.y + other.y)
        return p
    def in_bounds(self, width, height):
        return 0 <= self.x < width and 0 <= self.y < height
Vector = Point

def show_grid(grid, antinodes=[]):
    newgrid = deepcopy(grid)
    for node in antinodes:
        newgrid[node.y][node.x] = '#'
    height = len(grid)
    width = len(grid[0])
    for r in range(height):
        for c in range(width):
            print(newgrid[r][c], end='')
        print('')

def part1(verbose=False):
    with open('input/day08') as file:
        input = file.read()
    grid = [list(line) for line in input.strip().splitlines()]
    height = len(grid)
    width = len(grid[0])
    antennas = defaultdict(set)
    antinodes = set()
    for r in range(height):
        for c in range(width):
            v = grid[r][c]
            if v.isalnum():
                antennas[v].add(Point(c, r))
    for at in antennas:
        combos = list(combinations(antennas[at], 2))
        for (p0, p1) in combos:
            q0 = p0 + Vector(p0.x - p1.x, p0.y - p1.y)
            q1 = p1 + Vector(p1.x - p0.x, p1.y - p0.y)
            if q0.in_bounds(width, height):
                antinodes.add(q0)
            if q1.in_bounds(width, height):
                antinodes.add(q1)
    if verbose:
        show_grid(grid, antinodes)
    return len(antinodes)

def part2(verbose=False):
    with open('input/day08') as file:
        input = file.read()
    grid = [list(line) for line in input.strip().splitlines()]
    height = len(grid)
    width = len(grid[0])
    antennas = defaultdict(set)
    antinodes = set()
    for y in range(height):
        for x in range(width):
            cell = grid[y][x]
            if cell.isalnum():
                antennas[cell].add(Point(x, y))
    for at in antennas:
        combos = list(combinations(antennas[at], 2))
        for (p0, p1) in combos:
            v0 = Vector(p0.x - p1.x, p0.y - p1.y)
            v1 = Vector(p1.x - p0.x, p1.y - p0.y)
            while p0.in_bounds(width, height):
                antinodes.add(p0)
                p0 += v0
            while p1.in_bounds(width, height):
                antinodes.add(p1)
                p1 += v1
    return len(antinodes)

if __name__ == '__main__':
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    part1 = part1(verbose)
    part2 = part2(verbose)
    print(f'{part1} {part2}')
