class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # sum of cost should not be more than gas

        if sum(cost) > sum(gas):
            return -1

        total = 0   # 
        res = 0   # 

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0: # current starting point can't work
                total = 0 # reset and try again
                res = i + 1 # set next station as new start
            
        return res