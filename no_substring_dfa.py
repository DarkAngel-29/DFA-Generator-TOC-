from dfa import DFA

def build_no_substring_dfa(alphabet, pattern):
    m = len(pattern)
    states = [f"q{i}" for i in range(m + 1)]
    start_state = "q0"
    accept_states = set(states[:-1])  # all except full match state

    transitions = {state: {} for state in states}

    def longest_prefix_suffix(s):
        for l in range(len(s), 0, -1):
            if s.endswith(pattern[:l]):
                return l
        return 0

    for i in range(m + 1):
        for sym in alphabet:
            if i < m and sym == pattern[i]:
                next_len = i + 1
            else:
                candidate = pattern[:i] + sym
                next_len = longest_prefix_suffix(candidate)

            # once forbidden pattern is fully matched, stay there
            if i == m:
                transitions[f"q{i}"][sym] = f"q{m}"
            else:
                transitions[f"q{i}"][sym] = f"q{next_len}"

    return DFA(set(states), set(alphabet), transitions, start_state, accept_states)
