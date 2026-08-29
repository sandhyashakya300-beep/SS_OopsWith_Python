# 🐍 Object-Oriented Programming in Python

A beginner-friendly Jupyter Notebook covering the fundamental concepts of **Object-Oriented Programming (OOP) in Python**.

This project uses practical `Car` and `ElectricCar` examples to demonstrate how classes, objects, inheritance, encapsulation, polymorphism, static methods, properties, and multiple inheritance work in Python.

---

## 📌 Overview

The notebook covers:

* Classes and Objects
* Constructors with `__init__`
* Instance attributes
* Instance methods
* Inheritance
* `super()`
* Encapsulation
* Private attributes
* Getter methods
* Polymorphism
* Class variables
* Static methods
* `@property` decorators
* `isinstance()`
* Multiple inheritance

---

## 📂 Project Structure

```text
.
├── Oops_concept.ipynb
└── README.md
```

---

# 🧠 OOP Concepts Covered

## 1. Classes and Objects

The notebook begins with a basic `Car` class:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

An object is then created:

```python
my_car = Car("Toyota", "Corolla")
```

The object's attributes can be accessed using:

```python
my_car.brand
my_car.model
```

The notebook produces:

```text
My car is a Toyota Corolla
```

This introduces the relationship between a **class** and an **object**.

---

# 2. Constructors — `__init__`

The `__init__()` method initializes an object when it is created.

```python
def __init__(self, brand, model):
    self.brand = brand
    self.model = model
```

When this is executed:

```python
Car("Toyota", "Corolla")
```

Python creates a `Car` object and initializes its attributes.

The notebook uses `__init__()` throughout the examples.

---

# 3. Inheritance

The notebook demonstrates inheritance by creating an `ElectricCar` class that inherits from `Car`:

```python
class ElectricCar(Car):
```

The child class adds a new attribute:

```python
self.battery_size = battery_size
```

and uses:

```python
super().__init__(brand, model)
```

to initialize the attributes inherited from `Car`.

### Example

```python
my_tesla = ElectricCar("Tesla", "Model s", 100)

print(my_tesla.battery_size)
print(my_tesla.full_name())
```

Output:

```text
100
Tesla Model s
```

The `ElectricCar` object can use methods inherited from `Car`, such as `full_name()`.

---

# 4. `super()`

The notebook uses:

```python
super().__init__(brand, model)
```

inside `ElectricCar`.

This allows the child class to call the constructor of its parent class.

Conceptually:

```text
ElectricCar
     │
     │ super()
     ▼
   Car.__init__()
     │
     ▼
brand + model initialized
```

This avoids duplicating the initialization logic from the parent class.

---

# 5. Encapsulation

The notebook introduces **encapsulation** by making the `brand` attribute private:

```python
self.__brand = brand
```

The double underscore indicates that the attribute is intended to be accessed through the class's interface.

A getter method is provided:

```python
def get_brand(self):
    return self.__brand + "!"
```

This allows the brand to be retrieved through a method rather than directly accessing the private attribute.

Example:

```python
my_car = Car("Toyota", "Corolla")

print(my_car.get_brand())
```

Output:

```text
Toyota!
```

---

# 6. Polymorphism

The notebook demonstrates **polymorphism** by defining the same method, `fuel_type()`, in both `Car` and `ElectricCar`.

In `Car`:

```python
def fuel_type(self):
    return "Petrol or Diesel"
```

In `ElectricCar`:

```python
def fuel_type(self):
    return " Electric Charge"
```

The same method name produces different behavior depending on the object.

Example:

```python
my_car = Car("Toyota", "Corolla")
my_tesla = ElectricCar("Tesla", "Model s", 100)

print(my_car.fuel_type())
print(my_tesla.fuel_type())
```

Output:

```text
Petrol or Diesel
 Electric Charge
```

This is an example of **method overriding**.

---

# 7. Class Variables

The notebook demonstrates a class variable that keeps track of the number of cars created:

```python
class Car:
    total_cars = 0
```

The constructor increments the value whenever a new object is created:

```python
Car.total_cars += 1
```

The notebook creates three `Car` objects:

```python
my_car = Car("Toyota", "Corolla")
safari = Car("Land Rover", "Defender")
safari2 = Car("BMW", "X5")
```

and then displays:

```text
Total cars created : 3
3
```

This demonstrates how a class variable can store data shared at the class level.

---

# 8. Static Methods

The notebook introduces a static method using the `@staticmethod` decorator:

```python
@staticmethod
def general_description():
    return " Cars are means of transportation that run on roads and are powered by engines."
```

A static method does not require `self` or `cls`.

It can be called through an object:

```python
my_car.general_description()
```

or directly through the class:

```python
Car.general_description()
```

Both calls are demonstrated in the notebook.

Output:

```text
 Cars are means of transportation that run on roads and are powered by engines.
 Cars are means of transportation that run on roads and are powered by engines.
```

---

# 9. Property Decorator

The notebook demonstrates the `@property` decorator to expose the private `model` attribute through a getter:

```python
@property
def model(self):
    return self.__model
```

The model is stored privately:

```python
self.__model = model
```

and accessed using:

```python
my_car.model
```

rather than:

```python
my_car.model()
```

The notebook also includes a commented-out assignment:

```python
# my_car.model = "New model"
```

which illustrates the intended read-only behavior of the property because only a getter is provided.

---

# 10. `isinstance()`

The notebook demonstrates the built-in `isinstance()` function:

