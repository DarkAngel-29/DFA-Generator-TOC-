from even_dfa import build_even_dfa
from odd_dfa import build_odd_dfa
from ends_with_dfa import build_ends_with_dfa
from contains_dfa import build_contains_dfa
from starts_with_dfa import build_starts_with_dfa
from no_substring_dfa import build_no_substring_dfa
from exact_count_dfa import build_exact_count_dfa
from at_least_dfa import build_at_least_dfa
from length_mod_dfa import build_length_mod_dfa

def main():
    print("Select rule:")
    print("1. even()")
    print("2. odd()")
    print("3. ends_with()")
    print("4. contains()")
    print("5. starts_with()")
    print("6. no_substring()")
    print("7. exact_count()")
    print("8. at_least()")
    print("9. length_mod()")



    choice = input("Enter choice: ").strip()

    if choice not in {"1", "2","3","4","5","6","7","8","9"}:
        print("Invalid choice")
        return

    alpha_input = input("Enter alphabet (comma separated): ")
    alphabet = set(sym.strip() for sym in alpha_input.split(","))

    

    if choice == "1":
        target = input("Enter symbol: ").strip()
        if target not in alphabet:
            print("Target must be in alphabet")
            return
        dfa = build_even_dfa(alphabet, target)

    elif choice == "2":
        target = input("Enter symbol: ").strip()
        if target not in alphabet:
            print("Target must be in alphabet")
            return
        dfa = build_odd_dfa(alphabet, target)
    
    elif choice == "3":
        pattern = input("Enter suffix pattern (e.g. ab): ").strip()
        if not pattern:
            print("Pattern cannot be empty")
            return
        dfa = build_ends_with_dfa(alphabet, pattern)
   
    elif choice == "4":
        pattern = input("Enter substring pattern (e.g. aba): ").strip()
        if not pattern:
            print("Pattern cannot be empty")
            return
        dfa = build_contains_dfa(alphabet, pattern)

    elif choice == "5":
        pattern = input("Enter prefix pattern (e.g. ab): ").strip()
        if not pattern:
            print("Pattern cannot be empty")
            return
        dfa = build_starts_with_dfa(alphabet, pattern)

    elif choice == "6":
        pattern = input("Enter forbidden substring (e.g. 11): ").strip()
        if not pattern:
            print("Pattern cannot be empty")
            return
        dfa = build_no_substring_dfa(alphabet, pattern)

    elif choice == "7":
        symbol = input("Enter symbol to count: ").strip()
        k = int(input("Enter exact count (k): "))
        if symbol not in alphabet:
            print("Symbol must be in alphabet")
            return
        dfa = build_exact_count_dfa(alphabet, symbol, k)

    elif choice == "8":
        symbol = input("Enter symbol to count: ").strip()
        k = int(input("Enter minimum count (k): "))
        if symbol not in alphabet:
            print("Symbol must be in alphabet")
            return
        dfa = build_at_least_dfa(alphabet, symbol, k)
    
    elif choice == "9":
        k = int(input("Enter modulo value (k): "))
        if k <= 0:
            print("k must be positive")
            return
        dfa = build_length_mod_dfa(alphabet, k)

    print("\nDFA created. Test strings (type 'exit' to quit)\n")

    try:
        dfa.draw("dfa_output")
        print("DFA diagram generated as dfa_output.png\n")
    except Exception:
        print("Graphviz not available. DFA saved as .dot format.\n")

    while True:
        s = input("Input string: ")
        if s == "exit":
            break
        print("VALID\n" if dfa.run(s) else "INVALID\n")

if __name__ == "__main__":
    main()
