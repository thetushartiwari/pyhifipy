# 🐍 Python Full Revision Workbook

## 📘 Overview

| Day | Topic                      | Focus                                             |
| --- | -------------------------- | ------------------------------------------------- |
| 0   | Foundations & Memory       | How Python executes code (Heap, Stack, Bytecode)  |
| 1   | Data Types & Variables     | Types, conversions, input/output, operators       |
| 2   | Control Flow & Loops       | Conditional logic, iterations, control statements |
| 3   | Functions, Scope & Modules | Defining, returning, importing, recursion         |
| 4   | Collections                | Lists, Tuples, Sets, Dictionaries                 |
| 5   | Strings & Regex            | Manipulation, pattern matching                    |
| 6   | File Handling & Exceptions | Read/write files, error handling                  |
| 7   | OOP (Classes & Objects)    | Encapsulation, inheritance, polymorphism          |
| 8   | Advanced Concepts          | Async, decorators, iterators, testing             |

---

## 🗓️ Day 0 – Foundations & Memory

### 🔹 Concept

Python is interpreted → converted to *bytecode* executed by the Python Virtual Machine.
Memory is managed automatically using **heap** (objects) and **stack** (function calls + references).

### 💻 Example

```python
x = 10          # Stored on Heap
y = x           # y points to same object
print(id(x), id(y))
```

*Both IDs are same → same memory object.*

### 🧠 Notes

* Variables are *names bound to objects*, not boxes storing data.
* Mutable (list, dict, set) vs Immutable (str, tuple, int).
* Garbage Collector frees unreferenced memory.

---

## 🗓️ Day 1 – Data Types & Variables

### 🔹 Core Types

int, float, str, bool, list, tuple, set, dict.

### 💻 Example

```python
x, y, z = 5, 3.14, "Hello"
print(type(x), type(z))
```

*Output:* `<class 'int'> <class 'str'>`

### 🔹 Type Casting & Input

```python
age = int(input("Enter age: "))
print(f"In 10 yrs: {age+10}")
```

### 🧠 Tips

* `input()` always returns string.
* Use `type()` & `isinstance()` to check type.
* Operators: `+ - * / // % **`.

---

## 🗓️ Day 2 – Control Flow & Loops

### 🔹 Conditionals

```python
n = -5
if n > 0: print("Positive")
elif n == 0: print("Zero")
else: print("Negative")
```

### 🔹 Loops

```python
for i in range(3): print(i)
# 0 1 2
```

```python
count = 3
while count > 0:
    print(count)
    count -= 1
# 3 2 1
```

### 🔹 break / continue

```python
for i in range(5):
    if i == 2: continue
    if i == 4: break
    print(i)
# 0 1 3
```

### 🧠 Use Tips

* `for` → known iterations / sequences.
* `while` → until condition fails.
* `break` → exit loop; `continue` → skip iteration.

---

## 🗓️ Day 3 – Functions, Scope & Modules

### 🔹 Defining Functions

```python
def add(a, b=0):
    return a + b
print(add(5, 3)) # 8
```

### 🔹 Scope

* Local (inside function)
* Global (defined outside)

```python
x = 10
def f(): print(x)
f()
```

### 🔹 Recursion

```python
def fact(n):
    return 1 if n<=1 else n*fact(n-1)
print(fact(5)) # 120
```

### 🔹 Modules

```python
import math
print(math.sqrt(16)) # 4.0
```

### 🧠 Tips

* Keep functions < 20 lines; 1 task only.
* `*args`, `**kwargs` → variable arguments.
* Always document (`"""docstring"""`).

---

## 🗓️ Day 4 – Collections (List, Tuple, Set, Dict)

### 🔹 Lists – Mutable

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits)
# ['apple','banana','cherry','mango']
```

### 🔹 Tuples – Immutable

```python
colors = ("red","green","blue")
print(colors[0]) # red
```

### 🔹 Sets – Unique & Unordered

```python
s = {1,2,2,3}
print(s)
# {1,2,3}
```

### 🔹 Dicts – Key:Value pairs

```python
student = {"name":"Alice","age":25}
student["grade"]="A"
print(student)
# {'name':'Alice','age':25,'grade':'A'}
```

### 🧠 Tips

* Use lists → ordered data.
* Use sets → remove duplicates.
* Use dicts → fast lookups by key.

---

## 🗓️ Day 5 – Strings & Regex

### 🔹 Strings

```python
text = "Python is fun"
print(text.upper()) # PYTHON IS FUN
print(text.replace("fun","powerful"))
```

### 🔹 Slicing

```python
s = "DataScience"
print(s[0:4]) # Data
print(s[-3:]) # nce
```

### 🔹 Regex (Basics)

```python
import re
txt = "My email is abc@xyz.com"
match = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+", txt)
print(match) # ['abc@xyz.com']
```

### 🧠 Tips

* `re.sub()` → replace pattern.
* `re.split()` → split on regex.
* Use for validation (e.g., email, phone).

---

## 🗓️ Day 6 – File Handling & Exceptions

### 🔹 File Read/Write

```python
with open("data.txt","w") as f:
    f.write("Hello World\n")

with open("data.txt","r") as f:
    print(f.read())
# Hello World
```

### 🔹 Try/Except

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("End")
# Cannot divide by zero → End
```

### 🧠 Tips

* Always use `with` for auto close.
* Catch specific exceptions.
* `try` > `if` checks for I/O errors.

---

## 🗓️ Day 7 – OOP (Classes & Objects)

### 🔹 Class Definition

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"I’m {self.name}, {self.age}")

s = Student("Tushar", 22)
s.intro()
# I’m Tushar, 22
```

### 🔹 Inheritance

```python
class Person: 
    def __init__(self, name): self.name = name
class Student(Person):
    def study(self): print(f"{self.name} is studying")

s = Student("Alice")
s.study()
```

### 🔹 Polymorphism

```python
class Dog: 
    def speak(self): print("Woof")
class Cat:
    def speak(self): print("Meow")

for a in (Dog(), Cat()): a.speak()
```

### 🧠 Notes

* Encapsulation: hide data (_variable).
* Abstraction: abc module for interfaces.
* Use OOP for real-world modeling.

---

## 🗓️ Day 8 – Advanced Concepts

### 🔹 Decorators

```python
def log(func):
    def wrapper(*a, **k):
        print("Calling:", func.__name__)
        return func(*a, **k)
    return wrapper

@log
def greet(): print("Hi")
greet()
# Calling: greet → Hi
```

### 🔹 Iterators & Generators

```python
def count_up_to(n):
    for i in range(1, n+1):
        yield i

for num in count_up_to(3): print(num)
# 1 2 3
```

### 🔹 Async Programming

```python
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(1)
    print("End")

asyncio.run(main())
# Start → (1 sec) → End
```

### 🔹 Testing

```python
def add(a,b): return a+b
def test_add(): assert add(2,3)==5
test_add()
```

### 🧠 Tips

* Use decorators for logging, timing.
* Use generators for large data processing.
* Async = non-blocking tasks.
* Always write unit tests for functions.
