from sys import stdin


valid_passphrases = 0

def no_dupes(line):
    words = line.split()

    for word in words:
        if words.count(word) > 1:
            return 0

    return 1

for line in stdin:
    valid_passphrases += no_dupes(line)


print(valid_passphrases)
