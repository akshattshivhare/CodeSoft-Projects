# CODSOFT Python Programming Internship - Tasks

Three command-line Python projects completed for the CODSOFT internship (September batch, C24).
Requires Python 3.8+ and no external libraries.

| # | Task | File | What it does |
|---|------|------|--------------|
| 1 | Calculator | `task1_calculator/calculator.py` | Takes two numbers and an operation (+, -, *, /, %, **), handles invalid input and divide-by-zero, and loops until you quit |
| 2 | Password Generator | `task2_password_generator/password_generator.py` | Generates secure random passwords of a chosen length with optional uppercase, digits and symbols, and rates their strength |
| 3 | To-Do List | `task3_todo_list/todo_list.py` | Add, view, edit, complete and delete tasks, saved to `tasks.json` so they persist between runs |

## How to run

```bash
python task1_calculator/calculator.py
python task2_password_generator/password_generator.py
python task3_todo_list/todo_list.py
```

## Highlights
- Input validation everywhere, so bad input never crashes the program
- Password generator uses Python's `secrets` module (cryptographically secure) and guarantees at least one character from each selected type
- To-do list persists data in JSON

#codsoft
