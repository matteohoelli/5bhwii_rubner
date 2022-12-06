class Person:
    def __init__(self, name, gender, department):
        self.name = name
        self.gender = gender
        self.department = department


class Employee(Person):
    def __init__(self, name, gender, department, company):
        super().__init__(name, gender, department)
        self.company = company


class Group_leader(Employee):
    def __init__(self, name, gender, department, company):
        super().__init__(name, gender, department, company)


class Department:
    def __init__(self, name, count_m):
        self.name = name
        self.count_m = count_m


class Company:
    def __init__(self, description):
        self.description = description
        self.employee = []
        self.group_leader = []
        self.departments = []

    def count_employee(self):
        count = 0
        for i in self.employee:
            count += 1
        return count

    def count_group_leader(self):
        count = 0
        for i in self.group_leader:
            count += 1
        return count

    def count_departments(self):
        count = 0
        for i in self.departments:
            count += 1
        return count

    def employee_count_highest(self):
        count_m_last = 0
        highest = 0
        for i in self.departments:
            if (i.count_m > count_m_last):
                highest = i.name
                count_m_last = i.count_m
        return highest

    def pro_fm(self):
        count_empl = 0
        for i in self.departments:
            count_empl += i.count_m
        man = 0
        woman = 0
        for j in self.employee:
            if (j.gender == "m"):
                man += 1
            else:
                woman += 1
        for j in self.group_leader:
            if (j.gender == "m"):
                man += 1
            else:
                woman += 1
        return "Men:", man * 100 // count_empl, "Women:", woman * 100 // count_empl


ie = Department("economy", 1)
mec = Department("mechanical engineering", 2)
company = Company("fire department absam")
ep1 = Employee("Franz", "m", ie, company)
ep2 = Employee("Frieda", "w", mec, company)
gl1 = Group_leader("Martin", "m", ie, company)

company.employee.append(ep1)
company.employee.append(ep2)
company.group_leader.append(gl1)
company.departments.append(ie)
company.departments.append(mec)

print("count of employees:", company.count_employee())
print("count of group_leaders:", company.count_group_leader())
print("count of departments:", company.count_departments())
print("department with highest count of employees:", company.employee_count_highest())
print("percentage man und woman (in %):", company.pro_fm())
