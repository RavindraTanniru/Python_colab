# PYTHON
Python coding practise and  Execution.... using google colab 

# Python – Theory + Examples 

> Concise theory with runnable examples. Each section ends with **Further reading** links to GeeksforGeeks.

## Table of Contents

* [Introduction](#introduction)
* [Install & Run](#install--run)
* [Basics: Syntax, Variables, Types](#basics-syntax-variables-types)
* [Operators](#operators)
* [Control Flow](#control-flow)
* [Functions](#functions)
* [Data Structures](#data-structures)
* [Strings](#strings)
* [Modules & Packages](#modules--packages)
* [File I/O](#file-io)
* [Exceptions](#exceptions)
* [Object-Oriented Programming](#object-oriented-programming)
* [Iterables, Iterators & Generators](#iterables-iterators--generators)
* [Comprehensions](#comprehensions)
* [Decorators & Context Managers](#decorators--context-managers)
* [Virtual Environments & pip](#virtual-environments--pip)
* [Standard Library Highlights](#standard-library-highlights)
* [Testing](#testing)
* [Typing (Type Hints)](#typing-type-hints)
* [Next Steps](#next-steps)

---

## Introduction

**Theory:** Python is a high‑level, dynamically typed language focused on readability and productivity. Indentation defines blocks; everything is an object; batteries‑included standard library.

**Example:**

```python
print("Hello, Python!")
```

**Further reading:**

* GeeksforGeeks – Python Tutorial: [https://www.geeksforgeeks.org/python/python-programming-language-tutorial/](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/)
* GeeksforGeeks – Python Basics: [https://www.geeksforgeeks.org/python/python-basics/](https://www.geeksforgeeks.org/python/python-basics/)

---

## Install & Run

**Theory:**

* Install from python.org or via package managers.
* Use `python --version`; run files with `python file.py`.
* Use REPL for quick experiments; prefer virtualenv per project.

**Example (Windows/macOS/Linux):**

```bash
python --version
python -c "print('ok')"
```

**Further reading:**

* GfG – Install and Setup Python: [https://www.geeksforgeeks.org/how-to-install-python-on-windows/](https://www.geeksforgeeks.org/how-to-install-python-on-windows/)

---

## Basics: Syntax, Variables, Types

**Theory:**

* Indentation (PEP 8 recommends 4 spaces).
* Variables are names bound to objects; no explicit declarations.
* Core types: `int`, `float`, `bool`, `str`, `None`.

**Example:**

```python
x = 10      # int
pi = 3.14   # float
ok = True   # bool
msg = "hi"  # str
print(type(pi).__name__)
```

**Further reading:**

* GfG – Python Basics: [https://www.geeksforgeeks.org/python/python-basics/](https://www.geeksforgeeks.org/python/python-basics/)

---

## Operators

**Theory:** arithmetic `+ - * / // % **`, comparison, logical `and or not`, membership `in`, identity `is`.

**Example:**

```python
assert 7 // 3 == 2
assert 2 ** 3 == 8
assert 'py' in 'python'
```

**Further reading:**

* GfG – Operators in Python: [https://www.geeksforgeeks.org/python-operators/](https://www.geeksforgeeks.org/python-operators/)

---

## Control Flow

**Theory:** `if/elif/else`, `for` loops iterate over iterables, `while` repeats until condition fails. `break`, `continue`, `else` on loops.

**Example:**

```python
for n in range(5):
    if n % 2:
        continue
    print(n)
else:
    print("finished")
```

**Further reading:**

* GfG – Loops and Control Statements: [https://www.geeksforgeeks.org/loops-in-python/](https://www.geeksforgeeks.org/loops-in-python/)

---

## Functions

**Theory:** defined with `def`, return values implicitly `None` if not returned. Default args, keyword args, `*args`, `**kwargs`, annotations.

**Example:**

```python
def greet(name: str, /, *, excited: bool = False) -> str:
    msg = f"Hello, {name}"
    return msg + "!" if excited else msg

print(greet("Ravi", excited=True))
```

**Further reading:**

* GfG – Functions in Python: [https://www.geeksforgeeks.org/python-functions/](https://www.geeksforgeeks.org/python-functions/)

---

## Data Structures

**Theory:**

* List (mutable), Tuple (immutable), Set (unique items), Dict (key→value).
* Time complexities vary; choose accordingly.

**Example:**

```python
nums = [1, 2, 3]
nums.append(4)
point = (10, 20)
unique = {1, 2, 2, 3}
phone = {"alice": "+91-123", "bob": "+91-456"}
```

**Further reading:**

* GfG – Python Data Structures: [https://www.geeksforgeeks.org/python/python-data-structures/](https://www.geeksforgeeks.org/python/python-data-structures/)

---

## Strings

**Theory:** immutable sequences; rich methods; f‑strings for formatting; slicing.

**Example:**

```python
s = "Geeks for Python"
print(s.lower())
print(s.split())
print(f"{len(s)=}")
print(s[::-1])  # reverse
```

**Further reading:**

* GfG – Python Strings: [https://www.geeksforgeeks.org/python-strings/](https://www.geeksforgeeks.org/python-strings/)

---

## Modules & Packages

**Theory:** reuse via modules (`.py` files) and packages (dirs with `__init__.py`). Use `import name as alias`.

**Example:**

```python
# mymath.py
PI = 3.14159

def area(r):
    return PI * r * r

# main.py
import mymath as mm
print(mm.area(2))
```

**Further reading:**

* GfG – Modules in Python: [https://www.geeksforgeeks.org/python-modules/](https://www.geeksforgeeks.org/python-modules/)

---

## File I/O

**Theory:** use context managers; text vs binary; encoding.

**Example:**

```python
from pathlib import Path
p = Path("note.txt")
with p.open("w", encoding="utf-8") as f:
    f.write("Hello file!\n")
print(p.read_text(encoding="utf-8"))
```

**Further reading:**

* GfG – File Handling: [https://www.geeksforgeeks.org/file-handling-python/](https://www.geeksforgeeks.org/file-handling-python/)

---

## Exceptions

**Theory:** use `try/except/else/finally`; raise custom exceptions.

**Example:**

```python
class NegativeError(ValueError):
    pass

def sqrt_nonneg(x: float) -> float:
    if x < 0:
        raise NegativeError("x must be non-negative")
    return x ** 0.5

try:
    sqrt_nonneg(-1)
except NegativeError as e:
    print("error:", e)
```

**Further reading:**

* GfG – Exceptions in Python: [https://www.geeksforgeeks.org/errors-and-exceptions-in-python/](https://www.geeksforgeeks.org/errors-and-exceptions-in-python/)

---

## Object-Oriented Programming

**Theory:** classes encapsulate data+behavior; `__init__`, methods, inheritance, dunder methods; dataclasses reduce boilerplate.

**Example:**

```python
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float

class Cart:
    def __init__(self):
        self.items: list[Item] = []
    def add(self, item: Item):
        self.items.append(item)
    def total(self) -> float:
        return sum(i.price for i in self.items)

c = Cart(); c.add(Item("Book", 199.0))
print(c.total())
```

**Further reading:**

* GfG – OOP in Python: [https://www.geeksforgeeks.org/python-oops-concepts/](https://www.geeksforgeeks.org/python-oops-concepts/)

---

## Iterables, Iterators & Generators

**Theory:** iterator protocol `__iter__`/`__next__`; generators with `yield`; lazy evaluation.

**Example:**

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(list(countdown(3)))
```

**Further reading:**

* GfG – Generators in Python: [https://www.geeksforgeeks.org/generators-in-python/](https://www.geeksforgeeks.org/generators-in-python/)

---

## Comprehensions

**Theory:** concise list/set/dict builders; optional conditions; faster than loops for simple transforms.

**Example:**

```python
squares = [n*n for n in range(6) if n % 2 == 0]
lookup = {c: ord(c) for c in "abc"}
unique = {c.upper() for c in "hello"}
```

**Further reading:**

* GfG – List/Dict Comprehension: [https://www.geeksforgeeks.org/python-list-comprehension/](https://www.geeksforgeeks.org/python-list-comprehension/)

---

## Decorators & Context Managers

**Theory:** decorators wrap callables; context managers manage setup/teardown (`with`).

**Example:**

```python
import time

def timing(fn):
    def wrapper(*a, **k):
        t0 = time.perf_counter()
        try:
            return fn(*a, **k)
        finally:
            print(f"{fn.__name__} took {time.perf_counter()-t0:.6f}s")
    return wrapper

@timing
def heavy():
    sum(range(1000000))

heavy()
```

**Further reading:**

* GfG – Decorators in Python: [https://www.geeksforgeeks.org/decorators-in-python/](https://www.geeksforgeeks.org/decorators-in-python/)
* GfG – Context Managers: [https://www.geeksforgeeks.org/context-manager-in-python/](https://www.geeksforgeeks.org/context-manager-in-python/)

---

## Virtual Environments & pip

**Theory:** isolate dependencies per project; `pip` installs packages from PyPI.

**Example:**

```bash
python -m venv .venv
# activate
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install requests
pip freeze > requirements.txt
```

**Further reading:**

* GfG – Virtual Environments: [https://www.geeksforgeeks.org/python-virtual-environment/](https://www.geeksforgeeks.org/python-virtual-environment/)
* GfG – pip in Python: [https://www.geeksforgeeks.org/how-to-install-pip-on-windows/](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)

---

## Standard Library Highlights

**Theory:** modules for common tasks: `pathlib`, `datetime`, `collections`, `itertools`, `functools`, `json`, `re`.

**Example:**

```python
from collections import Counter
from itertools import permutations
print(Counter("banana"))
print(next(permutations([1,2,3], 2)))
```

**Further reading:**

* GfG – Python Modules: [https://www.geeksforgeeks.org/python-modules/](https://www.geeksforgeeks.org/python-modules/)

---

## Testing

**Theory:** use `unittest` or `pytest`; structure tests as small, deterministic functions.

**Example (pytest‑style):**

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

**Further reading:**

* GfG – Unit Testing in Python: [https://www.geeksforgeeks.org/unit-testing-python-unittest/](https://www.geeksforgeeks.org/unit-testing-python-unittest/)

---

## Typing (Type Hints)

**Theory:** optional static typing via annotations; tools like `mypy` check types.

**Example:**

```python
from typing import Iterable

def total(values: Iterable[int]) -> int:
    return sum(values)
```

**Further reading:**

* GfG – Type Hints: [https://www.geeksforgeeks.org/type-hints-in-python/](https://www.geeksforgeeks.org/type-hints-in-python/)

---

## Next Steps

* Practice problems (DSA with Python), build small projects, read code.

**Further reading:**

* GfG – Python DSA Guide: [https://www.geeksforgeeks.org/dsa/python-data-structures-and-algorithms/](https://www.geeksforgeeks.org/dsa/python-data-structures-and-algorithms/)

---

> **License/Attribution Note:** This README text and code examples are original and paraphrased. Links are provided to relevant GeeksforGeeks articles for deeper study.
