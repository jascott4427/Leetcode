#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def willIntersect(target, posLead, posTrail, velLead, velTrail):
            if velLead >= velTrail:
                return False
            
            if velLead == 0:
                tLead = 100000000
            else:
                tLead = (target - posLead) / velLead

            if velTrail == 0:
                tTrail = 100000000
            else:
                tTrail = (target - posTrail) / velTrail           

            if tLead < tTrail:
                return False
            else:
                return True
        
        combined = zip(position, speed)
        sorted_combined = sorted(combined, reverse=True)
        # print(sorted_combined)

        numFleets = 0
        lastFleetPos = 0
        lastFleetSpeed = 0
        for p, s in sorted_combined:
            if numFleets == 0:
                lastFleetPos = p
                lastFleetSpeed = s
                numFleets += 1
            elif not willIntersect(target, lastFleetPos, p, lastFleetSpeed, s):
                numFleets += 1
                lastFleetPos = p
                lastFleetSpeed = s
        return numFleets

# @lc code=end

