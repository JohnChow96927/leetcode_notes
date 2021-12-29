from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1 + nums2) == 0:
        return float(0)
    new_nums = sorted(nums1 + nums2)
    n = len(new_nums)
    if n % 2 == 0:
        return (new_nums[n // 2] + new_nums[n // 2 - 1]) / 2
    else:
        return float(new_nums[n // 2])


print(findMedianSortedArrays([1, 2, 3], [2, 5, 6, 78]))
