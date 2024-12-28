import re

def transform_to_fol(sentence):
    # Universal quantifiers: "Every X is Y" or "All X are Y"
    if re.match(r"(Every|All) (\w+) (is|are) (\w+)", sentence, re.IGNORECASE):
        subject, predicate = re.findall(r"(?:Every|All) (\w+) (?:is|are) (\w+)", sentence, re.IGNORECASE)[0]
        return f"∀x ({subject.capitalize()}(x) → {predicate.capitalize()}(x))"

    # Existential quantifiers: "There is someone who X Y"
    elif re.match(r"There is someone who (\w+) (\w+)", sentence, re.IGNORECASE):
        action, target = re.findall(r"There is someone who (\w+) (\w+)", sentence, re.IGNORECASE)[0]
        return f"∃x ({action.capitalize()}(x, {target.capitalize()}))"

    # Negations: "There is no X who is Y"
    elif re.match(r"There is no (\w+) who is (\w+)", sentence, re.IGNORECASE):
        subject, predicate = re.findall(r"There is no (\w+) who is (\w+)", sentence, re.IGNORECASE)[0]
        return f"¬∃x ({subject.capitalize()}(x) ∧ {predicate.capitalize()}(x))"

    # Simple relationships: "X loves Y"
    elif re.match(r"(\w+) (\w+) (\w+)", sentence):
        subject, action, target = re.findall(r"(\w+) (\w+) (\w+)", sentence)[0]
        return f"{action.capitalize()}({subject.capitalize()}, {target.capitalize()})"

    # Conditional statements: "If it is X, then the Y is Z"
    elif re.match(r"If it is (\w+), then the (\w+) is (\w+)", sentence, re.IGNORECASE):
        condition, subject, predicate = re.findall(r"If it is (\w+), then the (\w+) is (\w+)", sentence, re.IGNORECASE)[0]
        return f"({condition.capitalize()} → {predicate.capitalize()}({subject.capitalize()}))"

    # Complex relationships: "John and Mary are both students."
    elif re.match(r"(\w+) and (\w+) are both (\w+)", sentence, re.IGNORECASE):
        person1, person2, role = re.findall(r"(\w+) and (\w+) are both (\w+)", sentence, re.IGNORECASE)[0]
        return f"{role.capitalize()}({person1.capitalize()}) ∧ {role.capitalize()}({person2.capitalize()})"

    # Nested quantifiers: "There is a person who knows every other person."
    elif re.match(r"There is a (\w+) who (\w+) every (\w+)", sentence, re.IGNORECASE):
        subject, action, target = re.findall(r"There is a (\w+) who (\w+) every (\w+)", sentence, re.IGNORECASE)[0]
        return f"∃x ∀y (x ≠ y → {action.capitalize()}(x, y))"

    # Reflexive statements: "Nobody is taller than themselves."
    elif re.match(r"Nobody is (\w+) than themselves", sentence, re.IGNORECASE):
        predicate = re.findall(r"Nobody is (\w+) than themselves", sentence, re.IGNORECASE)[0]
        return f"∀x ¬{predicate.capitalize()}(x, x)"

    # Fallback for unsupported patterns
    return "Unable to transform sentence into FOL. Please enter a valid sentence pattern."

def main():
    print("Enter a sentence to convert into First-Order Logic (FOL).")
    print("Type 'exit' to quit.\n")

    while True:
        user_sentence = input("Enter your sentence: ").strip()

        if user_sentence.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break

        fol_representation = transform_to_fol(user_sentence)
        print(f"FOL Representation:\n{fol_representation}\n")

if __name__ == "__main__":
    main()
