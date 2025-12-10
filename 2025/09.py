with (open('09.txt', 'r') as in_file):
    tiles = [tuple(map(int, line.strip().split(','))) for line in in_file.readlines()]
max_rect_part1 = max_rect_part2 = 0
for i, tile1 in enumerate(tiles):
    for j, tile2 in enumerate(tiles[i + 1:], i + 1):
        if (rect := (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)) <= max_rect_part2:
            continue
        if rect > max_rect_part1:
            max_rect_part1 = rect
        l, r, u, d = min(tile1[0], tile2[0]), max(tile1[0], tile2[0]), min(tile1[1], tile2[1]), max(tile1[1], tile2[1])
        valid = True
        for k in range(len(tiles)):
            if l < tiles[k][0] < r and (tiles[k - 1][1] <= u < tiles[k][1] or tiles[k - 1][1] >= d > tiles[k][1]) \
            or u < tiles[k][1] < d and (tiles[k - 1][0] <= l < tiles[k][0] or tiles[k - 1][0] >= r > tiles[k][0]):
                valid = False
                break
        if valid:
            max_rect_part2 = rect
print(max_rect_part1)
print(max_rect_part2)
