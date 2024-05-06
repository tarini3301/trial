def evaluate_postfix(postfix_expression):
    operand_stack = []
    for char in postfix_expression:
        if char.isdigit():
            operand_stack.append(char)
        elif char.isalpha():
            variable_value = int(input('enter predefined value for variables'))
            operand_stack.append(str(variable_value))
        elif char in {'+', '-', '*', '/'}:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            expression = f'({operand1} {char} {operand2})'
            result = eval(expression)
            operand_stack.append(str(result))
    return operand_stack[0]
def postfix_to_infix(postfix_expression):
    operand_stack = []
    for char in postfix_expression:
        if char.isdigit() or char.isalpha():
            operand_stack.append(char)
        elif char in {'+', '-', '*', '/'}:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            expression = f'({operand1} {char} {operand2})'
            operand_stack.append(expression)
    return operand_stack[0]
postfix_expression = input('Enter postfix expression: ')
infix_expression = postfix_to_infix(postfix_expression)
print("Infix expression:", infix_expression)
result_value = evaluate_postfix(postfix_expression)
print("Result:", result_value)
