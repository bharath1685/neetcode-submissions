class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        ans = []
        n = len(nums)
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for key,val in freq.items():
            if val > n//3:
                ans.append(key)
        return ans
