from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)
        result = []

        for start in range(word_len):
            left = start 
            right = start
            seen = Counter()

            while right + word_len <= len(s):
                word = s[right:right+word_len]
                right += word_len

                if word in word_freq:
                    seen[word] += 1
                # if count of current word exceeds allowed freq, shrink window by moving left pointer
                    while seen[word] > word_freq[word]:
                        left_word = s[left:left+word_len]
                        seen[left_word] -= 1
                        left += word_len
                    
                    if right - left == total_len:
                        result.append(left)
                else:
                    # if word not in word freq reset seen counter and move left ot the righ pointer to start again
                    seen.clear()
                    left = right
        return result

        '''
        old approach has time limit problems 
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)
        result = []

        for start in range(word_len):
            left = start
            right = start
            seen = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_freq:
                    seen[word] += 1
                    
                    # If word count exceeds, slide the window
                    while seen[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len

                    # Check if valid substring
                    if right - left == total_len:
                        result.append(left)
                else:
                    # Reset the window
                    seen.clear()
                    left = right

        return result
        '''