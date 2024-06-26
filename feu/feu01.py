import sys

def parse_args():
    argc = len(sys.argv)
    if argc < 2:
        print("error")
        exit(1)

    expression = sys.argv[1]
    return expression

def shunting_yard(expression: str):
    priority = { '+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
    operators = list()
    output = list()

    i=0
    while i < len(expression):
        if expression[i].isdigit():
            num = expression[i]
            while (i + 1) < len(expression) and expression[i + 1].isdigit():
                i += 1
                num += expression[i]
            output.append(num)
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
        elif expression[i] in priority:
            while(operators and operators[-1] in priority and priority[expression[i]] <= priority[operators[-1]]):
                output.append(operators.pop())
            operators.append(expression[i])
        i += 1

    while operators:
        output.append(operators.pop())
    return ' '.join(output)


def parse_arithmetic(expression):
    result = list()
    postfix = shunting_yard(expression).split()

    for c in postfix:
        if c.isdigit():
            result.append(int(c))
        else:
            right_op = result.pop()
            left_op = result.pop()

            match c:
                case '+':
                    result.append(left_op + right_op)
                case '-':
                    result.append(left_op - right_op)
                case '*':
                    result.append(left_op * right_op)
                case '/':
                    result.append(left_op / right_op)
                case '%':
                    result.append(left_op % right_op)
    return result[0]
expression = parse_args()
print(parse_arithmetic(expression))
