# Data Structure HW_1
# use python3.6
# Edit by 劉岳樺_B10330010
# Expression Converter
infix = []
post_result = []
top = -1
MAX = 50
stack = [] * MAX
post_answer = ""
pre_answer = ""


def push(st, val):
    global top
    if top == MAX-1:
        print('Stack Overflow!!!!')
    else:
        top += 1
        print('do PUSH~')
        st.insert(top, val)


def pop(st):
    global top
    if top == -1:
        print('Stack Underflow!!')
        return -1
    else:
        k = st[top]
        top -= 1
        print('do POP~')
        return k


def infix_to_postfix(content):
    # converting start here
    push(stack, '(')
    content += ')'
    for i in content:
        print("Now scan to:", i)
        if i == ')':
            while not(stack[top] == '('):
                print("Meet ')' ")
                post_result.append(pop(stack))
                print("Stack:", stack)
                print("postfix:", post_result, "\n")
            if stack[top] == '(':
                pop(stack)
        elif not ((i == '(')or(i == '+')or(i == '-')or(i == '*')or(i == '/')or(i == '%')):
            post_result.append(i)
            print("Stack:", stack)
            print("postfix:", post_result, "\n")

        else:
            if i == '(':
                push(stack, i)
                print("Stack:", stack)
                print("postfix:", post_result, "\n")
            # 處理 * 部分:
            elif i == '*':
                if stack[top] == '*':
                    post_result.append(pop(stack))
                    push(stack, i)
                    print("Stack:", stack)
                    print("postfix:", post_result, "\n")

                elif (stack[top] == '/') or (stack[top] == '%'):
                    push(stack, i)
                    print("Stack:", stack)
                    print("postfix:", post_result, "\n")

                elif (stack[top] == '(') or (stack[top] == '+') or (stack[top] == '-'):
                    push(stack, i)
                    print("Stack:", stack)
                    print("postfix:", post_result, "\n")

            # 處理 / 部分
            elif i == '/':
                if (stack[top] == '*') or (stack[top] == '/'):
                    post_result.append(pop(stack))
                    push(stack, i)
                    print("Stack:", stack)
                    print("postfix:", post_result, "\n")

                elif stack[top] == '%':
                    push(stack, i)
                    print("Stack:", stack)
                    print("postfix:", post_result, "\n")

                elif (stack[top] == '(') or (stack[top] == '+') or (stack[top] == '-'):
                    push(stack, i)
                    print("Stack:", stack)
                    print("postfix:", post_result, "\n")

            # 處理 % 部分
            elif i == '%':
                if (stack[top] == '*') or (stack[top] == '/') or (stack[top] == '%'):
                    post_result.append(pop(stack))
                    push(stack, i)
                    print("Stack:", stack)
                    print("postfix:", post_result, "\n")

                elif (stack[top] == '(') or (stack[top] == '+') or (stack[top] == '-'):
                    push(stack, i)
                    print("Stack:", stack)
                    print("postfix:", post_result, "\n")

            # 處理+ -部分
            elif (i == '+') or (i == '-'):
                if (stack[top] == '*') or (stack[top] == '/') or (stack[top] == '%'):
                    post_result.append(pop(stack))
                    push(stack, i)
                    print("Stack:", stack)
                    print("postfix:", post_result, "\n")

                elif (stack[top] == '+') or (stack[top] == '-'):
                    post_result.append(pop(stack))
                    push(stack, i)
                    print("Stack:", stack)
                    print("postfix:", post_result, "\n")

                else:
                    push(stack, i)
                    print("Stack:", stack)
                    print("postfix:", post_result, "\n")
    print("========== convert end ==========", "\n\n")
    return post_result


def infix_to_prefix(content):
    rev_content = []
    pre_ans = []
    print("========== prefix convert start ==========")
    for i in content:
        if i == '(':
            i = ')'
        elif i == ')':
            i = '('
        rev_content.insert(0, i)

    ans = infix_to_postfix(rev_content)

    for i in ans:
        pre_ans.insert(0, i)
    return pre_ans


print('This is an Expression Converter\n')
infix = input('輸入一段infix計算式：')

# show the postfix result
for x in infix_to_postfix(infix):
    post_answer += x

# post_result and stack clean
# convert into prefix
post_result.clear()
stack.clear()
top = -1
for x in infix_to_prefix(infix):
    pre_answer += x

print("***************************")
print("***************************")
print("The postfix is : " + post_answer)
print("The prefix is :" + pre_answer)
print("***************************")
print("***************************")
print("\n\nPress Enter to Continue...")
input()
