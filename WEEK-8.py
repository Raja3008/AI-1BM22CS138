class UnificationError(Exception):
    pass

def unify(expr1, expr2, substitutions=None):
    if substitutions is None:
        substitutions = {}

    if expr1 == expr2:
        return substitutions

    if is_variable(expr1):
        return unify_variable(expr1, expr2, substitutions)

    if is_variable(expr2):
        return unify_variable(expr2, expr1, substitutions)

    if is_compound(expr1) and is_compound(expr2):
        if expr1[0] != expr2[0] or len(expr1[1:]) != len(expr2[1:]):
            raise UnificationError("Expressions do not match.")
        for arg1, arg2 in zip(expr1[1:], expr2[1:]):
            substitutions = unify(arg1, arg2, substitutions)
        return substitutions

    raise UnificationError("Cannot unify expr1 and expr2.")

def unify_variable(var, expr, substitutions):
    if var in substitutions:
        return unify(substitutions[var], expr, substitutions)

    if occurs_check(var, expr, substitutions):
        raise UnificationError("Occurs check failed.")

    substitutions[var] = expr
    return substitutions

def occurs_check(var, expr, substitutions):
    if var == expr:
        return True

    if is_compound(expr):
        for sub in expr[1:]:
            if occurs_check(var, sub, substitutions):
                return True

    if expr in substitutions:
        return occurs_check(var, substitutions[expr], substitutions)

    return False

def is_variable(expr):
    return isinstance(expr, str) and expr.islower()

def is_compound(expr):
    return isinstance(expr, list) and len(expr) > 0

try:
    expr1 = ['f', 'x', 'y']
    expr2 = ['f', 'a', 'b']
    substitutions = unify(expr1, expr2)
    print("Substitutions:", substitutions)
except UnificationError as e:
    print("Unification failed:", e)
