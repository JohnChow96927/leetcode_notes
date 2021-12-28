"""
给你一个不含重复单词的字符串数组words ，请你找出并返回 words 中的所有连接词。
连接词定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。
示例：
输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成;
     "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成;
     "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
"""
from typing import List


class Solution:
    @staticmethod
    def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
        result = []
        
        nominee = ''
        return result


sol = Solution()
print(sol.findAllConcatenatedWordsInADict(
    ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))
