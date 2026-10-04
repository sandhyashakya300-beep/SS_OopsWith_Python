class Calculator:
    def __init__(self):
        # Initialize an attribute to store calculation history (Object State)
        self.history = []

    def add(self, a, b):
        result = a + b
        self._save_to_history(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self._save_to_history(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self._save_to_history(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero."
        result = a / b
        self._save_to_history(f"{a} / {b} = {result}")
        return result

    # A 'private' method meant only for internal use (Encapsulation)
    def _save_to_history(self, operation):
        self.history.append(operation)

    def show_history(self):
        if not self.history:
            print("No calculations performed yet.")
        else:
            print("Calculation History:")
            for item in self.history:
                print(item)


# --- Using the Calculator Object ---

# 1. Create an instance (Object) of the Calculator
my_calc = Calculator()

# 2. Call methods on the object
print("Addition:", my_calc.add(10, 5))        
print("Subtraction:", my_calc.subtract(20, 8)) 
print("Multiplication:", my_calc.multiply(4, 3))
print("Division:", my_calc.divide(15, 0))      

print("-" * 20)

# 3. Access the object's specific state
my_calc.show_history()