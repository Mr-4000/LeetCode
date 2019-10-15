class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        a = 0
        b = 0
        if (len(tokens) == 1):
            return (int(tokens[0]))
        for i in tokens:
            if i not in ["+","-","*","/"]:
                stack.append(i)
            if (i == "+"):
                a = int(stack.pop())
                b = int(stack.pop())
                print(a,b,i)
                ans = a + b
                stack.append(str(ans))
            if (i == "-"):
                a = int(stack.pop())
                b = int(stack.pop())
                print(a,b,i)
                ans = b - a
                stack.append(str(ans))
            if (i == "*"):
                a = int(stack.pop())
                b = int(stack.pop())
                print(a,b,i)
                ans = a * b
                stack.append(str(ans))
            if (i == "/"):
                a = int(stack.pop())
                b = int(stack.pop())
                print(a,b,i)
                ans = int(b / a)
                stack.append(str(ans))
        return(ans)
#Runtime: 88 ms, faster than 25.72% of Python3 online submissions for Evaluate Reverse Polish Notation.
#Memory Usage: 14.7 MB, less than 8.70% of Python3 online submissions for Evaluate Reverse Polish Notation.