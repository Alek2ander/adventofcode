sum_part1 = 0
with (open('07.txt', 'r') as in_file):
    beams = {in_file.readline().find('S'): 1}
    splitters = [set(x for x in range(0, len(line)) if line[x] == '^')
                     for line in in_file.readlines()]
for splitter_row in splitters:
    if not splitter_row:
        continue
    new_beams = {}
    for x, weight in beams.items():
        if x in splitter_row:
            new_beams[x - 1] = weight + new_beams.get(x - 1, 0)
            new_beams[x + 1] = weight
            sum_part1 += 1
        else:
            new_beams[x] = beams[x] + new_beams.get(x, 0)
    beams = new_beams
print(sum_part1)
print(sum(weight for weight in beams.values()))
