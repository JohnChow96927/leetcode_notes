from typing import List


def slowestKey(releaseTimes: List[int], keysPressed: str) -> str:
    slowest = releaseTimes[0]
    ch_list = [keysPressed[0]]
    for i in range(1, len(releaseTimes)):
        if releaseTimes[i] - releaseTimes[i - 1] > slowest:
            slowest = releaseTimes[i] - releaseTimes[i - 1]
            ch_list = [keysPressed[i]]
        elif releaseTimes[i] - releaseTimes[i - 1] == max:
            ch_list.append(keysPressed[i])
    ch_list.sort()
    return ch_list[-1]
