def find_largest_digits(s, ndigits):
    digits = list(s[-ndigits:])
    for digit in s[-ndigits - 1::-1]:
        for i in range(ndigits):
            if digit > digits[i]:
                digits[i], digit = digit, digits[i]
            elif digit < digits[i]:
                break
    return digits

sum_part1 = sum_part2 = 0
with (open('03.txt', 'r') as in_file):
    for bank in in_file.readlines():
        sum_part1 += int(''.join(find_largest_digits(bank.strip(), 2)))
        sum_part2 += int(''.join(find_largest_digits(bank.strip(), 12)))

print(sum_part1)
print(sum_part2)
