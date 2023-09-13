class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(token))
                
        return int(stack[-1])