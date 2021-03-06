"""
Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，
并且由 groupSize 张连续的牌组成。

给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。
如果她可能重新排列这些牌，返回 true ；否则，返回 false 。

示例 1：

输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
输出：true
解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
示例 2：

输入：hand = [1,2,3,4,5], groupSize = 4
输出：false
解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。

提示：
1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
"""
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 首先排除不能被除尽的情况
        if len(hand) % groupSize != 0:
            return False
        else:
            # 理牌逻辑:先将牌从小到大排
            hand.sort()
            # 理出一把顺子就拿出去
            # 使用list.remove(target)删除一个目标数字
            while True:
                if len(hand) == 0:  # 如果牌理完了则返回True
                    return True
                first_num = hand[0]     # 从手中最小的牌开始理
                for i in range(groupSize):
                    if first_num + i in hand:
                        hand.remove(first_num + i)  # 找到一张拿出去一张
                    else:
                        return False
