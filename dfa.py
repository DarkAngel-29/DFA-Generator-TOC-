# dfa.py
from graphviz import Digraph

class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def run(self, input_string):
        current_state = self.start_state

        for symbol in input_string:
            if symbol not in self.alphabet:
                return False  # invalid symbol
            current_state = self.transitions[current_state][symbol]

        return current_state in self.accept_states

    def draw(self, filename="dfa"):
        dot = Digraph(format="png")
        dot.attr(rankdir="LR")

        # start arrow
        dot.node("", shape="none")
        dot.edge("", self.start_state)

        for state in self.states:
            if state in self.accept_states:
                dot.node(state, shape="doublecircle")
            else:
                dot.node(state, shape="circle")

        for src in self.transitions:
            for sym, dst in self.transitions[src].items():
                dot.edge(src, dst, label=sym)

        dot.render(filename, cleanup=True)
