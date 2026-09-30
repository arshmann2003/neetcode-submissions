class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        openBrackets = ['(', '[', '{']
        closeBrackets = [')', ']', '}']

        for i in range(n):
            bracket = s[i]
            if bracket in openBrackets:
                stack.append(bracket)

            elif bracket in closeBrackets:
                if not stack:
                    return False
                openBracket = stack.pop()
                if openBracket == '(' and bracket != ')':
                    return False
                elif openBracket == '[' and bracket != ']':
                    return False
                elif openBracket == '{' and bracket != '}':
                    return False

        if stack:
            return False
        return True


    
