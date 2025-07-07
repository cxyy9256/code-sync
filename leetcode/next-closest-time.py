class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = list(time.replace(":", ""))
        curr_time = int(time[:2]) * 60 + int(time[3:])
        
        min_diff = 24*60
        
        result = time
        
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        h1, h2, m1, m2 = nums[i], nums[j], nums[k], nums[l]
                        hours = int(h1+h2)
                        mins = int(m1+m2)
                        if hours < 24 and mins < 60:
                            total_min = hours*60 + mins
                            diff = (total_min - curr_time) % (24*60)
                            if 0 < diff < min_diff:
                                min_diff = diff
                                result = "{}{}:{}{}".format(h1, h2, m1, m2)
                                    
        return result