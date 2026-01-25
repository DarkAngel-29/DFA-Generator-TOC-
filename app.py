from flask import Flask, request, jsonify, send_from_directory
from even_dfa import build_even_dfa
from odd_dfa import build_odd_dfa
from starts_with_dfa import build_starts_with_dfa
from ends_with_dfa import build_ends_with_dfa
from contains_dfa import build_contains_dfa
from no_substring_dfa import build_no_substring_dfa
from exact_count_dfa import build_exact_count_dfa
from at_least_dfa import build_at_least_dfa
from length_mod_dfa import build_length_mod_dfa

app = Flask(__name__, static_folder="static")

current_dfa = None   # store DFA in memory


@app.route("/build", methods=["POST"])
def build():
    global current_dfa
    data = request.json

    rule = data["rule"]
    alphabet = set(data["alphabet"])

    if rule == "even":
        current_dfa = build_even_dfa(alphabet, data["symbol"])
    elif rule == "odd":
        current_dfa = build_odd_dfa(alphabet, data["symbol"])
    elif rule == "starts_with":
        current_dfa = build_starts_with_dfa(alphabet, data["pattern"])
    elif rule == "ends_with":
        current_dfa = build_ends_with_dfa(alphabet, data["pattern"])
    elif rule == "contains":
        current_dfa = build_contains_dfa(alphabet, data["pattern"])
    elif rule == "no_substring":
        current_dfa = build_no_substring_dfa(alphabet, data["pattern"])
    elif rule == "exact_count":
        current_dfa = build_exact_count_dfa(alphabet, data["symbol"], data["k"])
    elif rule == "at_least":
        current_dfa = build_at_least_dfa(alphabet, data["symbol"], data["k"])
    elif rule == "length_mod":
        current_dfa = build_length_mod_dfa(alphabet, data["k"])

    # generate DFA diagram (safe)
    try:
        current_dfa.draw("static/dfa")
    except Exception:
        pass

    return jsonify({"status": "DFA built"})


@app.route("/test", methods=["POST"])
def test():
    if not current_dfa:
        return jsonify({"error": "DFA not built yet"})

    s = request.json["string"]
    return jsonify({"valid": current_dfa.run(s)})


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


if __name__ == "__main__":
    app.run(debug=True)
