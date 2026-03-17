import sys

# --------------------------
# Tokenizer
# --------------------------
def tokenize(code):
    code = code.replace("(", " ( ").replace(")", " ) ")
    return code.split()

# --------------------------
# Parser
# --------------------------
def parse(tokens):
    if len(tokens) == 0:
        raise SyntaxError("Unexpected EOF")

    token = tokens.pop(0)
    if token == "(":
        expr = []
        while tokens[0] != ")":
            expr.append(parse(tokens))
        tokens.pop(0)  # remove ')'
        return expr

    elif token == ")":
        raise SyntaxError("Unexpected )")

    else:
        return atom(token)

def atom(token):
    try:
        return int(token)
    except ValueError:
        return token

# --------------------------
# Evaluator
# --------------------------
def evaluate(expr):
    if isinstance(expr, int):
        return expr

    operator = expr[0]
    left = evaluate(expr[1])
    right = evaluate(expr[2])

    if operator == "+":
        return left + right
    elif operator == "-":
        return left - right
    elif operator == "*":
        return left * right
    elif operator == "/":
        return left / right
    else:
        pass

# --------------------------
# Main
# --------------------------
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 parser.py test.lisp")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename) as f:
        code = f.read()

    tokens = tokenize(code)
    parsed = parse(tokens)
    result = evaluate(parsed)

    print("Result:", result)


# nano parser.py
# python3 parser.py test.lisp
# test.lisp --> eg (+3(*24)) 
