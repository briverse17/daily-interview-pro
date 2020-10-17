# October 17, 2020
# Validate Balanced Parentheses

# Hi, here's your problem today. This problem was recently asked by Uber:
# Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced.
# Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.

# Example:
# Input: "((()))"
# Output: True

# Input: "[()]{}"
# Output: True

# Input: "({[)]"
# Output: False

pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}

def isValid(string):
    '''
    Reference: https://bradfieldcs.com/algos/stacks/balanced-parentheses/
    '''
    stack = [] #Python list as a stack. The stack only contains openings
    for c in string: #for each character in string
        if c in pairs.keys(): #if c is an opening, push (append) c to the stack
            stack.append(c)
            continue
        try:
            expected_opening = stack.pop()
        except IndexError: #there's no opening left in the stack => too many closings
            return False
        if c != pairs[expected_opening]: #mismatch
            return False
    return len(stack) == 0 #false if there're openings left in the stack

test_str = [
    "()(){(())",    #False, because '{' remained in the stack after the loop
    "",             #True
    "([{}])()",     #True
    "{[()()]}[()]", #True
    "[(])]",        #False, because of mismatch
    "[{}({})]()",   #True
    "(((([])))",    #False, because '(' remained in stack after the loop
    "((([]))))"     #False, because there's too much closings

]

for s in test_str[-1:]:
    print(isValid(s))