class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        print(f"Employee name: {self.name}\nEmployee id: {self.emp_id}");

class Programmer(Employee):

    def showRole(self, role):
        self._role = role

paras = Programmer("Paras", "354626")
paras.showRole("Software Engineer")
print(paras._role)

tanuja = Programmer("Tanuja", "498325")
tanuja.showRole("CA")
print(tanuja._role)

satish = Employee("Satish", "248935")

