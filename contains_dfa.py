from dfa import DFA

def build_contains_dfa(alphabet, pattern):
    m = len(pattern)
    states = [f"q{i}" for i in range(m + 1)]
    start_state = "q0"
    accept_states = {f"q{m}"}

    transitions = {state: {} for state in states}

    def longest_prefix_suffix(s):
        for l in range(len(s), 0, -1):
            if s.endswith(pattern[:l]):
                return l
        return 0

    for i in range(m + 1):
        for sym in alphabet:
            if i < m and sym == pattern[i]:
                transitions[f"q{i}"][sym] = f"q{i+1}"
            else:
                candidate = pattern[:i] + sym
                next_len = longest_prefix_suffix(candidate)
                transitions[f"q{i}"][sym] = f"q{next_len}"

    # accept state stays accepting forever
    for sym in alphabet:
        transitions[f"q{m}"][sym] = f"q{m}"

    return DFA(set(states), set(alphabet), transitions, start_state, accept_states)
