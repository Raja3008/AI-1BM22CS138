class FirstOrderLogicKB:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, premise, conclusion):
        self.rules.append((premise, conclusion))

    def forward_reasoning(self):
        new_facts = set(self.facts)
        inferred = True

        while inferred:
            inferred = False
            for premise, conclusion in self.rules:
                if premise.issubset(new_facts) and conclusion not in new_facts:
                    new_facts.add(conclusion)
                    inferred = True
        self.facts = new_facts

    def query(self, fact):
        return fact in self.facts

    def display_facts(self):
        print("Known Facts:")
        for fact in self.facts:
            print(fact)

def input_facts_and_rules():
    kb = FirstOrderLogicKB()

    kb.add_fact("American(Robert)")
    kb.add_fact("Enemy(A, America)")
    kb.add_fact("Owns(A, T1)")
    kb.add_fact("Missile(T1)")
    kb.add_fact("SellsWeapon(Robert, T1)")

    rule_premise = {"American(Robert)", "SellsWeapon(Robert, T1)", "Enemy(A, America)"}
    rule_conclusion = "Criminal(Robert)"
    kb.add_rule(rule_premise, rule_conclusion)

    kb.forward_reasoning()

    return kb

def main():
    kb = input_facts_and_rules()

    kb.display_facts()


    if kb.query("Criminal(Robert)"):
        print("\nYes, Robert is a criminal.")
    else:
        print("\nNo, Robert is not a criminal.")

if __name__ == "__main__":
    main()
