# 🐍 Python Decorators

A beginner-friendly Jupyter Notebook demonstrating how **Python decorators** can modify or extend the behavior of functions without changing their original implementation.

The notebook contains three practical decorator examples:

1. ⏱️ Timing function execution
2. 🐞 Debugging function calls
3. 💾 Caching function return values

---

## 📌 Overview

This project is designed to understand the fundamentals of Python decorators through simple, practical examples.

The notebook demonstrates:

* Function decorators
* Nested functions
* `*args`
* `**kwargs`
* Higher-order functions
* Function execution timing
* Function-call debugging
* Dictionary-based caching concepts
* The `@decorator` syntax

---

## 📂 Project Structure

```text
.
├── decorators.ipynb
└── README.md
```

---

# 🧠 What Is a Decorator?

A decorator is a function that takes another function as an argument and returns a new function with additional behavior.

A typical decorator looks like:

```python
def decorator_function(fun):
    def wrapper(*args, **kwargs):
        # Additional behavior
        return fun(*args, **kwargs)

    return wrapper
```

The decorator can then be applied using:

```python
@decorator_function
def my_function():
    pass
```

This is equivalent to:

```python
my_function = decorator_function(my_function)
```

---

# 1️⃣ Timing Function Execution

The first example creates a `timer` decorator to measure how long a function takes to execute.

```python
import time

def timer(fun):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = fun(*args, **kwargs)

        end = time.time()

        print(f"{fun.__name__} ran in {end-start} time ")

        return result

    return wrapper
```

The decorator is applied to:

```python
@timer
def sleep_fun(n):
    time.sleep(n)
```

The function is then called with:

```python
sleep_fun(2)
```

The function intentionally pauses for approximately two seconds using `time.sleep()`. The decorator records the time before and after the function call and prints the elapsed time.

---

## 🔍 How the Timer Decorator Works

The execution flow is:

```text
sleep_fun(2)
      │
      ▼
   wrapper()
      │
      ├── Record start time
      │
      ├── Execute sleep_fun()
      │
      ├── Record end time
      │
      └── Print execution time
```

The important idea is that the original `sleep_fun()` function does not contain timing logic.

The decorator adds that functionality externally.

---

# 2️⃣ Debugging Function Calls

The second example creates a `debug` decorator.

Its purpose is to print the function name and the arguments passed to it whenever the decorated function is called.

```python
def debug(fun):
    def wrapper(*args, **kwargs):
        args_value = ' ,'.join(str(args) for args in args)

        kwargs_value = ' ,'.join(
            f"{k}={v}" for k, v in kwargs.items()
        )

        print(
            f"calling: {fun.__name__} "
            f"with args {args_value} "
            f"and kwargs {kwargs_value}"
        )

        return fun(*args, **kwargs)

    return wrapper
```

---

## Example: `hello()`

The decorator is applied to:

```python
@debug
def hello():
    print("hello , guys ")
```

When:

```python
hello()
```

is executed, the decorator prints information about the function call before executing the original function.

---

## Example: `greet()`

The notebook also decorates a function with both positional and default arguments:

```python
@debug
def greet(name, greeting="Nice to meet you"):
    print(f"{greeting},{name}")
```

It is called using:

```python
greet("William")
```

This demonstrates how:

```python
*args
```

and:

```python
**kwargs
```

can be forwarded from the decorator to the original function.

---

# 🔑 Understanding `*args` and `**kwargs`

The decorators use:

```python
def wrapper(*args, **kwargs):
```

This allows the wrapper to accept different types and numbers of arguments.

### `*args`

Collects positional arguments.

Example:

```python
greet("William")
```

The value `"William"` can be received through `args`.

### `**kwargs`

Collects keyword arguments.

For example:

```python
greet(name="William", greeting="Hello")
```

The keyword arguments can be accessed through `kwargs`.

This makes the decorator reusable with functions that have different argument structures.

---

# 3️⃣ Caching Function Results

The third example introduces the concept of caching.

The notebook creates a `cache` decorator:

```python
def cache(fun):
    cache_value = {}

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]

        result = fun(*args)

        return result

    return wrapper
```

The intention is to avoid executing an expensive function again when the same arguments are provided.

The decorated function is:

```python
@cache
def long_running(a, b):
    time.sleep(2)
    return a * b
```

The function intentionally waits for two seconds before returning the multiplication result.

It is called with:

```python
print(long_running(6, 3))
print(long_running(5, 4))
```

---

# ⚠️ Important: Cache Implementation Is Incomplete

The notebook's comment says the decorator should:

> cache the return value of the function so that the cached value is returned instead of executing the function again.

However, the current implementation does not actually save the result.

It creates:

```python
cache_value = {}
```

and checks:

```python
if args in cache_value:
    return cache_value[args]
```

but after calculating:

```python
result = fun(*args)
```

