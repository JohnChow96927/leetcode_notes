def lastRemaining(n: int) -> int:
    arr = [i for i in range(1, n + 1)]
    while len(arr) > 1:
        arr = arr[:: -1]
        for i in range(len(arr) - 1, -1, -2):
            del arr[i]
    return arr[0]
