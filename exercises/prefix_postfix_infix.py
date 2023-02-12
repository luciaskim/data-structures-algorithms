
def infix_to_postfix(input_string):
    precedence = {"+": 0, "-": 0, "*": 1, "/": 1, "^":2}
    stack = Stack()
    output = ""
    for char in input_string:
        if char.isdigit():
            output += char
        elif char == "(" or stack.is_empty():
            stack.push(char)
        elif char == ")":
            while not stack.is_empty() and stack.peek() != "(":
                # Check empty first to terminate early
                output += stack.pop()
            if stack.is_empty():
                return "Incorrect brackets"
            else:
                stack.pop()
        else:
            while not stack.is_empty() and stack.peek() != "(" and precedence[char] <= precedence[stack.peek()]: 
                # Operatoers of equal or higher precedence are added to output
                output += stack.pop()
            stack.push(char)
    while not stack.is_empty():
        output += stack.pop()
    return output

def infix_to_prefix(string):
    precedence = {"+": 0, "-": 0, "*": 1, "/": 1, "^":2}
    stack = Stack()
    output = ""
    for char in string[::-1]: # Reverse string
        if char.isdigit():
            output = char + output # Update output so that char is at front
        elif char == ")" or stack.is_empty(): # ) becomes opening bracket
            stack.push(char)
        elif char == "(": # ( becomes closing bracket
            while not stack.is_empty() and stack.peek() != ")": 
                output = stack.pop() + output
            if stack.is_empty():
                return "Incorrect brackets"
            else:
                stack.pop()
        else:
            while not stack.is_empty() and stack.peek() != ")" and precedence[stack.peek()] >= precedence[char]: # Check empty first to terminate early
                output = stack.pop() + output  # Update output so that char is at front
            stack.push(char)
    while not stack.is_empty():
        output = stack.pop() + output  # Update output so that char is at front
    return output



def evaluate_prefix(string):
    stack = Stack()
    for char in string:
        if char.isdigit():
            stack.push(char)
        else:
            arg1 = stack.pop()
            arg2 = stack.pop()
            stack.push(str(eval(arg2 + char + arg1))) # Reverse order of arguments
    return stack.pop()

def evaluate_prefix(string):
    stack = Stack()
    for char in string[::-1]: # Reverse string
        if char.isdigit():
            stack.push(char)
        else:
            arg1 = stack.pop()
            arg2 = stack.pop()
            stack.push(str(eval(arg1 + char + arg2)))
    return stack.pop()

print(infix_to_prefix("(A+B)*(C-D)"))
print(evaluate_prefix("(A+B)*(C-D)"))