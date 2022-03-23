def solution(lst):
    sorted_list = sorted(lst)
    result = []
    for j in range(len(sorted_list)):
        if j == 0:
            for i in range(1, sorted_list[j]):
                if i != sorted_list[j]:
                    result.append(i)
        else:
            for i in range(sorted_list[j - 1] + 1, sorted_list[j]):
                if i != sorted_list[j]:
                    result.append(i)
    return result


if __name__ == '__main__':
    print(solution([3, 9, 1, 4, 7]))
