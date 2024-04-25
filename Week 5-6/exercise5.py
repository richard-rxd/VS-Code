from collections import deque

# Task 1

class stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
def reverse_string(inpu):
    string = stack()
    for i in inpu: 
        string.push(i)
    reverse = ""
    while string.is_empty() == False:
        reverse += string.pop()
    return reverse

text = input("Text to reverse: ")
print(f"Reversed Text: {reverse_string(text)}")

# Task 2

def is_balancedrmw(value):
    string = stack()
    for i in value:
        string.push(i)
    p1 = 0
    p2 = 0
    p3 = 0
    check = ""
    while string.is_empty() == False:
        check = string.pop()
        if check == ")":
            p1 += 1
        elif check == "]":
            p2 += 1
        elif check == "}":
            p3 += 1
        elif check == "(":
            p1 -= 1
        elif check == "[":
            p2 -= 1
        elif check == "{":
            p3 -= 1
    if p1 == 0 and p2 == 0 and p3 == 0:
        print("parantheses is balanced")
    else:
        print("parantheses is not balanced")

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0

text2 = input("Text to check: ")
is_balancedrmw(text2)