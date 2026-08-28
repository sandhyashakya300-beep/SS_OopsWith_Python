# 🐍 Class Methods in Python

A beginner-friendly Python example demonstrating the difference between **instance methods** and **class methods**.

This project uses an `Employee` class to show how a class variable can be accessed through an instance method and modified using a `@classmethod`.

---

## 📌 Overview

This example demonstrates:

* Python classes
* Class variables
* Instance attributes
* Instance methods
* Class methods
* The `self` parameter
* The `cls` parameter
* The `@classmethod` decorator
* Modifying class-level data

---

## 🐍 Example Code

```python
class Employee:
    company_name = "TechCorp"

    def show(self):
        print(f"Company: {self.company_name}")

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name


e1 = Employee()

e1.name = "tesla"

e1.show()

e1.change_company_name("InnoTech")

e1.show()

print(Employee.company_name)
```

The original code defines `company_name` at the class level, uses `show()` as an instance method, and uses `change_company_name()` as a class method.

---

# 🧠 What Is a Class Method?

A **class method** is a method that works with the class itself rather than a particular instance.

It is created using the `@classmethod` decorator:

```python
@classmethod
def change_company_name(cls, new_name):
    cls.company_name = new_name
```

The first parameter of a class method is conventionally named `cls`.

Here:

```python
cls
```

refers to the `Employee` class.

Therefore:

```python
cls.company_name = new_name
```

changes the class-level `company_name`.

---

# 🏗️ Understanding the `Employee` Class

The class contains:

```python
class Employee:
    company_name = "TechCorp"
```

`company_name` is a **class variable**.

It belongs to the class and is shared by instances unless an instance provides its own attribute with the same name.

Initially:

```text
Employee.company_name
        ↓
    "TechCorp"
```

---

# 1️⃣ Instance Method

The `show()` method is an instance method:

```python
def show(self):
    print(f"Company: {self.company_name}")
```

Instance methods receive the instance through the `self` parameter.

When the code executes:

```python
e1.show()
```

`self` refers to:

```text
e1
```

The method then accesses:

```python
self.company_name
```

and prints the company name.

---

# 2️⃣ Class Method

The following method is a class method:

```python
@classmethod
def change_company_name(cls, new_name):
    cls.company_name = new_name
```

The `@classmethod` decorator tells Python that this method should receive the class as its first argument.

Here:

```python
cls
```

refers to:

```text
Employee
```

So:

```python
cls.company_name = new_name
```

is effectively modifying:

```python
Employee.company_name
```

The source uses this method to change the company name to `"InnoTech"`.

---

# 🔄 How the Program Works

The program first creates an `Employee` object:

```python
e1 = Employee()
```

Then it assigns an instance attribute:

```python
e1.name = "tesla"
```

This creates:

```text
e1.name
   ↓
"tesla"
```

However, this `name` attribute is not used by the `show()` method. The `show()` method uses `company_name` instead.

---

## Step 1 — Initial Company Name

Initially:

```python
Employee.company_name
```

is:

```text
TechCorp
```

Therefore:

```python
e1.show()
```

prints:

```text
Company: TechCorp
```

---

## Step 2 — Change the Company Name

The code calls:

```python
e1.change_company_name("InnoTech")
```

Although the method is called through `e1`, it is a class method.

It receives the `Employee` class as `cls` and executes:

```python
cls.company_name = "InnoTech"
```

Therefore:

```python
Employee.company_name
```

becomes:

```text
InnoTech
```

---

## Step 3 — Display the Updated Name

The program then calls:

```python
e1.show()
```

Again, the method accesses:

```python
self.company_name
```

and now the result is:

```text
Company: InnoTech
```

Finally:

```python
print(Employee.company_name)
```

also prints:

```text
InnoTech
```

The sequence of calls is present in the original source.

---

# 📊 Instance Method vs Class Method

