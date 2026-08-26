class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        newString = ""
        operators = ["+", "-", "/", "*"]
        for item in tokens:
            if item not in operators:
                stack.append(int(item))
            else:
                b= stack.pop()
                a = stack.pop()

                if item == "+":
                    stack.append(a + b)
                elif item == "-":
                    stack.append(a - b)
                elif item == "*":
                    stack.append(a * b)
                elif item == "/":
                    stack.append(int(a/b))
        return stack[0]
            