class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # for nondistict arrays, sort the array so nondistinct stuff is next to each other
        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):

                # If already used nums[i] in this current recursive path, skip it.
                if used[i]:
                    continue # skip to next i that is unique

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                    # removes [1(second copy), 1(first copy), 2] and [1(first copy), 1(second copy), 2]
                
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop() # removes last item in list 
                used[i] = False

        # used = [False, False, False]  # initially, nothing is used

        nums.sort()
        result = []
        backtrack([], [False] * len(nums))
        return result