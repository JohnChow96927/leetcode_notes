"""
给你一个 下标从 0 开始 的整数数组 nums ，
返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：
nums[a] + nums[b] + nums[c] == nums[d] ，且 a < b < c < d

示例 1：
输入：nums = [1,2,3,6]
输出：1
解释：满足要求的唯一一个四元组是 (0, 1, 2, 3) 因为 1 + 2 + 3 == 6 。
示例 2：
输入：nums = [3,3,6,4,5]
输出：0
解释：[3,3,6,4,5] 中不存在满足要求的四元组。
示例 3：
输入：nums = [1,1,1,3,5]
输出：4
解释：满足要求的 4 个四元组如下：
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5
提示：

4 <= nums.length <= 50
1 <= nums[i] <= 100

链接：https://leetcode-cn.com/problems/count-special-quadruplets
"""
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        temp_diff_list = []
        # 设a, b, c, d为四个数字对应的下标, a < b < c < d
        for b in range(n - 3, 0, -1):
            for d in range(b + 2, n):
                temp_diff_list.append(nums[d] - nums[b + 1])
            for a in range(b):
                if nums[a] + nums[b] in temp_diff_list:
                    print(a, b)
                    result += temp_diff_list.count(nums[a] + nums[b])
        return result


sol = Solution()
print(sol.countQuadruplets([1, 1, 1, 3, 5]))
