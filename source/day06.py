import sys
import copy
from collections import namedtuple, defaultdict

Cell = namedtuple('Cell', 'x y val')
Position = namedtuple('Position', 'x y')
Direction = namedtuple('Direction', 'x y')

def load_grid():
    with open('input/day06') as file:
        input_data = file.read()
        grid = [list(line) for line in input_data.splitlines()]
    height = len(grid)
    index = input_data.index('^')
    start_pos = Position(index - ((index//height - 1) * (height+1)), index//height - 1)
    start_dir = Direction(0, -1)
    return grid, start_pos, start_dir

def trace_path_part1(grid, start_pos, start_dir):
    visited = set()
    out_of_bounds = False
    pos = Position(start_pos.x, start_pos.y)
    dir = Direction(start_dir.x, start_dir.y)
    while not out_of_bounds:
        vertical = [Cell(pos.x, i, row[pos.x]) for i, row in enumerate(grid)]
        horizontal = [Cell(i, pos.y, val) for i, val in enumerate(grid[pos.y])]
        if dir.y < 0: path = vertical[pos.y-1::-1]
        elif dir.y > 0: path = vertical[pos.y+1:]
        elif dir.x < 0: path = horizontal[pos.x-1::-1]
        elif dir.x > 0: path = horizontal[pos.x+1:]
        out_of_bounds = True
        for cell in path:
            if cell.val == '#':
                out_of_bounds = False
                dir = Direction(-dir.y, dir.x)
                break
            pos = Position(cell.x, cell.y)
            visited.add(pos)
        if out_of_bounds:
            return visited

def trace_path_part2(grid, start_pos, start_dir):
    visited = defaultdict(list)
    pos = copy.copy(start_pos)
    dir = copy.copy(start_dir)
    out_of_bounds = False
    while not out_of_bounds:
        vertical = [Cell(pos.x, i, row[pos.x]) for i, row in enumerate(grid)]
        horizontal = [Cell(i, pos.y, val) for i, val in enumerate(grid[pos.y])]
        if dir.y < 0: path = vertical[pos.y-1::-1]
        elif dir.y > 0: path = vertical[pos.y+1:]
        elif dir.x < 0: path = horizontal[pos.x-1::-1]
        elif dir.x > 0: path = horizontal[pos.x+1:]
        out_of_bounds = True
        for cell in path:
            if cell.val == '#' or cell.val == 'O':
                out_of_bounds = False
                dir = Direction(-dir.y, dir.x)
                break
            pos = Position(cell.x, cell.y)
            if pos in visited and dir in visited[pos]:
                return visited, True
            visited[pos].append(dir)
    if out_of_bounds:
        return visited, False

def part1(verbose=False):
    grid, start_pos, start_dir = load_grid()
    visited = trace_path_part1(grid, start_pos, start_dir)
    if verbose:
        print(f'Visited positions: {visited}')
    return len(visited)+1

def part2(verbose=False):
    grid, start_pos, start_dir = load_grid()
    visited, _ = trace_path_part2(grid, start_pos, start_dir)
    if verbose:
        print(f'Visited positions: {visited}')
    loop_paths = []
    for v in visited:
        grid[v.y][v.x] = 'O'
        path, loops = trace_path_part2(grid, start_pos, start_dir)
        if loops:
            loop_paths.append(path)
        grid[v.y][v.x] = '.'
    if verbose:
        print(f'Loop paths: {loop_paths}')
    return len(loop_paths)

if __name__ == '__main__':
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    part1 = part1(verbose)
    part2 = part2(verbose)
    print(f'{part1} {part2}')
