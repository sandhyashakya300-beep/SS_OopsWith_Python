# Calculator – Python OOP Project

## 📌 Project Overview

This project implements a simple calculator using **Object-Oriented Programming (OOP)** in Python.

The `Calculator` class supports four basic arithmetic operations:

* Addition
* Subtraction
* Multiplication
* Division

It also maintains a **calculation history**, demonstrating object state and encapsulation through a private-style helper method.

## ✨ Features

* Addition of two numbers
* Subtraction of two numbers
* Multiplication of two numbers
* Division of two numbers
* Division-by-zero error handling
* Stores performed calculations in history
* Displays calculation history
* Demonstrates Python classes, objects, methods, attributes, and encapsulation

## 🧠 OOP Concepts Demonstrated

### 1. Class and Object

The `Calculator` class defines the calculator's behavior and state. An object is created using:

```python
my_calc = Calculator()
```

### 2. Object State

The constructor initializes a `history` list to store previous calculations:

```python
self.history = []
```

### 3. Methods

The calculator provides methods for arithmetic operations:

```python
add()
subtract()
multiply()
divide()
```

Each successful operation returns its result and saves the calculation to the history.

### 4. Encapsulation

The `_save_to_history()` method is intended for internal use:

```python
def _save_to_history(self, operation):
    self.history.append(operation)
```

The leading underscore communicates that the method is an internal implementation detail.

## 🔢 Supported Operations

| Operation      | Method           | Example        |
| -------------- | ---------------- | -------------- |
| Addition       | `add(a, b)`      | `10 + 5 = 15`  |
| Subtraction    | `subtract(a, b)` | `20 - 8 = 12`  |
| Multiplication | `multiply(a, b)` | `4 × 3 = 12`   |
| Division       | `divide(a, b)`   | `15 / 5 = 3.0` |

The `divide()` method checks whether the second number is zero and returns an error message instead of performing the division.

## 📜 Calculation History

Successful calculations are stored in the calculator's `history` list.

The `show_history()` method displays the stored operations. If no calculations have been performed, it prints:

```text
No calculations performed yet.
```

Otherwise, it prints the calculation history.

## 📂 Project Structure

```text
.
├── calculator.py
└── README.md
```

## ⚙️ Requirements

* Python 3.x
* No external libraries are required.

## 🚀 How to Run

1. Install Python 3.x.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run:

```bash
python calculator.py
```

## 💻 Example Usage

The current program creates a `Calculator` object and tests the arithmetic methods:

```python
my_calc = Calculator()

print("Addition:", my_calc.add(10, 5))
print("Subtraction:", my_calc.subtract(20, 8))
print("Multiplication:", my_calc.multiply(4, 3))
print("Division:", my_calc.divide(15, 0))

my_calc.show_history()
```

The division example intentionally uses `0` as the divisor to demonstrate the built-in division-by-zero check.

## 🎯 Learning Objectives

This project helps practice:

* Python classes and objects
* Constructors using `__init__`
* Instance attributes
* Instance methods
* Returning values from methods
* Conditional statements
* Lists and list operations
* f-strings
* Input validation
* Basic encapsulation
* Maintaining object state

## 🔮 Possible Improvements

The current project could be extended with:

* A menu-driven user interface
* User input for calculations
* Power and modulo operations
* Square-root functionality
* A method to clear calculation history
* More robust exception handling
* Unit tests
* A graphical user interface (GUI)

## 👩‍💻 Author

**Sandhya Shakya**

GitHub: `sandhyashakya300-beep`

## 📄 License

This project is intended for learning and educational purposes.
