#Implication (C ⇒ D) as a separate function
def imply(p, q) :
    return not p or q

#Define a function to evaluate a propositional formula given a truth assignment
def evaluate(formula, assignment) :
    #Only the local assignment dictionary is allowed, no global variables or built-ins
    return eval(formula, {"implies": imply}, assignment)

#A Recursive function to generate all possible truth assignments for a set of variables
def truth(variables, current = None, index = 0) :
    if current is None :
        current = {}

    if index == len(variables) :
        return[current.copy()]
    
    var = variables[index]
    current[var] = True
    true = truth(variables, current, index + 1)

    current[var] = False
    false = truth(variables, current, index + 1)

    return true + false

#A function to check if a set of sentences is satisfied by a given assignment
def check(sentences, assignment) :
    return all(evaluate(sentence, assignment) for sentence in sentences)

#Function to generate models for a given set of sentences and variables
def model(sentences, variables) :
    truthassignment = truth(variables)
    models = []
    
    for assignment in truthassignment :
        if check(sentences, assignment) :
            models.append(assignment)
    
    return models

#Pretty-print the models without negations
def printmodel(models) :
    for model in models :
        vars = [var for var, value in model.items() if value]
        print(vars)

#Define the sets of sentences (in string form) and variables
S1 = ['A or B', 'A and C', 'implies(C, D)']  # C ⇒ D represented by implies(C, D)
S2 = ['A or not B', 'C or D']

# Variables for S1 and S2
varS1 = ['A', 'B', 'C', 'D']
varS2 = ['A', 'B', 'C', 'D']

#Choice made by users on which set the input should run in, either be 1 for S1 oe 2 for S2
choice = input("Enter 1 for S1 or 2 for S2: ")

if choice == "1":
    modS1 = model(S1, varS1)
    print(f"\nThere are {len(modS1)} models for {S1}")
    printmodel(modS1)
elif choice == "2":
    modS2 = model(S2, varS2)
    print(f"\nThere are {len(modS2)} models for {S2}")
    printmodel(modS2)
else:
    print("Invalid choice!")
