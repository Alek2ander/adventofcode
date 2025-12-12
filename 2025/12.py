import itertools

def fit_shape(grid, todo):
    if not todo:
        return True
    shape_idx = todo.pop()
    for shape in shapes[shape_idx]:
        for anchor_x in range(0, max_x - present_max_size + 1):
            for anchor_y in range(0, max_y - present_max_size + 1):
                if any(grid[anchor_y + y][anchor_x + x] for x, y in shape):
                    continue
                for x, y in shape:
                    grid[anchor_y + y][anchor_x + x] = True
                goals[shape_idx] -= 1
                if fit_shape(grid, todo):
                    return True
                else:
                    goals[shape_idx] += 1
                    for x, y in shape:
                        grid[anchor_y + y][anchor_x + x] = False
    todo.append(shape_idx)
    return False

present_max_size = 3
variations = (
    lambda x, y: (x, y), # base shape
    lambda x, y: (present_max_size - x - 1, y), # mirror horizontally
    lambda x, y: (present_max_size - y - 1, x), # rotate 90 clockwise
    lambda x, y: (y, x), # rotate 90 clockwise & mirror horizontally
    lambda x, y: (present_max_size - x - 1, present_max_size - y - 1), # rotate 180
    lambda x, y: (x, present_max_size - y - 1), # rotate 180 & mirror horizontally
    lambda x, y: (y, present_max_size - x - 1), # rotate 270
    lambda x, y: (present_max_size - y - 1, present_max_size - x - 1) # rotate 270 & mirror horizontally
)

shapes, shape_areas, tests = {}, {}, []
with (open('12.txt', 'r') as in_file):
    while line := in_file.readline().strip():
        if line.endswith(':'):
            idx, y, tiles = int(line[:-1]), 0, []
            while line := in_file.readline().strip():
                for x, c in enumerate(line):
                    if c == '#':
                        tiles.append((x, y))
                y += 1
            shapes[idx] = frozenset(frozenset(v(x, y) for x, y in tiles) for v in variations)
            shape_areas[idx] = len(tiles)
        else:
            sizes, goals = line.split(': ')
            tests.append((list(map(int, goals.split(' '))), *map(int, sizes.split('x'))))
count_part1 = 0
for goals, max_x, max_y in tests:
    if sum(shape_areas[i] * goal for i, goal in enumerate(goals)) > max_x * max_y:
        continue
    grid = [[False] * max_x for _ in range(max_y)]
    todo = list(itertools.chain.from_iterable([i] * v for i, v in enumerate(goals)))
    count_part1 += fit_shape(grid, todo)
print(count_part1)
