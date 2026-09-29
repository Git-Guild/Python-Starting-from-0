# Python Starting from 0

A structured, beginner-friendly repository for learning Python from absolute scratch. This repo follows a progressive curriculum covering core Python concepts, from basic data types all the way through object-oriented programming and file handling, with hands-on projects and practice problems.

Maintained by [Git Guild](https://github.com/Git-Guild).

---

## Table of Contents

- [Who Is This For?](#who-is-this-for)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Learning Path](#learning-path)
- [Projects](#projects)
- [FreeCodeCamp Certification Problems](#freecodecamp-certification-problems)
- [How to Use This Repo](#how-to-use-this-repo)
- [Contributing](#contributing)
- [License](#license)

---

## Who Is This For?

This repository is designed for:

- **Complete beginners** who have never written code before
- **Students** looking for a structured Python learning path
- **Self-learners** who want curated practice material organized by topic
- **Educators** who need a ready-made curriculum to teach introductory Python

No prior programming experience is required.

---

## Repository Structure

```
Python-Starting-from-0/
├── Learning/                        # Core Python topic files
│   ├── Lec1-Data Types.py           # Variables, strings, integers, floats, booleans
│   ├── Lec2-Conditional Statements.py # if/elif/else, logical operators
│   ├── Lec3-List & Tuple.py         # Indexing, slicing, list methods, tuples
│   ├── Lec4-Dictionary & Sets.py    # Key-value pairs, set operations
│   ├── Lec5-Loops.py                # for loops, while loops, iteration patterns
│   ├── Lec6-Functions & Recursions.py # Defining functions, parameters, recursion
│   ├── Lec7-Files.py                # File I/O, reading/writing files
│   ├── Lec8-OOPS.py                 # Classes, objects, inheritance, encapsulation
│   ├── Lec9_OOPS2.py                # Advanced OOP: polymorphism, abstract classes
│   ├── Lec5 Prac.py                 # Practice exercises for loops
│   ├── Lec5.py                      # Additional loop examples
│   ├── Lec7-Prac.py                 # Practice exercises for file handling
│   ├── Hackerrank Basic Problems.py # Solved HackerRank beginner challenges
│   └── misc.py                      # Miscellaneous notes and experiments
├── Projects/                        # Applied projects
│   ├── Calculator.py                # Basic calculator application
│   ├── Emi_Calculator.py            # EMI/loan payment calculator
│   ├── Weight Converter.py          # Unit conversion tool
│   └── Word to Num.py              # Converts number words to digits
├── freecodecamp Certificate/        # FreeCodeCamp Scientific Computing exercises
│   ├── Budget_app.py                # Budget tracking application
│   ├── Hanoi.py                     # Tower of Hanoi solver
│   ├── HashTable.py                 # Hash table implementation
│   ├── Polygon_Area_Calculator.py   # Polygon geometry calculator
│   └── User_COnfiguration.py        # User configuration system
└── README.md
```

---

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/Git-Guild/Python-Starting-from-0.git
   ```

2. **Navigate to the project directory**

   ```bash
   cd Python-Starting-from-0
   ```

3. **Run any file**

   ```bash
   python Learning/Lec1-Data\ Types.py
   ```

That's it. No installation or dependencies are required.

---

## Prerequisites

- **Python 3.8+** installed on your system ([Download Python](https://www.python.org/downloads/))
- A **code editor** (VS Code, PyCharm, Sublime Text, or any editor you prefer)
- A **terminal or command prompt** to run Python scripts

---

## Learning Path

Follow the lectures in order for a progressive learning experience:

| Order | File | Topic | Key Concepts |
|-------|------|-------|--------------|
| 1 | `Lec1-Data Types.py` | Data Types | Variables, strings, integers, floats, booleans, type casting |
| 2 | `Lec2-Conditional Statements.py` | Conditionals | if/elif/else, comparison operators, logical operators |
| 3 | `Lec3-List & Tuple.py` | Lists & Tuples | Indexing, slicing, list methods, tuple immutability |
| 4 | `Lec4-Dictionary & Sets.py` | Dicts & Sets | Key-value pairs, dictionaries, set operations |
| 5 | `Lec5-Loops.py` | Loops | for loops, while loops, range(), break/continue |
| 6 | `Lec6-Functions & Recursions.py` | Functions | Defining functions, parameters, return values, recursion |
| 7 | `Lec7-Files.py` | File I/O | Reading files, writing files, context managers |
| 8 | `Lec8-OOPS.py` | OOP Basics | Classes, objects, methods, `__init__`, inheritance |
| 9 | `Lec9_OOPS2.py` | Advanced OOP | Polymorphism, abstract classes, method overriding |

After completing the learning modules, move on to the practice problems and projects to reinforce your understanding.

---

## Projects

Applied projects that combine multiple concepts from the learning path:

| Project | Description | Concepts Used |
|---------|-------------|---------------|
| `Calculator.py` | A basic calculator that performs arithmetic operations | Functions, conditionals, user input |
| `Emi_Calculator.py` | Calculates monthly EMI payments for loans | Functions, arithmetic, formatting |
| `Weight Converter.py` | Converts weights between different units | Conditionals, functions, user input |
| `Word to Num.py` | Converts number words (e.g., "one") to digits | Strings, dictionaries, string parsing |

---

## FreeCodeCamp Certification Problems

Solutions to exercises from the [FreeCodeCamp Python v9](https://www.freecodecamp.org/learn/python-v9/) certification. This folder contains completed projects and challenges from the course. If you are working through the certification yourself, use these as reference after attempting each challenge on your own.

| File | Description |
|------|-------------|
| `Budget_app.py` | Category budget tracking system |
| `Hanoi.py` | Tower of Hanoi recursive solver |
| `HashTable.py` | Hash table data structure implementation |
| `Polygon_Area_Calculator.py` | Polygon area calculation using geometry |
| `User_COnfiguration.py` | User configuration management system |

---

## How to Use This Repo

### As a Self-Learner

1. Start with `Lec1-Data Types.py` and work through each file in order
2. Read the code and comments in each file
3. Type out the code yourself rather than copying and pasting
4. Modify examples and experiment with changes to deepen your understanding
5. Complete the practice files (`Lec5 Prac.py`, `Lec7-Prac.py`) before moving on
6. Attempt the projects after finishing all learning modules

### As an Educator

- Use the `Learning/` directory as a lesson-by-lesson curriculum
- Assign the `Projects/` directory as homework or take-home exercises
- Use the FreeCodeCamp solutions as reference implementations for teaching

### Practice Problems

After each learning module, reinforce your skills with these external platforms:

- [HackerRank Python](https://www.hackerrank.com/domains/python) - Track your progress in `Hackerrank Basic Problems.py`
- [LeetCode](https://leetcode.com/problemset/all/) - Filter by "Easy" and Python tag
- [FreeCodeCamp Python v9](https://www.freecodecamp.org/learn/python-v9/) - Solutions included in this repo

---

## Contributing

Contributions are welcome. If you want to add practice problems, fix errors, or improve explanations:

1. Fork the repository
2. Create a new branch for your change
3. Make your changes
4. Submit a pull request with a clear description of what you changed and why

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for full details.

You are free to use, modify, and distribute this material for personal or commercial purposes, with or without attribution.
