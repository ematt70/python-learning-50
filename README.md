# 🐍 Python Learning Journey — 50 Progressive Exercises

> A structured, self-paced curriculum that takes you from your very first `print()` statement to building real-world Python applications — one exercise at a time.

---

## Table of Contents

1. [Overview](#overview)
2. [Goals](#goals)
3. [Repository Structure](#repository-structure)
4. [How to Use This Repo](#how-to-use-this-repo)
5. [Phase Breakdown](#phase-breakdown)
   - [Phase 1 — Python Fundamentals (Exercises 1–10)](#phase-1--python-fundamentals-exercises-110)
   - [Phase 2 — Data Structures & Collections (Exercises 11–20)](#phase-2--data-structures--collections-exercises-1120)
   - [Phase 3 — Functions, Modules & OOP (Exercises 21–30)](#phase-3--functions-modules--oop-exercises-2130)
   - [Phase 4 — File I/O, Error Handling & Libraries (Exercises 31–40)](#phase-4--file-io-error-handling--libraries-exercises-3140)
   - [Phase 5 — Projects & Advanced Topics (Exercises 41–50)](#phase-5--projects--advanced-topics-exercises-4150)
6. [Running the Exercises](#running-the-exercises)
7. [Tracking Your Progress](#tracking-your-progress)
8. [Optional Next Steps](#optional-next-steps)
9. [Resources](#resources)

---

## Overview

This repository contains **50 carefully sequenced Python exercises** designed to build genuine programming fluency from the ground up. Each exercise introduces a new concept while reinforcing prior knowledge, creating a smooth, confidence-building learning curve.

The curriculum is divided into **five phases** of ten exercises each. By the end, you will have written dozens of working programs and completed multiple mini-projects — giving you a portfolio of real code to point to.

No prior programming experience is required to begin. A basic familiarity with using a terminal is helpful but not essential.

---

## Goals

By completing all 50 exercises, you will be able to:

- ✅ Understand Python's syntax, types, and core control flow
- ✅ Confidently work with lists, dictionaries, tuples, and sets
- ✅ Write clean, reusable functions and understand scope
- ✅ Apply Object-Oriented Programming (OOP) principles
- ✅ Read from and write to files and handle errors gracefully
- ✅ Use popular standard-library and third-party modules
- ✅ Build small command-line applications and scripts from scratch
- ✅ Develop habits around readable, well-documented code

---

## Repository Structure

```
python-50-exercises/
│
├── README.md                        ← You are here
├── progress.md                      ← Your personal progress tracker
│
├── phase1_fundamentals/
│   ├── ex01_hello_world.py
│   ├── ex02_variables.py
│   ├── ex03_user_input.py
│   ├── ex04_arithmetic.py
│   ├── ex05_string_formatting.py
│   ├── ex06_conditionals.py
│   ├── ex07_while_loops.py
│   ├── ex08_for_loops.py
│   ├── ex09_nested_logic.py
│   └── ex10_calculator.py
│
├── phase2_data_structures/
│   ├── ex11_lists_intro.py
│   ├── ex12_list_methods.py
│   ├── ex13_looping_lists.py
│   ├── ex14_list_comprehensions.py
│   ├── ex15_tuples.py
│   ├── ex16_dicts_intro.py
│   ├── ex17_dict_methods.py
│   ├── ex18_sets.py
│   ├── ex19_nested_collections.py
│   └── ex20_contact_book.py
│
├── phase3_functions_oop/
│   ├── ex21_functions_basics.py
│   ├── ex22_parameters_returns.py
│   ├── ex23_args_kwargs.py
│   ├── ex24_scope.py
│   ├── ex25_lambda.py
│   ├── ex26_modules.py
│   ├── ex27_classes_objects.py
│   ├── ex28_inheritance.py
│   ├── ex29_dunder_methods.py
│   └── ex30_library_system.py
│
├── phase4_files_errors_libs/
│   ├── ex31_read_file.py
│   ├── ex32_write_file.py
│   ├── ex33_csv_files.py
│   ├── ex34_json_files.py
│   ├── ex35_exception_handling.py
│   ├── ex36_custom_exceptions.py
│   ├── ex37_datetime.py
│   ├── ex38_os_pathlib.py
│   ├── ex39_random.py
│   └── ex40_expense_tracker.py
│
└── phase5_projects_advanced/
    ├── ex41_cli_todo_app.py
    ├── ex42_number_guessing_game.py
    ├── ex43_web_scraper.py
    ├── ex44_api_calls.py
    ├── ex45_decorators.py
    ├── ex46_generators.py
    ├── ex47_advanced_comprehensions.py
    ├── ex48_unit_testing.py
    ├── ex49_virtual_environments.py
    └── ex50_capstone_dashboard.py
```

---

## How to Use This Repo

### 1. Clone the repository

```bash
git clone https://github.com/your-username/python-50-exercises.git
cd python-50-exercises
```

### 2. Set up your Python environment

Make sure Python 3.10 or later is installed:

```bash
python3 --version
```

Optionally, create a virtual environment to keep dependencies clean:

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3. Work through exercises in order

Open each exercise file, read the instructions in the comments, and write your solution below them. Then run it:

```bash
python phase1_fundamentals/ex01_hello_world.py
```

### 4. Check your work

Each file contains:
- A **description** of what the exercise asks you to build
- **Hints** (commented out) if you get stuck
- An **expected output** section at the bottom for self-checking

### 5. Commit your progress

Get into the habit of committing after completing each exercise:

```bash
git add phase1_fundamentals/ex01_hello_world.py
git commit -m "Complete Ex01: Hello World"
```

---

## Phase Breakdown

---

### Phase 1 — Python Fundamentals (Exercises 1–10)

**Goal:** Get comfortable with Python's basic building blocks — syntax, types, input/output, and simple logic.

| #  | Exercise                      | Key Concept                                      |
|----|-------------------------------|--------------------------------------------------|
| 01 | Hello, World!                 | `print()`, running a script                      |
| 02 | Variables & Types             | `int`, `float`, `str`, `bool`                    |
| 03 | User Input                    | `input()`, type casting                          |
| 04 | Basic Arithmetic              | Operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`  |
| 05 | String Formatting             | f-strings, `.format()`                           |
| 06 | Conditionals                  | `if`, `elif`, `else`                             |
| 07 | While Loops                   | Loop control, `break`, `continue`                |
| 08 | For Loops & Ranges            | `for`, `range()`                                 |
| 09 | Nested Logic                  | Combining loops and conditionals                 |
| 10 | Mini-Project: Simple Calculator | Puts Exercises 1–9 together                    |

**Phase 1 Milestone:** Build a command-line calculator that handles addition, subtraction, multiplication, and division with input validation.

---

### Phase 2 — Data Structures & Collections (Exercises 11–20)

**Goal:** Learn to store, organize, and manipulate data using Python's built-in collection types.

| #  | Exercise                  | Key Concept                                          |
|----|---------------------------|------------------------------------------------------|
| 11 | Lists — Intro             | Creating, indexing, slicing                          |
| 12 | List Methods              | `.append()`, `.remove()`, `.sort()`, `.pop()`        |
| 13 | Looping Over Lists        | `for` with lists, `enumerate()`                      |
| 14 | List Comprehensions       | Compact list-building syntax                         |
| 15 | Tuples                    | Immutability, packing/unpacking                      |
| 16 | Dictionaries — Intro      | Key-value pairs, CRUD operations                     |
| 17 | Dictionary Methods        | `.keys()`, `.values()`, `.items()`, `.get()`         |
| 18 | Sets                      | Uniqueness, `union`, `intersection`, `difference`    |
| 19 | Nested Collections        | Dicts of lists, lists of dicts                       |
| 20 | Mini-Project: Contact Book | Dictionary-based contact manager                    |

**Phase 2 Milestone:** Build an in-memory contact book that lets the user add, search, update, and delete contacts stored in a dictionary.

---

### Phase 3 — Functions, Modules & OOP (Exercises 21–30)

**Goal:** Write organized, reusable code using functions and Python's object-oriented features.

| #  | Exercise                     | Key Concept                                      |
|----|------------------------------|--------------------------------------------------|
| 21 | Functions — Basics           | `def`, calling functions, `return`               |
| 22 | Parameters & Defaults        | Positional, keyword, and default arguments       |
| 23 | `*args` & `**kwargs`         | Variable-length arguments                        |
| 24 | Scope & Global Variables     | LEGB rule                                        |
| 25 | Lambda Functions             | Anonymous one-liners with `lambda`               |
| 26 | Importing Modules            | `import`, `from … import`, `as`                 |
| 27 | Classes & Objects            | `class`, `__init__`, attributes, methods         |
| 28 | Inheritance                  | Subclasses, `super()`, method overriding         |
| 29 | Dunder Methods               | `__str__`, `__repr__`, `__len__`, `__eq__`       |
| 30 | Mini-Project: Library System | OOP-based book catalog                           |

**Phase 3 Milestone:** Build a library catalog using classes for `Book` and `Library`, supporting add, remove, search, and display operations.

---

### Phase 4 — File I/O, Error Handling & Libraries (Exercises 31–40)

**Goal:** Make your programs interact with the real world — files, errors, dates, and third-party tools.

| #  | Exercise                        | Key Concept                                        |
|----|---------------------------------|----------------------------------------------------|
| 31 | Reading Files                   | `open()`, `read()`, `readlines()`                  |
| 32 | Writing Files                   | `write()`, `writelines()`, `with` statement        |
| 33 | CSV Files                       | `csv` module, reading/writing tabular data         |
| 34 | JSON Files                      | `json` module, serialization & deserialization     |
| 35 | Exception Handling              | `try`, `except`, `finally`, `raise`                |
| 36 | Custom Exceptions               | Defining your own exception classes                |
| 37 | `datetime` Module               | Dates, times, formatting, arithmetic               |
| 38 | `os` & `pathlib`                | File system navigation, path manipulation          |
| 39 | `random` Module                 | Random numbers, choices, shuffling                 |
| 40 | Mini-Project: Expense Tracker   | CSV-backed command-line expense logger             |

**Phase 4 Milestone:** Build an expense tracker that saves and loads records from a CSV file, calculates totals by category, and handles bad input gracefully.

---

### Phase 5 — Projects & Advanced Topics (Exercises 41–50)

**Goal:** Synthesize everything into complete applications and explore intermediate-level Python concepts.

| #  | Exercise                             | Key Concept                                      |
|----|--------------------------------------|--------------------------------------------------|
| 41 | CLI To-Do App                        | `argparse`, persistent JSON storage              |
| 42 | Number Guessing Game                 | Game loop, randomness, input validation          |
| 43 | Web Scraper (Basic)                  | `requests` + `BeautifulSoup`                     |
| 44 | API Calls                            | `requests`, JSON APIs, error handling            |
| 45 | Decorators                           | `@decorator` syntax, wrapping functions          |
| 46 | Generators & Iterators               | `yield`, `next()`, lazy evaluation               |
| 47 | Comprehensions (Advanced)            | Dict/set comprehensions, nesting                 |
| 48 | Unit Testing with `unittest`         | Writing and running tests, `assert`              |
| 49 | Virtual Environments & `pip`         | Dependency management best practices             |
| 50 | Capstone Project: Personal Dashboard | Combines APIs, files, OOP, and CLI               |

**Phase 5 Milestone (Capstone):** Build a personal command-line dashboard that fetches live weather data from a public API, displays your to-do list from a local file, and shows your recent expenses — all in a clean terminal interface.

---

## Running the Exercises

Run any single exercise:

```bash
python phase2_data_structures/ex14_list_comprehensions.py
```

Run all exercises in a phase (macOS / Linux):

```bash
for f in phase1_fundamentals/*.py; do echo "--- $f ---"; python "$f"; done
```

Run unit tests (Phase 4+):

```bash
python -m unittest discover -s phase4_files_errors_libs -p "test_*.py"
```

---

## Tracking Your Progress

Use `progress.md` at the root of the repo to log your completions. A simple table works well:

```markdown
| Exercise | Status           | Date Completed | Notes                     |
|----------|------------------|----------------|---------------------------|
| Ex01     | ✅ Done          | 2026-09-01     | Easy warm-up              |
| Ex02     | ✅ Done          | 2026-09-01     | Needed to review casting  |
| Ex03     | 🔄 In Progress   | —              |                           |
| Ex04     | ⬜ Not Started   | —              |                           |
```

Commit `progress.md` regularly — watching it fill up is genuinely motivating.

---

## Optional Next Steps

Once you have completed all 50 exercises, consider these paths to level up further:

### 🌐 Web Development
- **Flask** or **FastAPI** — build REST APIs and web apps
- **Django** — full-stack web framework with batteries included

### 📊 Data Science & Analysis
- **pandas** — data manipulation and analysis
- **matplotlib** / **seaborn** — data visualization
- **NumPy** — numerical computing

### 🤖 Automation & Scripting
- **Selenium** or **Playwright** — browser automation
- **schedule** — task scheduling
- **Paramiko** — SSH and remote server scripting

### 🧠 Machine Learning
- **scikit-learn** — classical ML algorithms
- **PyTorch** or **TensorFlow** — deep learning

### 🏗️ Software Engineering Skills
- Learn **Git branching strategies** (feature branches, pull requests)
- Explore **design patterns** in Python
- Study **PEP 8** and clean code principles

---

## Resources

| Resource            | Type          | URL                                      |
|---------------------|---------------|------------------------------------------|
| Official Python Docs | Reference    | https://docs.python.org/3/               |
| Real Python          | Tutorials    | https://realpython.com                   |
| Python Tutor         | Visualizer   | https://pythontutor.com                  |
| PyPI                 | Package Index | https://pypi.org                        |
| PEP 8 Style Guide    | Style        | https://peps.python.org/pep-0008/        |

---

<p align="center">
  Built with 🐍 Python &nbsp;·&nbsp; Maintained by <strong>Erich</strong><br>
  <em>"The best way to learn to code is to write a lot of code."</em>
</p>
