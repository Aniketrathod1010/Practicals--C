class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0
        self.address = ""

    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def display_data(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = ""

    def get_data(self):
        super().get_data()
        self.department = input("Enter department: ")

    def display_data(self):
        super().display_data()
        print("Department:", self.department)
        print("-------------------------")


managers = []

for i in range(10):
    print(f"\nEnter details for Manager {i+1}")
    m = Manager()
    m.get_data()
    managers.append(m)

print("\n--- Manager Details ---")
for m in managers:
    m.display_data()
