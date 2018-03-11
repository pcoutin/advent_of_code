import sys

checksum = 0

for line in sys.stdin:
    if len(line) < 5:
        pass

    nums = [int(n) for n in line.split()]

    for n1 in nums:
        for n2 in nums:
            # requires all numbers in each row to be different
            if n1 % n2 == 0 and n1 != n2:
                checksum += n1 / n2

print(checksum)