```python
my_tesla = ElectricCar("Tesla", "Model s", 100)

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
```

Output:

```text
True
True
```

This happens because `ElectricCar` inherits from `Car`.

Therefore, an `ElectricCar` object is also considered an instance of `Car`.

Conceptually:

```text
ElectricCar
     │
     └── inherits from Car

my_tesla
   │
   ├── isinstance(my_tesla, ElectricCar) → True
   └── isinstance(my_tesla, Car)         → True
```

---

# 11. Multiple Inheritance

The final major example demonstrates **multiple inheritance**.

Two independent classes are created:

```python
class Battery:
    def Battery_info(self):
        return "this is a battery "
```

and:

```python
class Engine:
    def Engine_info(self):
        return "this is engine"
```

The notebook then creates:

```python
class ElectricCar2(Battery, Engine, Car):
    pass
```

This means `ElectricCar2` inherits from three classes:

```text
        Battery
           │
           │
Engine ────┼──── ElectricCar2
           │
           │
          Car
```

The object can access methods from both `Battery` and `Engine`:

```python
my_New_tesla = ElectricCar2("Tesla", "Model s")

print(my_New_tesla.Battery_info())
print(my_New_tesla.Engine_info())
```

Output:

```text
this is a battery
this is engine
```

The multiple-inheritance example is implemented directly in the notebook.

---

# 📊 OOP Concepts at a Glance

| #  | Concept              | Demonstrated With       |
| -- | -------------------- | ----------------------- |
| 1  | Class                | `Car`                   |
| 2  | Object               | `my_car`                |
| 3  | Constructor          | `__init__()`            |
| 4  | Instance attributes  | `brand`, `model`        |
| 5  | Instance methods     | `full_name()`           |
| 6  | Inheritance          | `ElectricCar(Car)`      |
| 7  | `super()`            | Parent initialization   |
| 8  | Encapsulation        | `__brand`, `__model`    |
| 9  | Getter               | `get_brand()`           |
| 10 | Polymorphism         | `fuel_type()`           |
| 11 | Class variable       | `total_cars`            |
| 12 | Static method        | `general_description()` |
| 13 | Property             | `@property`             |
| 14 | Type checking        | `isinstance()`          |
| 15 | Multiple inheritance | `ElectricCar2`          |

---

# 🔄 OOP Concepts Relationship

The examples build on one another:

```text
Class & Object
      ↓
Constructor
      ↓
Instance Methods
      ↓
Inheritance
      ↓
Encapsulation
      ↓
Polymorphism
      ↓
Class Variables
      ↓
Static Methods
      ↓
Properties
      ↓
isinstance()
      ↓
Multiple Inheritance
```

This makes the notebook useful as a progression through fundamental Python OOP concepts.

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
Oops_concept.ipynb
```

Run each cell individually to explore the examples.

---

# 🎯 Learning Objectives

After completing this notebook, you should understand:

* What Object-Oriented Programming is
* How to create classes
* How to create objects
* How constructors work
* How instance attributes work
* How instance methods work
* How inheritance works
* How `super()` is used
* What encapsulation means
* How private attributes are represented
* How getter methods work
* What polymorphism means
* How method overriding works
* What class variables are
* How static methods work
* How `@property` works
* How `isinstance()` checks object types
* How multiple inheritance works

---

# 🚀 Practice Ideas

After studying the notebook, try extending the examples.

### Create a New Vehicle Class

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
```

Then create:

```python
class Car(Vehicle):
    pass
```

---

### Add a New Electric-Car Method

Try adding:

```python
def charge(self):
    return "Charging battery..."
```

to `ElectricCar`.

---

### Add a Setter Property

The current notebook demonstrates a property getter. Try adding a setter:

```python
@model.setter
def model(self, value):
    self.__model = value
```

This will allow the model to be changed through the property.

---

### Experiment With Polymorphism

Create another vehicle class with its own:

```python
fuel_type()
```

method and compare the results.

---

### Experiment With Multiple Inheritance

Create another class such as:

```python
class GPS:
    def navigation(self):
        return "Navigation enabled"
```

Then experiment with inheriting from:

```python
class SmartCar(Car, GPS):
    pass
```

---

# 📝 Important Notes

This repository is intended for **learning and practicing Python OOP concepts**.

The notebook contains several independent versions of the `Car` and `ElectricCar` classes. Each example focuses on a different OOP concept, so the class definitions are intentionally repeated and modified between examples.
The examples are educational demonstrations rather than production-ready vehicle-management software.

---

# 🛠️ Technologies Used

* 🐍 Python 3
* 📓 Jupyter Notebook

The notebook metadata indicates that it was created using a Python 3 kernel and records Python version `3.13.4`.

---

# 📚 Key Takeaway

Object-Oriented Programming allows us to organize programs around **objects that contain data and behavior**.

This notebook demonstrates the progression from a simple class:

```python
class Car:
    ...
```

to more advanced concepts such as:

```python
class ElectricCar(Car):
    ...
```

```python
@staticmethod
```

```python
@property
```

and:

```python
class ElectricCar2(Battery, Engine, Car):
    ...
```

The most important OOP concepts demonstrated are:

> **Classes → Objects → Encapsulation → Inheritance → Polymorphism → Abstraction through interfaces/properties → Reusable object-oriented design**

---

## ⭐ Keep Learning

Explore each example, modify the classes, create your own objects, and experiment with different inheritance relationships.

**Happy Coding! 🐍**
