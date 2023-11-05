class Subject:

    def __init__(self, name, type, year): 
        self.name = name
        self.type = type
        self.year = year
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    


