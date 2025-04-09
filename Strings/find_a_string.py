# The str.count() method does not count overlapping substrings.
def count_substring(string, sub_string):
    res = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if string.startswith(sub_string, i):
            res += 1

    return res


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
