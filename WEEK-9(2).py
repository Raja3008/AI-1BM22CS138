class ResolutionKB:
    def __init__(self):
        self.clauses = []

    def add_clause(self, clause):
        self.clauses.append(set(clause))

    def negate_query(self, query):
        return {"-" + literal if not literal.startswith("-") else literal[1:] for literal in query}

    def resolve(self, clause1, clause2):
        resolvent = set()
        for literal in clause1:
            if "-" + literal in clause2 or literal[1:] in clause2:
                resolvent = (clause1 | clause2) - {literal, "-" + literal}
                return resolvent
        return None

    def resolution(self, query):
        clauses = self.clauses[:]
        clauses.append(self.negate_query(query))
        while True:
            new_clauses = []
            for i, clause1 in enumerate(clauses):
                for clause2 in clauses[i + 1:]:
                    resolvent = self.resolve(clause1, clause2)
                    if resolvent is not None:
                        if not resolvent:
                            return True
                        new_clauses.append(resolvent)
            if not new_clauses:
                return False
            clauses.extend(new_clauses)

def input_clauses():
    kb = ResolutionKB()
    kb.add_clause(["American(Robert)"])
    kb.add_clause(["-American(Robert)", "-SellsWeapon(Robert, T1)", "-Enemy(A, America)", "Criminal(Robert)"])
    kb.add_clause(["SellsWeapon(Robert, T1)"])
    kb.add_clause(["Enemy(A, America)"])
    kb.add_clause(["Missile(T1)"])
    return kb

def main_resolution():
    kb = input_clauses()
    query = {"Criminal(Robert)"}
    if kb.resolution(query):
        print("\nYes, Robert is a criminal.")
    else:
        print("\nNo, Robert is not a criminal.")

if __name__ == "__main__":
    main_resolution()
