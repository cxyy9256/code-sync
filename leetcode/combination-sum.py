class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combos = []

        def make_combo(idx, comb, curr_total):
            if curr_total == target:
                combos.append(comb[:]) # shallow copy
                return
            if curr_total > target or idx >= len(candidates):
                return

            comb.append(candidates[idx])
            make_combo(idx, comb, curr_total+candidates[idx])
            comb.pop()
            make_combo(idx+1, comb, curr_total)
            return combos

        return make_combo(0, [], 0)