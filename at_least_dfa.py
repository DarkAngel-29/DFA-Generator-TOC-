from dfa import DFA

def build_at_least_dfa(alphabet, symbol, k):
    # states q0 ... qk
    states = [f"q{i}" for i in range(k + 1)]
    start_state = "q0"
    accept_states = {f"q{k}"}  # once we reach k, we accept forever

    transitions = {state: {} for state in states}

    for i in range(k + 1):
        for sym in alphabet:
            if sym == symbol:
                if i < k:
                    transitions[f"q{i}"][sym] = f"q{i+1}"
                else:
                    transitions[f"q{i}"][sym] = f"q{k}"
            else:
                transitions[f"q{i}"][sym] = f"q{i}"

    return DFA(set(states), set(alphabet), transitions, start_state, accept_states)
