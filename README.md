section 3

Cs

انا حليت ال4 تاسكات افضل اني اتسال في pda_simulation
و tm_increment

اشنغلته بالبايثون 
unit test:
def test_minimize_dfa():
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
    expected = [set(['A']), set(['B', 'C', 'D'])]
    assert all(any(group == exp for group in result) for exp in expected), "DFA minimization test failed"

test_minimize_dfa()
print("DFA minimization test passed!")
----------------------------------
def test_convert_to_cnf():
    cfg = "S,A,B#a,b#S->AB|aA;A->a|SB;B->b"
    result = convert_to_cnf(cfg)
    expected_subsets = [
        "S->AB", "S->aA",
        "A->a", "A->SB",
        "B->b"
    ]
    for exp in expected_subsets:
        assert any(r.startswith(exp[:4]) for r in result), f"Missing {exp} in CNF conversion"
    print("CFG to CNF test passed!")

test_convert_to_cnf()
------------------------------------------------
def test_pda_simulate():
    cfg = ["S->aSb", "S->"]
    pda = PDA(cfg)
    assert pda.simulate("aaabbb") == True, "PDA should accept 'aaabbb'"
    assert pda.simulate("aab") == False, "PDA should reject 'aab'"
    print("PDA simulation test passed!")

test_pda_simulate()
-----------------------------------------
def test_increment_binary():
    assert increment_binary("1011") == "1100", "Increment failed for '1011'"
    assert increment_binary("111") == "1000", "Increment failed for '111'"
    assert increment_binary("0") == "1", "Increment failed for '0'"
    print("Binary increment test passed!")

test_increment_binary()
