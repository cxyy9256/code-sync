class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        
        # return a list in the format []
        def counter(word):
            groups = []
            i = 0
            while i < len(word):
                char = word[i]
                count = 1
                # chain of letters of the sam e
                while i + 1 < len(word) and word[i+1] == char:
                    i += 1
                    count += 1
                groups.append((char, count))
                i += 1
            return groups
        
        s_groups = counter(s)
        stretch_count = 0
        for word in words:
            w_groups = counter(word)
            if len(s_groups) != len(w_groups):
                continue
            valid = True
            for (sc, scount), (wc, wcount) in zip(s_groups, w_groups):
                if sc != wc:
                    valid = False
                    break
                if scount < 3 and scount != wcount:
                    valid = False
                    break
                    
                '''
                case where u have more char in already in the word can't unstretch
                s = "heeellooo"   → groups: [('h',1), ('e',3), ('l',2), ('o',3)]
                word = "hellloooo" → groups: [('h',1), ('e',1), ('l',3), ('o',4)]
                '''
                if scount >=3 and wcount > scount:
                    valid = False
                    break
            if valid:
                stretch_count += 1
                
        return stretch_count