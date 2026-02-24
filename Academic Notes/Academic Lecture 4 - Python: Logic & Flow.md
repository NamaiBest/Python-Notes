# Git, GitHub, and Introduction to Python  
Detailed Lecture Notes

---

# 1. Git and GitHub: Version Control and Collaboration

## What is Git?

### Definition

Git is a distributed version control system.

### What That Means in Simple Terms

Git helps you:
- Track changes in your code
- Go back to older versions if something breaks
- Work with other developers without overwriting each other's work

Think of Git like a "history tracker" for your project.

If you make a mistake today, Git allows you to return to yesterday’s working version.

---

## Why Do We Need Version Control?

Imagine you are writing a large project:
- You change something.
- The program stops working.
- You do not remember what you changed.

Without Git:
You are stuck.

With Git:
You can go back to a previous version safely.

---

## Local vs Remote Repository

### Local Repository

This is the version of the project stored on your own computer.

You:
- Edit code
- Test changes
- Save commits

It exists only on your machine.

---

### Remote Repository

This is a copy of your project stored online.

Example platform:
GitHub

Purpose:
- Backup your project
- Share it with others
- Collaborate with teammates

---

## What is GitHub?

GitHub is a web platform that hosts Git repositories.

In simple terms:
Git is the tool.
GitHub is the website where projects are stored and shared.

GitHub allows you to:
- Upload code
- Collaborate with others
- Track issues
- Review code
- Manage versions

GitHub is owned by Microsoft.

---

## Important Git Commands

| Command | What It Does | Simple Meaning |
|----------|--------------|----------------|
| `git init` | Creates a new Git repository | Start tracking a project |
| `git clone` | Copies a remote repo to your machine | Download project from GitHub |
| `git status` | Shows changed files | See what has changed |
| `git add` | Stages files | Prepare changes to save |
| `git commit` | Saves changes locally | Take a snapshot |
| `git push` | Sends changes to remote | Upload to GitHub |
| `git pull` | Downloads updates from remote | Get latest changes |
| `git remote` | Shows remote connections | Check linked repositories |

---

## Basic Git Workflow

1. Clone the repository.
2. Make changes.
3. Use `git add` to stage changes.
4. Use `git commit` to save changes locally.
5. Use `git pull` to get latest updates.
6. Use `git push` to upload your changes.

---

## Why "Pull Before Push"?

If someone else has updated the project:

If you push without pulling:
You may create a conflict.

Pulling first ensures:
You are working on the latest version.

---

## Best Practices in Git

- Always pull before pushing.
- Write clear commit messages.
- Make small commits frequently.
- Do not commit unnecessary files.

---

# 2. Introduction to Programming

## What is Programming?

Programming means writing instructions that a computer can follow.

Computers do not understand human language.
They only understand structured instructions written in programming languages.

In simple terms:
Programming is telling the computer exactly what to do.

---

## Why Python?

Python is popular because:

- Simple and readable syntax
- Easy for beginners
- Powerful for professionals
- Used in web development, automation, data science, AI, and more

Python reads almost like English.

---

## Programming Environment Used

### Google Colab

Google Colab is an online platform where you can:
- Write Python code
- Run it instantly
- Save your work
- Share with others

You do not need to install Python on your computer.

---

# 3. Basic Python Syntax and Concepts

## Printing Output

To display output on screen, use:

```python
print("Hello everyone")
```

`print()` tells the computer to show something on the screen.

---

## Variables

### What is a Variable?

A variable stores information.

Think of it like a labeled box.

Example:

```python
message = "Welcome to Python"
print(message)
```

Here:
- `message` is the box
- `"Welcome to Python"` is the value inside the box

Variables can change anytime.

---

## Data Types

Different kinds of data exist in Python.

### Integer (int)

Whole numbers.

Example:
```
5
100
-20
```

---

### String (str)

Text inside quotes.

Example:
```
"Hello"
"Python"
```

---

### Boolean (bool)

Represents logical values.

Only two values exist:
```
True
False
```

Used in decision making.

---

## Checking Data Type

Use:

```python
x = 10
print(type(x))
```

Output:
```
<class 'int'>
```

`type()` tells you what kind of data something is.

---

## Input and Output

### Getting Input

```python
name = input("Enter your name: ")
```

Important:
`input()` always returns a string.

---

### Converting Input

If you want a number:

```python
age = int(input("Enter your age: "))
```

`int()` converts string to integer.

If the user enters text instead of a number, an error will occur.

---

# 4. Control Flow and Logic

## What is Control Flow?

Control flow means deciding:
- Which code runs
- When it runs
- How many times it runs

---

## Conditional Statements

Used when the program needs to make decisions.

### Syntax

```python
if condition:
    # code if True
else:
    # code if False
```

---

### Example: Voting Eligibility

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("Not eligible to vote.")
```

Meaning:
If age is 18 or more → eligible.
Otherwise → not eligible.

---

## Importance of Indentation

Python uses indentation (spaces) to group code.

Correct:

```python
if age >= 18:
    print("Eligible")
```

Incorrect indentation causes errors.

Indentation tells Python which lines belong together.

---

# 5. Python Keywords Covered

Keywords are reserved words.
They have special meaning in Python.
You cannot use them as variable names.

| Keyword | Purpose |
|----------|----------|
| `if` | Start condition |
| `else` | Alternative block |
| `print` | Display output |
| `input` | Take user input |
| `int` | Convert to integer |
| `True` | Boolean true value |
| `False` | Boolean false value |

---

# 6. Important Learning Tips

- Pull before push in Git.
- Build programs step by step.
- Test small parts frequently.
- Improve typing speed.
- Accept errors as part of learning.
- Practice regularly.
- Learn to read error messages carefully.

---

# Summary Example Program

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("Not eligible to vote.")
```

This program:
1. Takes input.
2. Converts it to a number.
3. Checks a condition.
4. Displays output based on decision.

---

# Final Understanding

Git helps track changes in projects.

GitHub helps share and collaborate.

Programming is giving instructions to a computer.

Python is a simple and powerful language used to automate tasks and build real-world applications.