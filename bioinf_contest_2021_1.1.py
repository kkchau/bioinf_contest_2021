import sys

# Test A
# with open(sys.argv[1], "r") as fh:
#    tests = [_.split() for _ in fh.readlines()[1:]]
#
# for test in tests:
#    print(int(test[0]) + int(test[1]))

# Test B


def find_substring_indexes(s, t):
    indexes = []
    for i, letter in enumerate(s):
        if len(s) - i < len(t):
            break
        if s[i : i + len(t)] == t:
            indexes.append(i)
    return [_ + 1 for _ in indexes]


current_s = ""
current_t = ""
with open(sys.argv[1], "r") as fh:
    for line_num, line in enumerate(fh.readlines()[1:]):
        if line_num % 2 == 0:
            current_s = line.strip()
        else:
            current_t = line.strip()
        if current_s and current_t:
            print(
                " ".join([str(_) for _ in find_substring_indexes(current_s, current_t)])
            )
