class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        global_idx = 0 # first index of the current group you are on 
        res = 0 # current length of compressed string

        while global_idx < len(chars):
            group_len = 1
            while (global_idx + group_len < len(chars) and chars[global_idx + group_len] == chars[global_idx]):
                group_len += 1
            
            # overwrite the existing cells with the char, this is if group length is 1
            chars[res] = chars[global_idx]
            res += 1 # add one for the first char 

            # add in the group length after the char
            if group_len > 1:
                total_str = str(group_len)
                chars[res: res + len(total_str)] = list(total_str)
                res += len(total_str)
            global_idx += group_len
        return res