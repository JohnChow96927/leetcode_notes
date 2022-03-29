"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水
"""

def solution(lst):
    result = 0
    if len(lst) <= 2:
        return result
    left_index = 0
    right_index = len(lst) - 1
    left_max = 0
    right_max = 0
    while left_index < right_index:
        left_max = max(int(lst[left_index]), left_max)
        right_max = max(int(lst[right_index]), right_max)
        if int(lst[left_index]) < int(lst[right_index]):
            result += left_max - int(lst[left_index])
            left_index += 1
        else:
            result += right_max - int(lst[right_index])
            right_index -= 1
    return result


if __name__ == '__main__':
    lst = list(input()[1: -1].split(','))
    print(solution(lst))

