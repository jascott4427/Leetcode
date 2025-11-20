#
# @lc app=leetcode id=587 lang=python
#
# [587] Erect the Fence
#

# @lc code=start
class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[List[int]]
        """
        hull = self.buildHull(trees)
        return hull
    
    def buildHull(self, trees):
        if len(trees) <= 1:
            return trees

        # Primarily sort by ascending y, then secondarily sort ascending x
        trees.sort(key=lambda coord: (coord[1], coord[0]))

        # Set our lowest y and left most coordinate as P
        p0 = trees[0]

        hull = []        

        for p in trees:
            while len(hull) >= 2 and self.crossProduct(hull[-2],hull[-1],p)<0:
                hull.pop()
            hull.append(p)

        for p in reversed(trees):
            while len(hull) >= 2 and self.crossProduct(hull[-2],hull[-1],p)<0:
                hull.pop()
            hull.append(p)

        result = []
        seen = set()
        for point in hull:
            tuple_point = tuple(point)
            if tuple_point not in seen:
                seen.add(tuple_point)
                result.append(point)
        
        return result

    def crossProduct(self, o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
# @lc code=end

