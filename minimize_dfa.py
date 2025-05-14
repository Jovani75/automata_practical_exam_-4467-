def minimize_dfa(states, alphabet, transitions, start_state, accept_states):
    partitions = [set(accept_states), set(states) - set(accept_states)]
    changed = True
    while changed:
        changed = False
        new_partitions = []
        for group in partitions:
            splitter = {}
            for state in group:
                key = tuple([next((i for i, g in enumerate(partitions) if transitions[state][a] in g), -1) for a in alphabet])
                splitter.setdefault(key, set()).add(state)
            if len(splitter) > 1:
                changed = True
                new_partitions.extend(splitter.values())
            else:
                new_partitions.append(group)
        partitions = new_partitions
    return partitions

states = ['A', 'B', 'C', 'D']
alphabet = ['0', '1']
transitions = {
    'A': {'0': 'B', '1': 'C'},
    'B': {'0': 'A', '1': 'D'},
    'C': {'0': 'D', '1': 'A'},
    'D': {'0': 'C', '1': 'B'}
}
start_state = 'A'
accept_states = ['A']

result = minimize_dfa(states, alphabet, transitions, start_state, accept_states)
print(result)
