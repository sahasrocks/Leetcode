class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost): return -1
        tank = [0] * len(gas)  
        for i in range(1, len(gas)): tank[i] = tank[i - 1] + gas[i - 1] - cost[i - 1]
        return tank.index(min(tank))  
        