it immediately returns:

```python
return result
```

without doing:

```python
cache_value[args] = result
```

Therefore, repeated calls with the same arguments would still execute the function again.

---

## ✅ How the Cache Would Normally Store the Result

The missing operation would conceptually be:

```python
cache_value[args] = result
```

The complete logic would therefore be:

```python
def cache(fun):
    cache_value = {}

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]

        result = fun(*args)

        cache_value[args] = result

        return result

    return wrapper
```

This corrected version is provided only to explain the intended caching mechanism; the notebook itself does not contain this assignment.

---

# 🔄 Decorator Execution Flow

The three examples follow the same fundamental pattern:

```text
Original Function
       │
       ▼
   Decorator
       │
       ▼
    Wrapper
       │
       ▼
Additional Behavior
       │
       ▼
Original Function
```

For example:

```text
@timer
   │
   ▼
sleep_fun()
   │
   ▼
wrapper()
   │
   ├── Start timer
   ├── Run function
   ├── Stop timer
   └── Display execution time
```

---

# 📊 Decorators Demonstrated

| Decorator | Purpose                               | Main Concept        |
| --------- | ------------------------------------- | ------------------- |
| `timer`   | Measures execution time               | `time.time()`       |
| `debug`   | Displays function calls and arguments | `*args`, `**kwargs` |
| `cache`   | Demonstrates result caching           | Dictionary lookup   |

---

# 🧩 Important Python Concepts

## Higher-Order Functions

Decorators are based on the idea that functions can be passed around like other Python objects.

For example:

```python
def decorator(fun):
    ...
```

Here, `fun` receives another function.

---

## Nested Functions

The decorators define an inner function:

```python
def wrapper(*args, **kwargs):
    ...
```

The wrapper can access the function received by the outer decorator.

---

## Returning Functions

Each decorator returns its wrapper:

```python
return wrapper
```

This is what allows the wrapper to replace the original function.

---

## `@` Syntax

The notebook uses:

```python
@timer
```

and:

```python
@debug
```

and:

```python
@cache
```

This provides a convenient syntax for applying decorators to functions.

---

# 🛠️ Technologies Used

* 🐍 Python 3
* 📓 Jupyter Notebook
* ⏱️ Python `time` module
* 🗂️ Python dictionaries

The `time` module used by the examples is part of Python's standard library, so no separate installation is required for it.

---

# ▶️ How to Run

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

## 2. Navigate to the Repository

```bash
cd <repository-name>
```

## 3. Install Jupyter

```bash
pip install jupyter
```

## 4. Start Jupyter Notebook

```bash
jupyter notebook
```

## 5. Open the Notebook

Open:

```text
decorators.ipynb
```

Run the cells individually to explore each decorator example.

---

# 🎯 Learning Objectives

After completing this notebook, you should understand:

* What Python decorators are
* How decorators modify function behavior
* How wrapper functions work
* How `*args` and `**kwargs` are used
* How to measure function execution time
* How to debug function calls using decorators
* How dictionaries can be used for caching
* How the `@decorator` syntax works
* How functions can be passed as arguments
* How functions can return other functions

---

# 🚀 Practice Ideas

After completing the notebook, try building your own decorators.

### 1. Logging Decorator

Create a decorator that prints:

```text
Function started
Function completed
```

---

### 2. Authentication Decorator

Create a simple decorator that checks whether a user is authorized before calling a function.

---

### 3. Retry Decorator

Create a decorator that attempts to execute a function multiple times if it fails.

---

### 4. Improved Cache Decorator

Complete the cache implementation so repeated calls with identical arguments return the stored result.

---

### 5. Execution Counter

Create a decorator that counts how many times a function has been called.

Example:

```text
Function called 1 time
Function called 2 times
Function called 3 times
```

---

# 📝 Project Notes

This notebook is intended as a **learning exercise** rather than a production-ready decorator library.

The examples intentionally use simple implementations so that the underlying concepts are easy to understand.

In particular, the `cache` example demonstrates the **idea of caching**, but its current implementation does not persist calculated results in the cache dictionary.

---

# 🔑 Key Takeaway

Python decorators allow you to add functionality to existing functions without modifying the function's core implementation.

The three examples demonstrate this idea in different ways:

```text
             Python Decorators
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      Timer       Debug       Cache
        │           │           │
        ▼           ▼           ▼
   Execution     Function     Return
     Time          Calls       Values
```

The fundamental pattern is:

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        # Add functionality
        result = function(*args, **kwargs)
        # Add functionality
        return result

    return wrapper
```

> **Decorators provide a clean and reusable way to extend function behavior without changing the original function itself.**

---

## ⭐ Keep Learning

Experiment with the decorators, modify the wrapper functions, and create your own decorators to understand how Python's functional programming features work.

**Happy Coding! 🐍**
