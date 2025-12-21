"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # best is to maintain a map where the key is the ord-representation of the letters

        def create_representation(s):
            rep = [0]*26
            list_s = list(s)
            for letter in list_s:
                pos = ord(letter.upper()) - ord('A')
                rep[pos] += 1
            str_rep = (",").join(map(str, rep))
            return str_rep

        seen = {}

        for string in strs:
            rep = create_representation(string)
            if rep in seen.keys():
                seen[rep].append(string)
            else:
                seen[rep] = [string]
        
        return list(seen.values())
