class employee:
    auto_id = 1
    def __init__(self, name):
        self.id = employee.auto_id
        self.name = name 
        employee.auto_id += 1

    def delete_id(self):
        del self.id

    def delete_object(self):
        del self

    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")


emp = employee("coder")

emp.display()

emp.delete_id()

try:
    print(emp.id)
except AttributeError:
    print("ID not defined")

emp.delete_object()

try:
    emp.display()
except AttributeError:
    print("Object not defined")

