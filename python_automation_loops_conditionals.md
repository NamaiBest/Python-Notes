# Python Automation, Loops, and Conditionals: 12th Feb


---

## 1. Overview

### Main Focus

This lecture introduces fundamental Python programming concepts with emphasis on:

- Automation
- Conditionals (`if`, `elif`, `else`)
- Loops (`for`, `while`)
- Lists
- Basic error handling

Practical examples include:
- A password authentication system
- A simple interactive console program

### Core Goals

- Understand how automation works in programming
- Learn how programs make decisions
- Learn how to repeat tasks using loops
- Handle user input properly

---

## 2. Automation

### Definition

Automation means using a program to perform tasks automatically without manual repetition.

In simple terms:
Instead of doing the same task again and again yourself, you write code once and let the computer do it.

### Why Automation is Important

- Saves time
- Reduces human error
- Handles repetitive tasks efficiently
- Processes large amounts of data quickly

### Real-World Examples

- Counting words in a large document
- Automatic attendance calculation
- Salary calculation systems
- Online form validation

### Key Idea

Programming exists mainly to automate tasks and solve real problems efficiently.

---

## 3. Conditionals

### What Are Conditionals?

Conditionals allow a program to make decisions.

A condition is an expression that evaluates to:
- `True`
- `False`

Based on that result, the program chooses which block of code to run.

---

### Basic Syntax

```python
if condition:
    # runs if condition is True
elif another_condition:
    # runs if first condition is False and this is True
else:
    # runs if all conditions are False
```

---

### Meaning of Each Keyword

| Keyword | Meaning in Simple Terms |
|----------|------------------------|
| `if` | Check this condition first |
| `elif` | Check another condition if previous was False |
| `else` | Do this if none of the above conditions are True |

---

### Example: Checking Age

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible.")
```

Here:
- `age >= 18` is the condition.
- If it is True, the first block runs.
- Otherwise, the `else` block runs.

---

## Logical Operators

Logical operators allow combining multiple conditions.

| Operator | Meaning | Simple Explanation |
|----------|---------|-------------------|
| `and` | Both conditions must be True | All conditions must match |
| `or` | At least one condition must be True | Any one condition is enough |
| `not` | Reverses the condition | Makes True become False |

---

### Example with `and`

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
```

Both conditions must be True.

---

### What is Case Sensitivity?

Python treats uppercase and lowercase letters as different.

Example:

```
"Yes" is different from "yes"
```

To avoid errors:

```python
answer = input("Enter yes or no: ").lower()
```

`.lower()` converts input to lowercase.

---

### Type Conversion

When using:

```python
age = int(input())
```

`input()` always returns a string.

`int()` converts that string to an integer.

If the user enters text instead of a number, Python raises:

```
ValueError
```

---

## 4. Loops

### What Is a Loop?

A loop repeats a block of code multiple times.

Instead of writing the same code many times, we use loops.

---

## A. for Loop

### Definition

A `for` loop is used when the number of repetitions is known.

### Syntax

```python
for variable in range(n):
    # code block
```

### Example

```python
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

`range(5)` means numbers from 0 to 4.

---

## B. while Loop

### Definition

A `while` loop runs as long as a condition remains True.

It is used when we do not know in advance how many times the loop will run.

### Syntax

```python
while condition:
    # code block
```

### Example

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Important:
`count += 1` updates the variable.
If we do not update it, the loop may run forever.

---

## Loop Control Statements

| Keyword | Meaning |
|----------|----------|
| `break` | Stops the loop immediately |
| `continue` | Skips current iteration and moves to next |

### Example of break

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

Stops when `i` becomes 3.

---

## for vs while

| Feature | for Loop | while Loop |
|----------|-----------|-------------|
| Iterations known? | Yes | No |
| Based on | Range or collection | Condition |
| Common use | Fixed repetition | User interaction |

---

## 5. Lists

### What Is a List?

A list is a collection of multiple values stored in a single variable.

Example:

```python
fruits = ['apple', 'banana', 'cherry']
```

Each item has an index.

Indexing starts from 0.

```
apple -> index 0
banana -> index 1
cherry -> index 2
```

---

### Accessing Items

```python
print(fruits[0])
```

Output:
```
apple
```

---

### Common List Operations

#### Add Items

```python
fruits.append('orange')
```

`append()` adds item at the end.

---

#### Insert at Specific Position

```python
fruits.insert(1, 'grape')
```

---

#### Modify Item

```python
fruits[0] = 'pear'
```

---

#### Fixed Length List

```python
numbers = [0] * 5
```

Creates:
```
[0, 0, 0, 0, 0]
```

---

### Common Error

Accessing invalid index causes:

```
IndexError
```

---

## 6. Password Authentication Example

```python
password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Access Granted")
        break
    else:
        print("Incorrect password")
        attempts += 1

if attempts == max_attempts:
    print("Access Denied")
```

### Concepts Used

- while loop
- condition checking
- counter variable
- break statement

---

## 7. Simple Interactive Program

```python
while True:
    choice = input("Enter 1 to continue or 0 to exit: ")

    if choice == "1":
        print("Program running...")
    elif choice == "0":
        print("Exiting program.")
        break
    else:
        print("Invalid input.")
```

`while True` creates an infinite loop.
`break` is required to exit it.

---

## Best Practices

1. Normalize user input using `.lower()`
2. Avoid repeating code
3. Always update loop variables
4. Remember indexing starts from 0
5. Convert data types carefully
6. Debugging is part of learning

---

## Important Keywords Summary

| Keyword | Purpose |
|----------|----------|
| `if` | Start condition |
| `elif` | Additional condition |
| `else` | Default case |
| `for` | Fixed loop |
| `while` | Condition loop |
| `break` | Exit loop |
| `and` | Logical AND |
| `or` | Logical OR |
| `not` | Logical NOT |

---

## Practice Questions

1. Write a program that asks the user for a number and prints numbers from 1 to that number using a `for` loop.

2. Create a password system that allows only 2 attempts.

3. Ask the user to enter 5 numbers, store them in a list, and print the largest number.

---

## Further Exploration

- How to use `try` and `except` for proper error handling?
- What is the practical difference between `break` and `continue`?
- How can we automate file handling in Python?
- How do Python libraries extend automation?