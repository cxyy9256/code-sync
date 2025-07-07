class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = [] # store final lines
        lines = [] # current line of words
        line_len = 0 # total line length excluding spaces

        for word in words:
            # len(lines) is the current num of required spaces
            if len(word) + len(lines) + line_len > maxWidth:
                spaces_total = maxWidth - line_len
                if len(lines) == 1:
                    result.append(lines[0]+' '* spaces_total)
                else:
                    spaces = [' '* (spaces_total// (len(lines) - 1))] * (len(lines) -1)
                    # extra spaces going left most
                    for i in range (spaces_total % (len(lines) - 1)):
                        spaces[i] += ' '
                    justify_line = ''.join(word + space for word, space in zip(lines, spaces + ['']))
                    result.append(justify_line)
                lines = []
                line_len = 0
            lines.append(word)
            line_len += len(word)
        result.append(' '.join(lines).ljust(maxWidth))
        
        return result