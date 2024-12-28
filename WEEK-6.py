from itertools import product

def implies(p, q):
    return not p or q

def and_op(p, q):
    return p and q

def or_op(p, q):
    return p or q

def not_op(p):
    return not p

def evaluate(expr, model):
    if isinstance(expr, str):
        return model[expr]
    elif isinstance(expr, tuple):
        operator = expr[0]
        if operator == 'NOT':
            return not_op(evaluate(expr[1], model))
        elif operator == 'AND':
            return and_op(evaluate(expr[1], model), evaluate(expr[2], model))
        elif operator == 'OR':
            return or_op(evaluate(expr[1], model), evaluate(expr[2], model))
        elif operator == 'IMPLIES':
            return implies(evaluate(expr[1], model), evaluate(expr[2], model))
    return False

def tt_entails_with_truth_table(kb, query, symbols):
    all_models = list(product([True, False], repeat=len(symbols)))
    symbols = list(symbols)
    entails = True

    print(f"{' '.join([f'{s:^5}' for s in symbols])} {'KB':^10} {'Query':^10} {'KB implies Query'}")
    print("-" * (6 * len(symbols) + 30))

    for values in all_models:
        model = dict(zip(symbols, values))

        kb_true = evaluate(kb, model)
        query_true = evaluate(query, model)

        entails_model = not kb_true or query_true

        row = ' '.join([f"{model[s]!s:^5}" for s in symbols])
        print(f"{row} {kb_true!s:^10} {query_true!s:^10} {entails_model!s:^15}")

        if kb_true and not query_true:
            entails = False

    return entails

def parse_expression(input_str):
    """Parse a user input string into a tuple-based logical expression."""
    tokens = input_str.replace('(', '').replace(')', '').split()
    if len(tokens) == 2 and tokens[0] == 'NOT':
        return ('NOT', tokens[1].strip())
    elif len(tokens) == 3:
        op = tokens[1].strip()
        left = tokens[0].strip()
        right = tokens[2].strip()
        if op == 'AND':
            return ('AND', left, right)
        elif op == 'OR':
            return ('OR', left, right)
        elif op == 'IMPLIES':
            return ('IMPLIES', left, right)
    return input_str.strip()

symbols = input("Enter the symbols separated by commas (e.g., A, B, C): ").replace(" ", "").split(",")
kb_input = input("Enter the KB expression (use AND, OR, IMPLIES, NOT): ")
query_input = input("Enter the Query expression (use AND, OR, IMPLIES, NOT): ")

kb = parse_expression(kb_input)
query = parse_expression(query_input)

result = tt_entails_with_truth_table(kb, query, symbols)

print("\nFinal result:")
print(f"Does the KB entail the query? {'Yes' if result else 'No'}")
