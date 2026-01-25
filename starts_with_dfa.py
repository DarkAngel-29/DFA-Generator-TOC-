from dfa import DFA

def build_starts_with_dfa(alphabet, pattern):
    m = len(pattern)
    states = [f"q{i}" for i in range(m + 2)]
    start_state = "q0"
    accept_states = {f"q{m}", f"q{m+1}"}

    transitions = {state: {} for state in states}

    # matching prefix
    for i in range(m):
        for sym in alphabet:
            if sym == pattern[i]:
                transitions[f"q{i}"][sym] = f"q{i+1}"
            else:
                transitions[f"q{i}"][sym] = "dead"

    # once matched fully, stay accepting
    for sym in alphabet:
        transitions[f"q{m}"][sym] = f"q{m+1}"
        transitions[f"q{m+1}"][sym] = f"q{m+1}"

    # dead state
    transitions["dead"] = {sym: "dead" for sym in alphabet}
    states.append("dead")

    return DFA(set(states), set(alphabet), transitions, start_state, accept_states)
