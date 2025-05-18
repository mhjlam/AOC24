import sys

def check_seq(sequence, target='XMAS'):
    return sequence == target or sequence == target[::-1]

def part1(verbose=False):
    with open('input/day04') as f:
        map = [list(i.strip()) for i in f.read().split('\n')]

    hits = 0
    height = len(map)
    width = len(map[0])

    for y in range(height):
        for x in range(width):
            seqs = []

            # horizontal
            if x + 3 < width:
                seqs.append(str.join('', map[y][x:x+4]))

            # vertical
            if y + 3 < height:
                seqs.append(str.join('', [map[y+i][x] for i in range(0,4)]))

            # diagonal (top-left to bottom-right)
            if y + 3 < height and x + 3 < width:
                seqs.append(str.join('', [map[y+i][x+i] for i in range(0,4)]))

            # diagonal (top-right to bottom-left)
            if y + 3 < height and x - 3 >= 0:
                seqs.append(str.join('', [map[y+i][x-i] for i in range(0,4)]))

            for seq in seqs:
                hit = int(check_seq(seq))
                hits += hit
                if verbose and hit:
                    print(f'Found: {seq}')

    return hits

def part2(verbose=False):
    def check_seq(sequence, target='MAS'):
        return sequence == target or sequence == target[::-1]

    with open('input/day04') as f:
        map = [list(i.strip()) for i in f.read().split('\n')]

    hits = 0
    height = len(map)
    width = len(map[0])

    for y in range(1, height-1):
        for x in range(1, width-1):
            if map[y][x] == 'A':
                diag1 = str.join('', [map[y+i][x+i] for i in range(-1,2)])
                diag2 = str.join('', [map[y-i][x+i] for i in range(-1,2)])
                hit = int(check_seq(diag1) and check_seq(diag2))
                hits += hit
                if verbose and hit:
                    print(f'Found: {diag1}, {diag2}')

    return hits

if __name__ == '__main__':
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    part1 = part1(verbose)
    part2 = part2(verbose)
    print(f'{part1} {part2}')
