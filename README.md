# Python Mini-Projects Collection

A collection of simple, beginner-friendly command-line Python programs:

1. [Calculator](#1-calculator)
2. [Contact Book](#2-contact-book)
3. [Password Generator](#3-password-generator)
4. [To-Do List Application](#4-to-do-list-application)

## Requirements

- Python 3.10+ (required for the Calculator's `match` statement)
- No external libraries required (uses only Python's standard library)

## How to Run

Each program is a standalone script. Run any of them with:

```bash
python <filename>.py
```

---

## 1. Calculator

**File:** `Calculator.py`

A simple command-line calculator that performs basic arithmetic operations on two numbers.

### Features
- Supports addition, subtraction, multiplication, division, modulus, and exponentiation
- Accepts either a number (1-6) or a symbol (`+`, `-`, `*`, `/`, `%`, `**`) as the operation choice
- Handles division by zero gracefully

### Usage
1. Enter two numbers.
2. Choose an operation by number or symbol.
3. View the result.

### Example
```
Enter num1 : 10
Enter num2 : 5
Choose the operation you want to perform:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Exponentiation
Enter choice(1/2/3/4/5/6): 1
10 + 5 = 15
```

### Notes
- Only integer input is supported (`int(input(...))`); decimal input will raise an error.
- An invalid choice prints an error message instead of crashing.

---

## 2. Contact Book

**File:** `Contact_book.py`

A menu-driven contact management system for storing and managing contact details in memory.

### Features
- Add, view, search, update, and delete contacts
- Contacts stored with name, phone, email, and address
- Contact list displayed alphabetically by name
- Search by name or phone number
- Update fields selectively (leave blank to keep existing value)

### Menu Options
```
1. Add Contact
2. View Contact List
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
```

### Usage
Run the script and choose an option from the menu each time it's shown. The program loops until you select **Exit**.

### Notes
- Contacts are stored only in memory — they are lost when the program exits (no file/database persistence).
- Search matches on exact name or phone number, not partial matches.

---

## 3. Password Generator

**File:** `Password_generator.py`

Generates a random password of a user-specified length using letters, digits, and punctuation.

### Features
- Customizable password length
- Uses uppercase and lowercase letters, digits, and special characters
- Randomized character selection for each password

### Usage
1. Enter the desired password length.
2. View the generated password.

### Example
```
Enter the desired password length: 12
Generated Password: aT7!kLp9@zQx
```

### Notes
- No guarantee that every character type (letters, digits, punctuation) appears in the output — selection is fully random.
- No option to exclude ambiguous or specific characters.

---

## 4. To-Do List Application

**File:** `To_Do_List.py`

A menu-driven to-do list manager for tracking tasks and their completion status.

### Features
- Add, view, update, delete, and mark tasks as complete
- Tracks completion status (Pending / Completed) for each task
- Simple numbered task list for easy reference

### Menu Options
```
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Exit
```

### Usage
Run the script and choose an option from the menu each time it's shown. The program loops until you select **Exit**.

### Example
```
To-Do List Application
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Exit
Enter your choice (1-6): 1
Enter the task: Buy groceries
Task 'Buy groceries' added successfully.
```

### Notes
- Tasks are stored only in memory — they are lost when the program exits (no file/database persistence).
- Task numbers correspond to their position in the current list, which shifts after deletions.

---

## Possible Improvements

- **Calculator:** support decimal input, add a continuous calculation loop
- **Contact Book:** add file/database persistence (e.g., JSON or SQLite), support partial/fuzzy search
- **Password Generator:** allow selecting which character types to include, enforce minimum complexity rules
- **To-Do List Application:** add file/database persistence, due dates, and priority levels
