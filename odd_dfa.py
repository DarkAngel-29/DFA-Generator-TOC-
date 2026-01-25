from dfa import DFA

def build_odd_dfa(alphabet, target):
    states = {"q0", "q1"}          # q0 = even, q1 = odd
    start_state = "q0"
    accept_states = {"q1"}         # ONLY change vs even()

    transitions = {
        "q0": {},
        "q1": {}
    }

    for sym in alphabet:
        if sym == target:
            transitions["q0"][sym] = "q1"
            transitions["q1"][sym] = "q0"
        else:
            transitions["q0"][sym] = "q0"
            transitions["q1"][sym] = "q1"

    return DFA(states, alphabet, transitions, start_state, accept_states)
