directions = ((-1, 1),  (0, 1),  (1, 1),
              (-1, 0),           (1, 0),
              (-1, -1), (0, -1), (1, -1))

stuck = {}
removable = {}
with (open('04.txt', 'r') as in_file):
    for y, line in enumerate(in_file.readlines()):
        for x, c in enumerate(line.strip()):
            if c == '@':
                removable[this := (x, y)] = 0
                for d in directions:
                    if (other := (this[0] + d[0], this[1] + d[1])) in stuck:
                        stuck[other] += 1
                        removable[this] += 1
                    elif other in removable:
                        removable[other] += 1
                        removable[this] += 1
                        if removable[other] == 4:
                            stuck[other] = removable.pop(other)
                if removable[this] >= 4:
                    stuck[this] = removable.pop(this)
print(s := len(removable))
while removable:
    this, _ = removable.popitem()
    for d in directions:
        if (other := (this[0] + d[0], this[1] + d[1])) in stuck:
            stuck[other] -= 1
            if stuck[other] == 3:
                removable[other] = stuck.pop(other)
                s += 1
print(s)
