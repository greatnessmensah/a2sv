class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda cost: cost[0] - cost[1])
        costs_for_A = sum([cost[0] for cost in costs[:len(costs) // 2]])
        costs_for_B = sum([cost[1] for cost in costs[len(costs) // 2:]])
        return costs_for_A + costs_for_B
        
        
