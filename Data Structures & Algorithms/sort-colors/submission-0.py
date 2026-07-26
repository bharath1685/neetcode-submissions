class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergesort(l,r):
            
            if l >= r:
                return
            mid = (l+r)//2
            mergesort(l,mid)
            mergesort(mid+1,r)

            temp = []
            i,j=l,mid+1

            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= r:
                temp.append(nums[j])
                j += 1
            nums[l:r+1] = temp
        mergesort(0,len(nums)-1)
            
            
 
