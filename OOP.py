#object is type of class but not part of class

class Employee:
    name = ""
    dept = ""
    role = ""

    def show_details(self):
        print(self.name)
        print(self.dept)
        print(self.role)

emp1 = Employee()
emp1.name = "Bahaa"
emp1.dept = "IT"
emp1.role ="Software eng"
emp1.show_details()