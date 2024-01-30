class Employee:

  def __init__(self, name,dept, role):
      self.name = name
      self.dept = dept
      self.role = role

    def show_details(self):
        print(self.name)
        print(self.dept)
        print(self.role)

emp1 = Employee("Alaa","IT","Software eng")
emp1.show_details()