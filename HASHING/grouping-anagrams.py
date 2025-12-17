"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map=defaultdict(list)

        for word in strs:
            sorted_key=tuple(sorted(word))

            anagrams_map[sorted_key].append(word)
        return list(anagrams_map.values())
