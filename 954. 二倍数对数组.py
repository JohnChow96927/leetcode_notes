"""
给定一个长度为偶数的整数数组 arr
只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]”时，返回 true；否则，返回 false。

示例 1：

输入：arr = [3,1,3,6]
输出：false
示例 2：

输入：arr = [2,1,2,6]
输出：false
示例 3：

输入：arr = [4,-2,2,-4]
输出：true
解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]

提示：

0 <= arr.length <= 3 * 104
arr.length 是偶数
-105 <= arr[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/array-of-doubled-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import Counter, List


def canReorderDoubled(arr: List[int]) -> bool:
    cnt = Counter(arr)
    if cnt[0] % 2:
        return False
    for x in sorted(cnt, key=abs):
        if cnt[2 * x] < cnt[x]:  # 无法找到足够的 2x 与 x 配对
            return False
        cnt[2 * x] -= cnt[x]
    return True


if __name__ == '__main__':
    xlist = [4, -2, 2, -4]
    print(canReorderDoubled(xlist))
