from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment=assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment=assignment):
            if self.is_consistent(variable=var, value=value, assignment=assignment):
                assignment[var] = value
                res = self.recursive_backtracking(assignment=assignment)
                if res is not None:
                    return res
                assignment[var] = None
        return None

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_australia_csp():
   
    cr, pa, ve, gu, su, gufr, br, ur, ar, ch, bo, par, pe, ec, co = 'CR', 'PA', 'VE', 'GU', 'SU', 'GUFR', 'BR', 'UR', 'AR', 'CH', 'BO', 'PAR', 'PE', 'EC', 'CO'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [cr, pa, ve, gu, su, gufr,
                 br, ur, ar, ch, bo, par, pe, ec, co]
    domains = {
        cr: values[:],
        pa: values[:],
        ve: values[:],
        gu: values[:],
        su: values[:],
        gufr: values[:],
        br: values[:],
        ur: values[:],
        ar: values[:],
        ch: values[:],
        bo: values[:],
        par: values[:],
        pe: values[:],
        ec: values[:],
        co: values[:]
    }
    neighbours = {
        cr: [pa],
        pa: [cr, co],
        co: [pa, ve, ec, pe],
        ve: [co, br, gu],
        gu: [ve, su, br],
        su: [gu, gufr, br],
        gufr: [su, br],
        br: [co, ve, gu, su, gufr, pa, ur, ar, bo, pe],
        ur: [br, ar],
        ar: [ur, br, pa, bo, ch],
        par: [ar, br, bo],
        ch: [ar, bo],
        bo: [ar, br, pa, pe, ch],
        pe: [bo, br, ec, co],
        ec: [pe, co],
    }
    """  
   wa, q, t, v, sa, nt, nsw = 'WA', 'Q', 'T', 'V', 'SA', 'NT', 'NSW'
    values = ['Red', 'Green', 'Blue']
    variables = [wa, q, t, v, sa, nt, nsw]
    domains = {
        wa: values[:],
        q: values[:],
        t: values[:],
        v: values[:],
        sa: values[:],
        nt: values[:],
        nsw: values[:],
    }
    neighbours = {
        wa: [sa, nt],
        q: [sa, nt, nsw],
        t: [],
        v: [sa, nsw],
        sa: [wa, nt, q, nsw, v],
        nt: [sa, wa, q],
        nsw: [sa, q, v],
    } """

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    """ constraints = {
        wa: constraint_function,
        q: constraint_function,
        t: constraint_function,
        v: constraint_function,
        sa: constraint_function,
        nt: constraint_function,
        nsw: constraint_function,
    } """

    constraints = {
        cr: constraint_function,
        pa: constraint_function,
        ve: constraint_function,
        gu: constraint_function,
        su: constraint_function,
        gufr: constraint_function,
        br: constraint_function,
        ur: constraint_function,
        ar: constraint_function,
        ch: constraint_function,
        bo: constraint_function,
        par: constraint_function,
        pe: constraint_function,
        ec: constraint_function,
        co: constraint_function
    }
    return CSP(variables, domains, neighbours, constraints)
    


if __name__ == '__main__':
    australia = create_australia_csp()
    result = australia.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html