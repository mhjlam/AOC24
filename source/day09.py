import sys

def blocks(input):
    id = 0
    disk_map = []
    for i, block_size in enumerate(input):
        if i % 2 == 0: # file
            disk_map += [id] * block_size
            id += 1
        else: # free space
            disk_map += [-1] * block_size
    return disk_map

def format1(disk_map: list):
    i = 0
    j = len(disk_map)-1
    while i < len(disk_map):
        try:
            i = disk_map.index(-1, i)
            if i > j: break
            disk_map[i], disk_map[j] = disk_map[j], disk_map[i] # swap
            j -= 1
        except:
            break
    return disk_map

def checksum1(disk_map):
    sum = 0
    for i, id in enumerate(disk_map):
        if id == -1:
            break
        sum += i * id
    return sum

def show_disk(disk_map):
    for i in disk_map:
        if i == -1:
            print('.', end='')
        else:
            print(str(i), end='')
    print('')

def part1(verbose=False):
    with open('input/day09') as f:
        input = list(map(int, f.read().strip()))
    disk_map = blocks(input)
    format1(disk_map)
    sum = checksum1(disk_map)
    if verbose:
        show_disk(disk_map)
    return sum

def index(disk_map):
    disk = []
    for i in range(len(disk_map)):
        x = int(disk_map[i])
        if i % 2 == 0: # file
            disk.append((i//2, x))
        else:
            disk.append((-1, x))
    return disk

def format2(disk):
    file_index = len(disk)-1
    while file_index > 0:
        file_id, file_blocks = disk[file_index]
        if file_id == -1:
            file_index -= 1
            continue
        free_index = next((j for j in range(file_index) if disk[j][0] == -1 and disk[j][1] >= file_blocks), None)
        if not free_index:
            file_index -= 1
            continue
        new_disk = disk[:free_index]
        new_disk += [(file_id, file_blocks)]
        block_diff = disk[free_index][1] - file_blocks
        if block_diff > 0:
            new_disk += [(-1, block_diff)]
        new_disk += disk[free_index+1:file_index]
        new_disk += [(-1, file_blocks)]
        new_disk += disk[file_index+1:]
        disk = new_disk
    return disk

def cleanup(disk):
    for i, (id, blocks) in enumerate(disk):
        if id == -1 and blocks == 0:
            del(disk[i])
    return disk

def checksum2(disk):
    sum = 0
    block = 0
    for id, blocks in disk:
        if id == -1:
            block += blocks
            continue
        for _ in range(blocks):
            sum += block * id
            block += 1
    return sum

def part2(verbose=False):
    with open('input/day09') as f:
        disk_map = list(map(int, f.read().strip()))
    disk = index(disk_map)
    disk = format2(disk)
    disk = cleanup(disk)
    sum = checksum2(disk)
    if verbose:
        print(disk)
    return sum

if __name__ == '__main__':
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    part1 = part1(verbose)
    part2 = part2(verbose)
    print(f'{part1} {part2}')
