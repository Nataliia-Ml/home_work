class Developer:
    def __init__(self, name, age, profile, salary):
        self.name = name
        self.age = age
        self.profile = profile
        self.salary = salary
        self.max_increase = self.calculate_max_increase()

    def calculate_max_increase(self):
        return self.salary * 0.1

    def salary_increase(self, increase_amount):
        if increase_amount > self.max_increase:
            return {'error': f"Max increase for person {self} is {self.max_increase}"}
        self.salary += increase_amount
        self.max_increase = self.calculate_max_increase()
        return {'msg': f"Increase {increase_amount} for person {self} done"}


class Junior(Developer):
    def __init__(self, name, age, profile, salary, mentor=None, plan=None):
        super().__init__(name, age, profile, salary)
        self.mentor = mentor
        self.plan = plan

    def add_mentor(self, mentor):
        self.mentor = mentor
        if self not in mentor.padavans:
            mentor.padavans.append(self)


class Senior(Developer):
    def __init__(self, name, age, profile, salary, padavans=None):
        super().__init__(name, age, profile, salary)
        self.padavans = list()
        if padavans is not None:
            self.padavans.append(padavans)

    def add_padavans(self, padavans):
        if padavans not in self.padavans:
            self.padavans.append(padavans)
            padavans.mentor = self


s = Senior("Bob", 18, "Python", 2800.0)
j1 = Junior("Fill", 19, "Python", 900)
j2 = Junior("Mary", 22, "Python", 900)


if __name__ == '__main__':
    j1.add_mentor(s)
    j1.add_mentor(s)
    s.add_padavans(j1)
    j2.add_mentor(s)
    s.add_padavans(j2)
    print(f"List of padavans for mentor {s.name} is {[self.name for self in s.padavans]}")
    print(f"Mentor for {j1.name} is {j1.mentor.name}")
    print(f"Mentor for {j2.name} is {j2.mentor.name}")
