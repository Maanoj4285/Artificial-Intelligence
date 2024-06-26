class CSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables  # List of variables to be colored
        self.domains = domains  # Domains of each variable
        self.neighbors = neighbors  # Neighbors of each variable
        self.constraints = constraints  # Constraints between variables
        self.assignment = {}  # Current assignment of colors

    def is_consistent(self, var, value):
        for neighbor in self.neighbors[var]:
            if neighbor in self.assignment and not self.constraints(var, value, neighbor, self.assignment[neighbor]):
                return False
        return True

    def assign(self, var, value):
        self.assignment[var] = value

    def unassign(self, var):
        if var in self.assignment:
            del self.assignment[var]

    def select_unassigned_variable(self):
        # Selects the next unassigned variable
        for var in self.variables:
            if var not in self.assignment:
                return var
        return None

    def order_domain_values(self, var):
        # Returns the domain values for the variable in an ordered manner
        return self.domains[var]

    def backtrack(self):
        if len(self.assignment) == len(self.variables):
            return self.assignment

        var = self.select_unassigned_variable()
        for value in self.order_domain_values(var):
            if self.is_consistent(var, value):
                self.assign(var, value)
                result = self.backtrack()
                if result:
                    return result
                self.unassign(var)
        
        return None

def map_coloring_csp():
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {var: ['Red', 'Green', 'Blue'] for var in variables}
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    def constraints(A, a, B, b):
        return a != b  # Adjacent regions must have different colors

    csp = CSP(variables, domains, neighbors, constraints)
    solution = csp.backtrack()
    return solution

if __name__ == "__main__":
    solution = map_coloring_csp()
    print("Solution:", solution)
