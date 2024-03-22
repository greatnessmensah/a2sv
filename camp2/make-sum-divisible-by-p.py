class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        count = 0
        rem = sum(nums)%p
        
        if not rem:
            return rem
        
        mini = float("inf")
        hashmap = defaultdict(int)
        hashmap[0] = -1
       
        for i in range(len(nums)):
            count += nums[i]
            ans = count % p
            if (ans-rem)%p in hashmap:
                mini = min(mini, i-hashmap[(ans-rem)%p])
            hashmap[ans] = i
            
        return mini if mini < len(nums) else -1
           
