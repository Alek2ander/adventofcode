import math

operators = {
    '+': sum,
    '*': math.prod
}

operands_part1, operands_part2, actions, column_anchors = [], [], [], []
with (open('06.txt', 'r') as in_file):
    for y, line in enumerate(in_file):
        column, number = -1, False
        for x, c in enumerate(line):
            if not number and '0' <= c <= '9':
                column, number = column + 1, True
                if column >= len(column_anchors):
                    column_anchors.append(x)
                    operands_part1.append([])
                    operands_part2.append([])
                elif (old_anchor := column_anchors[column]) > x:
                    operands_part2[column] = [0] * (old_anchor - x) + operands_part2[column]
                    column_anchors[column] = x
                if len(operands_part1[column]) <= y:
                    operands_part1[column].append(0)
            if '0' <= c <= '9':
                shift = x - column_anchors[column]
                if len(operands_part2[column]) <= shift:
                    operands_part2[column].append(0)
                operands_part1[column][y] = operands_part1[column][y] * 10 + int(c)
                operands_part2[column][shift] = operands_part2[column][shift] * 10 + int(c)
            elif c in operators:
                actions.append(operators[c])
            else:
                number = False
print(sum(action(operands) for action, operands in zip(actions, operands_part1)))
print(sum(action(operands) for action, operands in zip(actions, operands_part2)))
