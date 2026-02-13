# Academic Lecture 3 - Terminal & Version Control
Terminal and Git Fundamentals 

---

# 1. Terminal (Command Line) Fundamentals

## 1.1 What is a Terminal?

A terminal is a text-based interface that allows users to interact directly with the operating system by typing commands.

Unlike a Graphical User Interface (GUI), where users click icons and buttons, the terminal requires written instructions.

In simple terms:
The terminal is a direct communication channel between you and your computer.

When you type a command, the operating system interprets it and performs the requested action.

---

## 1.2 Why is the Terminal Important?

The terminal is important because:

- Many servers operate without graphical interfaces.
- Most cloud systems run on Linux environments.
- Automation is easier through terminal commands.
- Advanced system configuration is often done through command line tools.
- Developers frequently use terminal-based tools such as Git.

Real-world meaning:
If you work in software development, DevOps, cybersecurity, or cloud computing, you will use the terminal regularly.

---

## 1.3 Understanding Directories and File Systems

A directory is simply another word for a folder.

Operating systems organize files in a hierarchical structure.

Example structure:

```
Home/
 ├── Documents/
 ├── Downloads/
 └── Projects/
```

Each folder can contain:
- Files
- Other folders

This structure is called a file system hierarchy.

---

## 1.4 Core Terminal Commands (Unix-Based Systems)

| Command | Description | Real Meaning |
|----------|------------|--------------|
| `pwd` | Print working directory | Show where you are |
| `ls` | List contents | Show what is here |
| `cd <folder>` | Change directory | Go inside folder |
| `cd ..` | Move up | Go back one level |
| `mkdir <name>` | Make directory | Create new folder |
| `rm <file>` | Remove file | Delete file |
| `touch <file>` | Create empty file | Make blank file |

---

### Example Usage

Check current location:

```bash
pwd
```

List files:

```bash
ls
```

Move into folder:

```bash
cd Projects
```

Go back:

```bash
cd ..
```

---

## 1.5 File Creation and Editing

Create file:

```bash
touch notes.txt
```

Write into file:

```bash
echo "Hello World" > notes.txt
```

Open file in basic editor:

```bash
nano notes.txt
```

---

## 1.6 Common Terminal Mistakes

- Deleting files without checking location
- Spelling commands incorrectly
- Forgetting case sensitivity
- Not understanding current directory

Always verify location before deletion:

```bash
pwd
ls
```

---

# 2. Version Control and Git

## 2.1 What is Version Control?

Version control is a system that tracks changes to files over time.

It allows you to:
- Restore previous versions
- Track who made changes
- Collaborate safely

Real-world analogy:
It is like having a history log for your project.

If something breaks, you can go back to a previous working version.

---

## 2.2 What is Git?

Git is a distributed version control system.

Distributed means:
Every developer has a complete copy of the project history.

Git tracks:
- File modifications
- Additions
- Deletions
- Commit history

---

## 2.3 Repository (Repo)

A repository is a folder tracked by Git.

When you run:

```bash
git init
```

Git creates a hidden folder called `.git`.

This folder stores:
- Project history
- Commit records
- Branch information

---

## 2.4 The Three Areas in Git

Git operates in three main areas:

1. Working Directory  
   Your actual project files.

2. Staging Area  
   Temporary area where changes are prepared.

3. Repository (Commit History)  
   Permanent record of saved snapshots.

Flow:

Working Directory → Staging Area → Commit

---

## 2.5 What is a Commit?

A commit is a saved snapshot of staged changes.

Each commit contains:
- A unique identifier (hash)
- Author information
- Timestamp
- Commit message

Commit messages should describe:
What was changed and why.

Example:

```bash
git commit -m "Added login validation logic"
```

---

## 2.6 What is a Branch?

A branch is a parallel version of your project.

It allows you to:
- Develop new features
- Fix bugs
- Experiment safely

Without affecting the main project.

Branches are merged later.

---

## 2.7 Basic Git Commands Explained

| Command | Purpose | Practical Meaning |
|----------|----------|------------------|
| `git init` | Initialize repository | Start tracking project |
| `git status` | Show file status | Check what changed |
| `git add <file>` | Stage file | Prepare for commit |
| `git commit -m "msg"` | Save snapshot | Record changes |
| `git --version` | Check version | Confirm Git installed |

---

## 2.8 Basic Development Workflow

Step 1: Create or modify files  
Step 2: Check status  

```bash
git status
```

Step 3: Add changes  

```bash
git add filename
```

Step 4: Commit changes  

```bash
git commit -m "Description"
```

Repeat this cycle during development.

---

## 2.9 Why Git is Powerful

Git allows:

- Safe experimentation
- Collaboration
- Backup
- Project history tracking
- Error recovery

It prevents permanent loss of work.

---

# 3. GitHub (Introduction)

GitHub is a cloud-based hosting platform for Git repositories.

It enables:

- Remote backup
- Collaboration
- Code review
- Issue tracking

GitHub does not replace Git.
It uses Git internally.

---

# 4. Best Practices

- Commit frequently.
- Write meaningful commit messages.
- Avoid committing unnecessary files.
- Understand what you stage before committing.
- Practice terminal usage daily.

---

# 5. Important Key Terms

| Term | Explanation |
|-------|------------|
| Terminal | Text interface for system interaction |
| Directory | Folder in file system |
| Repository | Git-tracked project |
| Staging Area | Temporary pre-commit area |
| Commit | Saved snapshot |
| Branch | Parallel development path |
| Version Control | Tracking changes over time |
| GitHub | Remote hosting platform |

---

# Conceptual Questions

1. What problem does version control solve in software development?
2. What is the difference between the working directory and staging area?
3. Why is the terminal important for cloud and server environments?

---

# Step-by-Step Exercises

## Exercise 1: Terminal Navigation

1. Open terminal.
2. Create folder named `terminal_practice`.
   ```
   mkdir terminal_practice
   ```
3. Enter the folder.
   ```
   cd terminal_practice
   ```
4. Create a file.
   ```
   touch example.txt
   ```
5. Confirm with:
   ```
   ls
   ```

---

## Exercise 2: Initialize Git

1. Inside the folder, run:
   ```
   git init
   ```
2. Check status:
   ```
   git status
   ```
3. Add file:
   ```
   git add example.txt
   ```
4. Commit:
   ```
   git commit -m "Initial commit"
   ```

---

## Exercise 3: Modify and Track Changes

1. Add content to `example.txt`.
2. Save file.
3. Run:
   ```
   git status
   ```
4. Stage changes.
   ```
   git add example.txt
   ```
5. Commit again.
   ```
   git commit -m "Updated example file"
   ```

Observe how Git tracks multiple commits.