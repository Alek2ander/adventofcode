import math

connections = 1000

box_pairs, boxes, circuits = [], {}, []
with (open('08.txt', 'r') as in_file):
    while line := in_file.readline().strip():
        box = tuple(map(int, line.split(',')))
        for other in boxes:
            box_pairs.append((sum((x1 - x2) ** 2 for x1, x2 in zip(box, other)), box, other))
        boxes[box] = len(circuits)
        circuits.append({box})
for i, (_, box1, box2) in enumerate(sorted(box_pairs)):
    circuit1, circuit2 = boxes[box1], boxes[box2]
    if circuit1 == circuit2:
        continue
    circuits[circuit1] |= circuits[circuit2]
    for box in circuits[circuit2]:
        boxes[box] = circuit1
    circuits[circuit2].clear()
    if i == connections:
        print(math.prod(len(x) for x in sorted(circuits, key=len, reverse=True)[:3]))
    if len(circuits[circuit1]) == len(circuits):
        print(box1[0] * box2[0])
        break
