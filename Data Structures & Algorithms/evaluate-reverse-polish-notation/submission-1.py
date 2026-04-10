class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # add values to stack until operator encountered
        # when operator encountered pop 2 values from stack and apply operator than add res to stack
        # res is final number on the stack
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif token == "-":
               a, b = stack.pop(), stack.pop()

               stack.append(b-a)

            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            
            else:
                stack.append(int(token))
        return stack[0]


        
        