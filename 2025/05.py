from sortedcontainers import SortedDict

with (open('05.txt', 'r') as in_file):
    ranges = SortedDict()
    while s := in_file.readline().strip():
        l, r = map(int, s.split('-'))
        idx = ranges.bisect_right(l)
        if idx < len(ranges) and ranges.peekitem(idx)[0] <= r + 1:
            r = max(r, ranges.popitem(idx)[1])
        if idx > 0 and (left := ranges.peekitem(idx - 1))[1] >= l - 1:
            l, r = left[0], max(r, ranges[left[0]])
        ranges[l] = r
    part1_count = 0
    while s := in_file.readline().strip():
        if (idx := ranges.bisect_right(i := int(s))) > 0 and ranges.peekitem(idx - 1)[1] >= i:
            part1_count += 1
print(part1_count)
print(sum(r - l + 1 for l, r in ranges.items()))
