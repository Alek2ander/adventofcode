from collections import deque
from scipy.optimize import LinearConstraint, milp

sum_part1 = sum_part2 = n = 0
with (open('10.txt', 'r') as in_file):
    while line := in_file.readline().strip():
        n += 1
        line_i, *lines_b, line_j = line.split(' ')
        indicators = sum(2 ** i * (1 if c == '#' else 0) for i, c in enumerate(line_i[1:-1]))
        buttons = tuple(sum(2 ** i for i in map(int, line_b[1:-1].split(','))) for line_b in lines_b)
        joltages = tuple(map(int, line_j[1:-1].split(',')))
        states, queue = {0: 0}, deque((0,))
        while queue:
            presses = states[state := queue.popleft()]
            for button in buttons:
                if (new_state := state ^ button) in states:
                    continue
                states[new_state] = presses + 1
                if new_state == indicators:
                    break
                queue.append(new_state)
            if indicators in states:
                sum_part1 += states[indicators]
                break
        states, queue = {tuple([0] * len(joltages)): 0}, deque((tuple([0] * len(joltages)),))
        button_matrix = [[(button & (1 << i)) >> i for button in buttons] for i in range(len(joltages))]
        sum_part2 += int(sum(milp([1] * len(buttons), integrality=1,
            constraints=LinearConstraint(button_matrix, lb=joltages, ub=joltages)).x))
print(sum_part1)
print(sum_part2)
