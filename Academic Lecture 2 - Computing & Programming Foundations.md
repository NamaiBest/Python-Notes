# Academic Lecture 2 - Computing & Programming Foundations

---

# 1. Overview of the Lecture

This lecture introduces the foundational concepts of computing and programming.

It covers:

- How computers work
- Hardware and software components
- Programming and programming languages
- IDEs and terminal usage
- Compiled vs interpreted languages
- Introduction to Python

The goal is to build a strong conceptual understanding before writing complex programs.

---

# 2. Understanding Computers: Machines That Follow Instructions

## 2.1 What is a Computer?

A computer is a machine that executes instructions exactly as given.

It does not think.
It does not understand meaning.
It only follows logical instructions.

If instructions are incorrect, the output will also be incorrect.

This is why programming requires precision.

---

## 2.2 CPU (Central Processing Unit)

The CPU is called the brain of the computer.

It is responsible for:
- Executing instructions
- Performing calculations
- Managing tasks

Every program you run sends instructions to the CPU.

Without the CPU, no processing happens.

---

## 2.3 RAM (Random Access Memory)

RAM is temporary memory.

It stores:
- Programs currently running
- Data being actively processed

RAM is fast but temporary.
When you turn off the computer, RAM data disappears.

Example:
When you open a browser, it loads into RAM.

---

## 2.4 Storage Devices (SSD / HDD)

Storage devices keep data permanently.

Examples:
- SSD (Solid State Drive)
- HDD (Hard Disk Drive)

They store:
- Operating system
- Installed software
- Documents
- Media files

Difference from RAM:
Storage is permanent.
RAM is temporary.

---

## 2.5 Input and Output Devices

Input devices:
- Keyboard
- Mouse
- Microphone

These send data into the computer.

Output devices:
- Monitor
- Printer
- Speakers

These display or output processed results.

---

# 3. Hardware vs Software

## 3.1 Hardware

Hardware refers to physical components.

Examples:
- CPU
- RAM
- Keyboard
- Monitor

You can physically touch hardware.

---

## 3.2 Software

Software is a set of instructions that tells hardware what to do.

Examples:
- Operating systems
- Applications (Spotify, Netflix, WhatsApp)
- Games

Software cannot exist without hardware.
Hardware cannot function properly without software.

They depend on each other.

---

# 4. Programming and Programs

## 4.1 What is a Program?

A program is a set of step-by-step instructions that tells a computer how to perform a task.

Example tasks:
- Playing music
- Sending messages
- Calculating numbers

---

## 4.2 What is Programming?

Programming is the process of writing those instructions using a programming language.

It involves:
- Logical thinking
- Problem solving
- Precision

---

## 4.3 Machine Language vs Programming Languages

Computers understand only binary:
0s and 1s.

Humans cannot easily write in binary.

Programming languages act as translators between humans and machines.

They convert human-readable code into machine language.

---

# 5. Programming Languages

Different languages are designed for different purposes.

| Language | Main Use |
|----------|----------|
| Python | AI, data science, automation, web |
| JavaScript | Web interactivity |
| C++ | High performance applications, games |
| SQL | Database querying |
| Java | Android applications |
| R | Statistical computing |

Each language has strengths and trade-offs.

---

# 6. Python: Features and Importance

## 6.1 Simple Syntax

Python code is readable and close to English.

This makes it beginner friendly.

---

## 6.2 Libraries and Frameworks

Python has powerful libraries:

- TensorFlow
- PyTorch
- NumPy
- Pandas

Libraries save time by providing pre-written functionality.

---

## 6.3 Versatility

Python is used in:

- Automation
- Artificial Intelligence
- Cybersecurity
- Web development
- Data analysis

---

## 6.4 Community Support

Python has a large global community.
This means:
- Many tutorials
- Documentation
- Problem-solving forums

---

# 7. Integrated Development Environment (IDE)

## 7.1 What is an IDE?

An IDE is software used to write and manage code.

It includes:
- Code editor
- Debugging tools
- Error highlighting
- Autocomplete

---

## 7.2 Examples of IDEs

- VS Code
- PyCharm
- Jupyter Notebook
- Atom
- Sublime Text

---

## 7.3 Benefits of IDEs

- Improves productivity
- Reduces syntax errors
- Organizes projects efficiently
- Provides debugging support

---

# 8. Terminal and Command Line Interface (CLI)

## 8.1 What is a Terminal?

A terminal is a text-based interface to interact with your operating system.

Instead of clicking, you type commands.

---

## 8.2 Common Commands

| Command | Purpose |
|----------|----------|
| mkdir | Create folder |
| cd | Change directory |
| cp | Copy files |
| ls | List files |
| clear | Clear terminal screen |

Terminal use is important for:
- Development workflows
- Git operations
- Server management

---

# 9. File System and File Extensions

## 9.1 File System

Files are organized inside folders (directories).

This hierarchical structure keeps data organized.

---

## 9.2 File Extensions

File extensions identify file type.

Examples:

- .txt → Text file
- .py → Python file
- .jpg → Image file
- .exe → Executable file

Extensions help the system decide how to open a file.

---

# 10. Compiled vs Interpreted Languages

## 10.1 Compiled Languages

Code is converted fully into machine language before execution.

Examples:
- C++
- Java (partially compiled)

Advantages:
- Faster execution
- Optimized performance

---

## 10.2 Interpreted Languages

Code is executed line by line.

Example:
- Python

Advantages:
- Easier debugging
- More flexible
- Faster development

---

## 10.3 Choosing Between Them

Use compiled languages when:
Performance is critical.

Use interpreted languages when:
Development speed and flexibility are important.

---

# 11. Programming Process

The general process of building software:

1. Understand the problem.
2. Create an algorithm (step-by-step solution).
3. Write code in chosen language.
4. Compile or interpret the code.
5. Execute and test.
6. Debug and improve.

---

# 12. Python Keywords

Python keywords are reserved words.

They cannot be used as variable names.

Complete list:

False      await      else       import     pass  
None       break      except     in         raise  
True       class      finally    is         return  
and        continue   for        lambda     try  
as         def        from       nonlocal   while  
assert     del        global     not        with  
async      elif       if         or         yield  

---

# Additional Python Notes

- Python is case sensitive.
- Comments start with `#`.
- Indentation defines blocks of code.
- Incorrect indentation causes errors.

---

# Final Summary

A computer system consists of:

Hardware + Software

Programming connects human logic with machine execution.

Understanding:
- Hardware
- Software
- Programming languages
- Tools like IDE and terminal

is essential before building advanced systems.

Python is widely used because of simplicity and power.

---

# Conceptual Questions

1. Why does a computer need programming languages instead of humans writing binary directly?
2. What is the difference between RAM and storage?
3. When would you choose a compiled language over an interpreted language?

---

# Step-by-Step Exercises

## Exercise 1: Identify Components

1. List 5 hardware components of your computer.
2. List 5 software applications you use daily.
3. Classify them as hardware or software.

---

## Exercise 2: File System Practice

1. Create a folder named `programming_intro`.
2. Inside it, create a file named `notes.txt`.
3. Create another file named `example.py`.
4. Identify their file extensions and what they represent.

---

## Exercise 3: Simple Python Execution

1. Open your IDE.
2. Create a file called `hello.py`.
3. Write:

   ```python
   print("Hello World")
   ```

4. Run the file.
5. Observe how the interpreter executes the code.

---
