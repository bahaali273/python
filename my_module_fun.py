def calc_salary(basic, inc, ded):
    return basic+inc-ded

def calc_hr(hours, rate):
    return hours *rate

class Student:
    def __init__(self,name,major):
        self.name=name
        self.major= major

    def show_data(self):
        print(self.name)
        print(self.major)