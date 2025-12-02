size = 100
pos = 50
zeros_part1 = zeros_part2 = 0

with open('01.txt', 'r') as in_file:
    for line in in_file.readlines():
        new_pos = pos + int(line[1:]) * (-1) ** (line[0] == 'L')
        zeros_part2 += abs(new_pos) // size + (pos > 0 >= new_pos)
        zeros_part1 += (pos := new_pos % size) == 0

print(zeros_part1)
print(zeros_part2)
