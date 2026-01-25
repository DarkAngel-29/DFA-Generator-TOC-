from dfa import DFA

def build_length_mod_dfa(alphabet, k):
    states = [f"q{i}" for i in range(k)]
    start_state = "q0"
    accept_states = {"q0"}   # length % k == 0

    transitions = {state: {} for state in states}

    for i in range(k):
        for sym in alphabet:
            transitions[f"q{i}"][sym] = f"q{(i + 1) % k}"

    return DFA(set(states), set(alphabet), transitions, start_state, accept_states)
