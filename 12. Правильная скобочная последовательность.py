def iscorrect(brackets):
    stack = []
    for i in range(len(brackets)):
        if len(stack) == 0 and (brackets[i] == ']' or brackets[i] == ')' or brackets[i] == '}'):
            return 'no'
        else:
            if len(stack) == 0 or brackets[i] == '[' or brackets[i] == '{' or brackets[i] == '(':
                stack.append(brackets[i])
            else:
                if brackets[i] == ']' and stack[-1] == '[':
                    stack.pop()
                elif brackets[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif brackets[i] == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return 'no'
    if len(stack) == 0:
         return('yes')
    else:
        return 'no'


brackets = input()
ans = iscorrect(brackets)
print(ans)



