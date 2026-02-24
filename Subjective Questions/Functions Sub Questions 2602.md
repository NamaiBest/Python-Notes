# Python: Functions & Modularity (Subjective)

## Question

You are building a mini student grade analyzer for a classroom system that processes student scores, evaluates performance, and generates a summary report.

---

## Task 1 — Process the Scores

Write a function `process_scores(students)` that:
- Accepts a dictionary where:
  - Keys = student names
  - Values = list of integer scores
- Calculates average score (rounded to 2 decimal places)
- Returns a new dictionary of averages

---

## Task 2 — Classify the Grades

Write a function `classify_grades(averages)` that:
- Takes output of Task 1
- Assigns letter grades:

| Average | Grade |
|----------|--------|
| 90 and above | A |
| 75 – 89 | B |
| 60 – 74 | C |
| Below 60 | F |

Return format:

```python
{
    "name": (average, grade)
}
```

Use local threshold variables inside the function.

---

## Task 3 — Generate the Report

Write a function:

```python
generate_report(classified, passing_avg=70)
```

It should:
- Print formatted student report
- Track pass count
- Return number of students passed

### Sample Output Format

```
===== Student Grade Report =====
Alice      Avg: 86.25 | Grade: B | Status: PASS
Bob        Avg: 62.50 | Grade: C | Status: PASS
Clara      Avg: 95.25 | Grade: A | Status: PASS
=================================
Total Students : 3
Passed         : 3
Failed         : 0
```

---

## Complete Solution

```python
def process_scores(students):
    averages = {}
    for name, scores in students.items():
        averages[name] = round(sum(scores) / len(scores), 2)
    return averages


def classify_grades(averages):
    thresholds = {"A": 90, "B": 75, "C": 60}
    classified = {}

    for name, avg in averages.items():
        if avg >= thresholds["A"]:
            grade = "A"
        elif avg >= thresholds["B"]:
            grade = "B"
        elif avg >= thresholds["C"]:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified


def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    passed = 0

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed += 1

        print(f"{name:<10} Avg: {avg:<6} | Grade: {grade} | Status: {status}")

    total = len(classified)
    print("=" * 33)
    print(f"{'Total Students':<15}: {total}")
    print(f"{'Passed':<15}: {passed}")
    print(f"{'Failed':<15}: {total - passed}")

    return passed


if __name__ == "__main__":
    students = {
        "Alice": [85, 92, 78, 90],
        "Bob": [60, 55, 70, 65],
        "Clara": [95, 98, 100, 92]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    total_passed = generate_report(classified)

    print(f"\nFinal Count — Students who passed: {total_passed}")
```

---

# Python: Files & JSON (Subjective)

## Working with Files and JSON

### Given Starter File: `inventory.json`

```json
[
    {"title": "The Alchemist", "author": "Paulo Coelho", "price": 12.99, "in_stock": true},
    {"title": "1984", "author": "George Orwell", "price": 9.99, "in_stock": true}
]
```

New book to add:

```python
new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}
```

---

## Complete Solution

```python
import json

new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# Task 1: Read inventory
with open('inventory.json', 'r') as f:
    inventory = json.load(f)

print(f"Total books: {len(inventory)}")

# Task 2: Append and save
inventory.append(new_book)

with open('inventory.json', 'w') as f:
    json.dump(inventory, f, indent=4)

# Task 3: Display inventory
with open('inventory.json', 'r') as f:
    updated_inventory = json.load(f)

for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")
```

---

# Python: Loops & Automation (Subjective)

## Weekly Temperature Analysis

---

## Task 1: Find Maximum and Minimum

Requirements:
- Use loop
- Do not use `max()` or `min()`

```python
print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

highest = temperatures[0]
lowest = temperatures[0]

for temp in temperatures:
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

print(f"Highest Temperature: {highest}°C")
print(f"Lowest Temperature: {lowest}°C")
```

---

## Task 2: Count Hot Days

Requirements:
- Use loop
- Use `continue`
- Count days > 30°C

```python
print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days = 0

for temp in temperatures:
    if temp <= 30:
        continue
    hot_days += 1

print(f"Hot Days (>30°C): {hot_days}")
```

---

## Task 3: Alert System

Requirements:
- Stop when temperature ≥ 40°C
- Use `break`
- Count hot days before alert

```python
print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days = 0
day_number = 0

for temp in temperatures:
    day_number += 1

    if temp >= 40:
        print(f"Hot Days before alert: {hot_days}")
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day_number}")
        break

    if temp > 30:
        hot_days += 1
```

---