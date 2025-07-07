class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in "+-*/":
                # e1 = later element (denominator in div)
                # e2 = earlier element (numerator in div)
                e1 = stack.pop()
                e2 = stack.pop()
                if token == "+":
                    stack.append(e1+e2)
                elif token == "-":
                    stack.append(e2-e1)
                elif token == "*":
                    stack.append(e1*e2)
                elif token == "/":
                    stack.append(int(e2/e1))
            else:
                stack.append(int(token))
        return stack[0]