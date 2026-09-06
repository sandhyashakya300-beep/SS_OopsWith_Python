#Overloading 

class Vector() :
    def __init__(self, i,j,k) :
        self.i = i
        self.j = j
        self.k = k

    def __str__(self) :
        return f"{self.i}i+ {self.j}j+ {self.k}k"

#Ask the user for inputs 
user_1 = int(input("Enter the value for i: "))
user_2 = int(input("Enter the value for j: "))
user_3 = int(input("Enter the value for k: "))

v = Vector(user_1, user_2, user_3)

print(v)
