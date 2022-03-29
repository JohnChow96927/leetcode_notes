def main(x):
    if x <= 1:
        return x
    left = 0
    right = x
    while left < right:
        mid = left + (right - left) / 2
        if (x / mid) >= mid:
            left = mid + 1
        else:
            right = mid
    return int(right - 1)


if __name__ == '__main__':
    x = int(input())
    print(main(x))
