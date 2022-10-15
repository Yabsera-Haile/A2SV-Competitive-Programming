import operator
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': lambda num1, num2: num1//num2 if num1*num2 > 0 else (num1+(-num1 % num2))//num2,
}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                num1 = int(Stack.pop(-2))
                num2 = int(Stack.pop(-1))
                Stack.append(ops[token](num1, num2))
            else:
                Stack.append(token)
        return Stack[0]
