#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize dict
        hashmap = {}

        # get one string
        for str in strs:
            # Remove whitespace
            str.strip

            # Turn string into list of sorted characters
            chars = sorted(str)

            # Reform sorted characters into string
            sorted_str = "".join(chars)

            # Put it in the dictionary with oringal string if not already a key
            if sorted_str not in hashmap:
                hashmap[sorted_str] = [str]
            else:
                hashmap[sorted_str].append(str)

        # Return as a list of lists of pairs
        return list(hashmap.values())

        
# @lc code=end

