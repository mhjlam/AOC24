import sys
from collections import defaultdict

def part1(verbose=False):
    with open('input/day05') as f:
        input = f.read()
    rules, updates = input.split('\n\n')
    rules = rules.split('\n')
    updates = updates.split('\n')[:-1]
    preceding_rules = defaultdict(set)
    for rule in rules:
        l, r = rule.split('|')
        preceding_rules[int(r)].add(int(l))
    def score(pages):
        disallowed_preceding = set()
        for page in pages:
            if page in disallowed_preceding:
                return 0
            disallowed_preceding.update(preceding_rules[page])
        return pages[len(pages)//2]
    total = 0
    for update in updates:
        pages = list(map(int, update.split(',')))
        val = score(pages)
        total += val
        if verbose:
            print(f'{pages} -> {val}')

    return total

def part2(verbose=False):
    with open('input/day05') as f:
        input = f.read()
    rules, updates = input.split('\n\n')
    rules = rules.split('\n')
    updates = updates.split('\n')[:-1]
    preceding_rules = defaultdict(set)
    for rule in rules:
        l, r = rule.split('|')
        preceding_rules[int(r)].add(int(l))
    def score(pages, reordered=False):
        disallowed = dict()
        for i, page in enumerate(pages):
            if page in disallowed:
                j = disallowed[page]
                reordered_pages = pages[:j] + [page] + pages[j:i] + pages[i+1:]
                return score(reordered_pages, True)
            for p in preceding_rules[page]:
                if p not in disallowed:
                    disallowed[p] = i
        return pages[len(pages)//2] if reordered else 0
    total = 0
    for update in updates:
        pages = list(map(int, update.split(',')))
        val = score(pages)
        total += val
        if verbose:
            print(f'{pages} -> {val}')

    return total

if __name__ == '__main__':
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    part1 = part1(verbose)
    part2 = part2(verbose)
    print(f'{part1} {part2}')
