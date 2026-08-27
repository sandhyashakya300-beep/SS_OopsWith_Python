#Understanding class methods in Python
# Instance Methods Vs class methods in python

class Employee:
    company_name = "TechCorp"

    def show(self):
        print(f"Company: {self.company_name}")

    @classmethod
    def change_company_name(cls, new_name):
            cls.company_name = new_name

e1 = Employee()
e1.name ="tesla"
e1.show()
e1.change_company_name("InnoTech")
e1.show()
print(Employee.company_name)