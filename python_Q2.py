def is_symbol_success(symbol):
    stack = []
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for char in symbol:
        if char in matching_brackets.values():
            stack.append(char)
        elif char in matching_brackets.keys():
            if not stack or stack.pop() != matching_brackets[char]:
                return "施法失敗"
    
    return "施法成功"

test_symbols = ["()", "{{}}", "({})", "({[()]})", "([)]", "(([)]", "{[]}", "({})"]

for symbol in test_symbols:
    result = is_symbol_success(symbol)
    print(f"{symbol}: {result}")