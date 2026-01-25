from dfa import DFA

def build_exact_count_dfa(alphabet, symbol, k):
    # states q0 ... qk and dead
    states = [f"q{i}" for i in range(k + 1)] + ["dead"]
    start_state = "q0"
    accept_states = {f"q{k}"}  # exactly k occurrences

    transitions = {state: {} for state in states}

    for i in range(k + 1):
        for sym in alphabet:
            if sym == symbol:
                if i < k:
                    transitions[f"q{i}"][sym] = f"q{i+1}"
                else:
                    transitions[f"q{i}"][sym] = "dead"
            else:
                transitions[f"q{i}"][sym] = f"q{i}"

    # dead state loops to itself
    for sym in alphabet:
        transitions["dead"][sym] = "dead"

    return DFA(set(states), set(alphabet), transitions, start_state, accept_states)
