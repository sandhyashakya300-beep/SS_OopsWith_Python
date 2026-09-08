# Vector Representation Script

## Overview
This repository contains `overload.py`, a simple Python script that demonstrates fundamental Object-Oriented Programming (OOP) concepts. Specifically, it showcases how to define a custom class, initialize attributes, and overload the string representation magic method (`__str__`) to format object output.

## Features
- **Custom `Vector` Class**: Models a mathematical 3D vector with `i`, `j`, and `k` components.
- **Method Overloading**: Utilizes the `__str__` dunder (magic) method to provide a clean, readable string format for the vector object (e.g., `3i+ 4j+ 5k`).
- **Interactive Prompts**: Asks the user to dynamically input integer values for the vector's components via the command line.

## Prerequisites
- Python 3.x installed on your machine.

## Usage
1. Clone the repository or download the `overload.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script using the following command:
   ```bash
   python overload.py
   ```

## Example Interaction
```text
Enter the value for i: 5
Enter the value for j: 8
Enter the value for k: 2
5i+ 8j+ 2k
```

## Code Analysis
- **`__init__(self, i, j, k)`**: The constructor initializes the vector's coordinates based on user input.
- **`__str__(self)`**: This method is overridden to change how the `Vector` object is printed. Instead of printing the default memory address, it returns a formatted string resembling standard vector notation.
