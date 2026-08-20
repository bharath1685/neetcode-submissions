class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        ans = []
        n = len(nums)
        for num in nums:
            freq[num] = freq.get(num,0) +1 
        for key,val in freq.items():
            if val > n//3:
                ans.append(key)
        return ans
