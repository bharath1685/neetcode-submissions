class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(l, r):
            if l >= r:
                return

            m = (l + r) // 2
            mergeSort(l, m)
            mergeSort(m + 1, r)

            temp = []
            i, j = l, m + 1

            while i <= m and j <= r:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= m:
                temp.append(nums[i])
                i += 1

            while j <= r:
                temp.append(nums[j])
                j += 1

            nums[l:r + 1] = temp

        mergeSort(0, len(nums) - 1)
        return nums