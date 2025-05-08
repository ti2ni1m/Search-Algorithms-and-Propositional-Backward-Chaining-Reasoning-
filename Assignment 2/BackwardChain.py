class BCR :
    #Initiialises the class with an empty set of rules and facts
    def __init__(self) :
        self.rules = [] #Stores the list of rules
        self.facts = set() #Stores known facts

    #Adds a rule or fact to the knowledge base 
    def add(self, rule) :
        if '=>' in rule: #If the rule contains the implies symbol, it means its a rule
            body, head = rule.split('=>') #Split rule into body and head
            head = head.strip() #Removes extra spaces around the head
            if '^' in body : #If the body has "AND" also known as Conjunction
                conditions = [cond.strip() for cond in body.split('^')] #Split premises by '^'
                self.rules.append(('AND', conditions, head)) #Stores the rule as an AND type
            elif 'v' in body : #If the body has "OR" also known as Disjunction
                conditions = [cond.strip() for cond in body.split('v')] #Split premises by 'v'
                self.rules.append(('OR', conditions, head)) #Stores the rule as an OR type
        else :
            #A fact, directly add it to the set of facts
            fact = rule.strip() #Removes any extra spaces
            self.facts.add(fact) #Add the fact to known fact
    
    #Start the backward chaining inference process for the given query
    def inference(self, query) : 
        return self.dfs(query, set()) #Calls the depth-first search with an empty visited set
    
    #Perform a depth-first search to check if the query can be inferred from the facts/rules
    def dfs(self, query, visited) :
        if query in self.facts :
            return True #If the query is already a known fact where it returns True
        
        if query in visited :
            return False #If the query was visited, return False
        visited.add(query) #Mark the query as visited

        #Iterate over all rules to try to infer the query from the rules
        for rule, conditions, conclusion in self.rules :
            if conclusion == query : #Check if the rule concludes the query
                #If it's an AND rule, all conditions must be true
                if rule == 'AND' :
                    if all(self.dfs(cond, visited) for cond in conditions) :
                        self.facts.add(conclusion) #If true, add the conclusion to known facts
                        return True
                #If it's an OR rule, at least one condition must be true
                elif rule == 'OR' :
                    if any(self.dfs(cond, visited) for cond in conditions) :
                        self.facts.add(conclusion) #If true, add the conclusion to known facts
                        return True
                    
        return False #If none of the rules can infer the query, return False
    

#Main function to handle user inputs and reasoning process
def main() :
    print("reasoning>> This is an extended propositional backward chaining reasoning system.")
    print("reasoning>> Knowledge base can only accept these facts like: ")
    print("reasoning>> P1^P2^...^Pk => P, or ")
    print("reasoning>> P1vP2v...vPk => P, or ")
    print("reasoning>> P.")
    reason = BCR() #Create an instance of the BCR class

    while True :
        #Keep accepting rules from the user until 'nil' is inputted
        rule = input("reasoning>> ")
        if rule == "nil" :
            break #Stops the input if the 'nil' is inputted 
        reason.add(rule) #Adds the rules to the knowledge base

    print("reasoning>> Finished inputing, now testing system...")

    while True :
        #Keep accepting queries until 'quit' is inputted
        query = input("reasoning>> ")
        if query == "quit" :
            break #Stops the input if the 'quit' is inputted
        if query.endswith('?') :
            query = query[:-1].strip() #Removes the question mark from the end of the query
            if reason.inference(query) :
                print("reasoning>> yes") #If the query can be inferred, 'yes' will be outputted
            else :
                print("reasoning>> no") #If not, 'no' will be outputted

#Enrty point of the program
if __name__  == "__main__" :
    #Runs the main function
    main()