| Feature                  | Instance Method   | Class Method         |
| ------------------------ | ----------------- | -------------------- |
| Decorator                | None required     | `@classmethod`       |
| First parameter          | `self`            | `cls`                |
| Works primarily with     | Instance          | Class                |
| Can access instance data | Yes               | Not directly         |
| Can access class data    | Yes               | Yes                  |
| Common use               | Instance behavior | Class-level behavior |

---

# 🔍 `self` vs `cls`

Understanding the difference between `self` and `cls` is important.

### `self`

`self` represents the **current object/instance**.

Example:

```python
def show(self):
    print(self.company_name)
```

When:

```python
e1.show()
```

is called:

```text
self → e1
```

---

### `cls`

`cls` represents the **class itself**.

Example:

```python
@classmethod
def change_company_name(cls, new_name):
    cls.company_name = new_name
```

When called on `Employee`:

```text
cls → Employee
```

Therefore:

```python
cls.company_name
```

refers to the class-level attribute.

---

# 🧩 Class Variable vs Instance Variable

The example contains:

```python
company_name = "TechCorp"
```

which is a class variable.

It also creates:

```python
e1.name = "tesla"
```

which is an instance variable.

### Class Variable

```python
Employee.company_name
```

belongs to the class.

### Instance Variable

```python
e1.name
```

belongs specifically to the `e1` object.

Conceptually:

```text
Employee
│
└── company_name = "TechCorp"

e1
│
├── name = "tesla"
│
└── accesses company_name
```

---

# ⚠️ Important Observation

The line:

```python
e1.name = "tesla"
```

does not affect the output of `show()` because `show()` uses:

```python
self.company_name
```

rather than:

```python
self.name
```

So changing:

```python
e1.name
```

## does not change the displayed company name.

# 📂 Project Structure

```text
.
├── clsmethod(1).py
└── README.md
```

For a cleaner GitHub repository, you may want to rename the Python file to something like:

```text
class_methods.py
```

This avoids spaces and parentheses in the filename.

---

# ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project

```bash
cd <repository-name>
```

### 3. Run the Python file

```bash
python "clsmethod(1).py"
```

If you rename the file:

```bash
python class_methods.py
```

---

# 💻 Expected Output

Based on the current code, the output follows this sequence:

```text
Company: TechCorp
Company: InnoTech
InnoTech
```

The company name changes from `TechCorp` to `InnoTech` through the class method.

---

# 🎯 Learning Objectives

After studying this example, you should understand:

* What an instance method is
* What a class method is
* How `@classmethod` works
* The difference between `self` and `cls`
* What class variables are
* What instance variables are
* How class-level data can be modified
* How an instance can call a class method

---

# 🚀 Practice Ideas

Try extending the `Employee` class.

### Add an Employee Name

Modify `show()` so that it displays both the employee and company:

```python
def show(self):
    print(f"Employee: {self.name}")
    print(f"Company: {self.company_name}")
```

### Add Another Class Method

Create a class method that displays the current company:

```python
@classmethod
def show_company(cls):
    print(cls.company_name)
```

### Create Multiple Employees

Try:

```python
e1 = Employee()
e2 = Employee()
e3 = Employee()
```

Then change the company name using the class method and observe what happens to all instances.

---

# 🔑 Key Takeaway

The main concept demonstrated by this project is:

> **Instance methods work with individual objects, while class methods work with class-level data and receive the class through `cls`.**

In this example:

```python
show(self)
```

works with an instance, while:

```python
change_company_name(cls, new_name)
```

changes the shared class-level `company_name`.

---

# 🛠️ Technologies Used

* 🐍 Python 3

---

# 📚 Conclusion

This example provides a simple introduction to one of the important concepts in Python object-oriented programming: **class methods**.

Understanding the difference between:

```python
self
```

and:

```python
cls
```

is an important step toward working confidently with Python classes, class variables, inheritance, and object-oriented design.

**Happy Coding! 🐍**
