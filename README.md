# DFA Generator 🚦

A web-based **Deterministic Finite Automata (DFA) Generator** that allows users to design, visualize, and test DFAs for common string-based rules through an interactive interface.

---

## ✨ Features

- Interactive DFA rule selection UI
- Supports multiple DFA rules:
  - `even()`
  - `odd()`
  - `starts_with()`
  - `ends_with()`
  - `contains()`
  - `no_substring()`
  - `exact_count()`
  - `at_least()`
  - `length_mod()`
- Automatic DFA state diagram generation
- Test input strings directly in the browser
- Clean separation between frontend and backend logic

---

## 🧠 How It Works

1. Select a DFA rule from the UI
2. Configure required parameters
3. Click **Build DFA**
4. Enter a test string
5. View Accept/Reject result and DFA state diagram

Each DFA rule is implemented as a separate Python module and rendered dynamically using Graphviz.

---

## 📁 Project Structure

```
.
├── app.py
├── main.py
├── dfa.py
├── even_dfa.py
├── odd_dfa.py
├── starts_with_dfa.py
├── ends_with_dfa.py
├── contains_dfa.py
├── no_substring_dfa.py
├── exact_count_dfa.py
├── at_least_dfa.py
├── length_mod_dfa.py
├── index.html
├── static/
├── dfa_output.png
├── README.md
├── LICENSE
└── __pycache__/
```

---

## 🚀 Getting Started

### Clone the Repository
```bash
git clone https://github.com/your-username/dfa-generator.git
cd dfa-generator
```

### Install Dependencies
```bash
pip install flask graphviz
```

> Ensure Graphviz is installed and added to system PATH.

### Run the Application
```bash
python app.py
```

### Open in Browser
```
http://127.0.0.1:5000/
```

---

## 🧪 Supported DFA Rules

| Rule | Description |
|------|-------------|
| `even()` | Accepts strings with even occurrences of a symbol |
| `odd()` | Accepts strings with odd occurrences of a symbol |
| `starts_with(x)` | String must start with `x` |
| `ends_with(x)` | String must end with `x` |
| `contains(x)` | String must contain substring `x` |
| `no_substring(x)` | String must NOT contain substring `x` |
| `exact_count(x, n)` | Symbol `x` occurs exactly `n` times |
| `at_least(x, n)` | Symbol `x` occurs at least `n` times |
| `length_mod(n)` | String length ≡ 0 (mod n) |

---

## 🎓 Use Cases

- Theory of Computation lab projects
- DFA visualization for learning
- Exam preparation
- Teaching automata concepts interactively

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🚧 Future Enhancements

- DFA minimization
- NFA to DFA conversion
- Animated DFA traversal
- Export DFA diagrams and transition tables

---

Made with ❤️ for automata lovers and last-minute submissions.
