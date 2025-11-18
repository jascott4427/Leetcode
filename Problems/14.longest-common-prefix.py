#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []: return ""
        for word in strs:
            if word == "": return ""
        sortedList = sorted(strs, key=len)
        shortestWord = sortedList[0]
        maxLength = len(shortestWord)
        prefix = ""
        currentLetter = ""
        end = False
        for i in range(maxLength):
            for word in strs:
                print(word)
                firstLetter = word[i]
                print(firstLetter)
                if not currentLetter:
                    currentLetter = firstLetter
                    print(currentLetter)
                elif firstLetter != currentLetter:
                    print("lets end")
                    end = True
                    break
            print("Reached end of for loop")
            if end == True: return prefix
            elif i == maxLength - 1:
                prefix += currentLetter
                return prefix
            else:
                prefix += currentLetter
                currentLetter = ""

# @lc code=end

