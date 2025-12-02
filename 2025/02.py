import math

sum_part1 = sum_part2 = 0

with (open('02.txt', 'r') as in_file):
    for id_range in in_file.read().split(','):
        l, r = map(int, id_range.strip().split('-'))
        hits = set()
        for scale in range(int(math.log10(l) + 1), int(math.log10(r) + 1) + 1):
            scale_l, scale_r = max(10 ** (scale - 1), l), min(10 ** scale - 1, r)
            for w in range(1, scale // 2 + 1):
                if scale % w != 0:
                    continue
                l_part = (scale_l // 10 ** (scale - w)) % (10 ** w)
                r_part = (scale_r // 10 ** (scale - w)) % (10 ** w)
                hits |= (h := set(s for n in range(l_part, r_part + 1)
                        if scale_l <= (s := sum(n * 10 ** p for p in range(0, scale, w))) <= scale_r))
                sum_part1 += sum(h) if scale // w == 2 else 0
        sum_part2 += sum(hits)

print(sum_part1)
print(sum_part2)
