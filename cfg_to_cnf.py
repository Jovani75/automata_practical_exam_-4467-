def convert_to_cnf(cfg):
    variables, terminals, rules = cfg.split("#")
    variables = variables.split(",")
    terminals = terminals.split(",")
    productions = rules.split(";")
    result = []
    for prod in productions:
        lhs, rhs = prod.split("->")
        rhs_parts = rhs.split("|")
        for part in rhs_parts:
            if len(part) > 2:
                result.append(lhs + "->" + part[:2])
            else:
                result.append(lhs + "->" + part)
    return result

cfg = "S,A,B#a,b#S->AB|aA;A->a|SB;B->b"
cnf = convert_to_cnf(cfg)
print(cnf)
