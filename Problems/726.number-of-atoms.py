#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#

# @lc code=start
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        my_dict = self.convertFormulaToDictionary(formula)
        # print(my_dict)
        sorted_pairs = sorted(my_dict.items())
        # print(sorted_pairs)
        sorted_elements = self.convertPairsToString(sorted_pairs)
        # print(sorted_elements)
        return sorted_elements
    
    def convertFormulaToDictionary(self, formula):
        my_dict = {}
        n = len(formula) - 1
        # print(n)
        multiplier = [1]
        current_element = ""
        current_num = ""
        int_num = 1
        while n >= 0:
            char = formula[n]
            n -= 1

            if char == ")":
                num = multiplier[-1] * int_num
                multiplier.append(num)
                int_num = 1
            elif char == "(":
                if len(multiplier) <= 1:
                    multiplier = [1]
                else:
                    multiplier.pop()
            elif char.islower():
                temp = char + current_element
                current_element = temp 
            elif char.isupper():
                temp = char + current_element
                current_element = temp
                num = multiplier[-1] * int_num
                self.addAtomsToDict(my_dict, current_element, num)
                current_element = ""
                int_num = 1

            elif char.isdigit():
                current_num = char + current_num
                if formula[n].isdigit():
                    continue
                else:
                    int_num = int(current_num)
                    current_num = ""

        return my_dict

    def addAtomsToDict(self, dictionary, key, num):
        if key not in dictionary:
            dictionary[key] = num
        else:
            dictionary[key] += num
    
    def convertPairsToString(self, sorted_pairs):
        string = ""
        for pair in sorted_pairs:
            str_element = pair[0]
            # print(str_element)
            num = pair[1]
            str_num = str(num) if num != 1 else ""
            # print(num)
            string = string + str_element + str_num
            # print(string)

        return string
    

        
# @lc code=end

