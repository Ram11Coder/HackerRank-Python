def mutate_string(val, pos, ch):
    input_list = list(val)
    input_list[pos] = ch
    return ''.join(input_list)


def mutate_string_oneliner(input_value, pos, ch):
    return input_value[:pos] + ch + input_value[pos + 1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string_oneliner(s, int(i), c)
    print(s_new)
