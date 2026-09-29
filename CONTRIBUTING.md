# Contributing to Python Starting from 0

Thanks for your interest in contributing. This guide explains how to add content, fix issues, and submit changes.

---

## Ways to Contribute

- **Add practice problems** to the `Learning/` directory
- **Fix bugs** or typos in existing code files
- **Improve comments and explanations** in lecture files
- **Add new projects** to the `Projects/` directory
- **Update the README** with better structure or corrected information

---

## Rules

1. **Keep it beginner-friendly.** This repo targets people learning Python for the first time. Avoid advanced or obscure patterns.
2. **Add clear comments.** Every code file should have comments explaining what each section does.
3. **Follow the naming convention.** Lecture files should follow the format `LecN-Topic Name.py`. Practice files should be named `LecN Prac.py`.
4. **Test your code.** Make sure every file you add or modify runs without errors using Python 3.8+.
5. **One concept per file.** Don't combine unrelated topics into a single file.

---

## How to Submit a Change

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/Python-Starting-from-0.git
   ```
3. Create a branch for your change:
   ```bash
   git checkout -b add-string-practice
   ```
4. Make your changes and verify they work:
   ```bash
   python Learning/your-file.py
   ```
5. Commit with a clear message:
   ```bash
   git commit -m "Add practice problems for string operations"
   ```
6. Push to your fork:
   ```bash
   git push origin add-string-practice
   ```
7. Open a pull request on the original repository with a description of what you changed and why.

---

## File Structure Guidelines

### Lecture Files

```python
# LecN-Topic Name.py
# Description: Brief explanation of what this file covers

# --- Section 1: Core Concept ---
# Explanation of the concept

example_code = "demonstration"
print(example_code)

# --- Section 2: Practice ---
# Interactive or practice examples
```

### Practice Files

```python
# LecN Prac.py
# Practice problems for Topic Name
# Try solving each problem before looking at the solution

# Problem 1: Description of the problem
# Your code here

# Solution (hidden below)
# -----------------------------------------------
# solution_code = "answer"
```

### Project Files

```python
# ProjectName.py
# A short description of what this project does
# Concepts used: concept1, concept2, concept3

# Implementation
```

---

## Reporting Issues

If you find a bug or have a suggestion:

1. Check existing issues to avoid duplicates.
2. Open a new issue with a clear title and description.
3. Include the file name, line number, and what you expected vs. what happened.

---

## Code Style

- Use **snake_case** for variable and function names
- Use **PascalCase** for class names
- Keep lines under **100 characters** where possible
- Add a **docstring** or comment at the top of every file explaining its purpose
- Use **f-strings** for string formatting (Python 3.6+)
