# def swap_case(s):
#     res = ""
#     for i in s:
#         if i.isupper():
#             res += i.lower()
#         elif i.islower():
#             res += i.upper()
#         else:
#             res += i
#     return res

def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
