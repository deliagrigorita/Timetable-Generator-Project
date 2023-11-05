class Class:
    schedule = None

    def __init__(self):
        pass

    def __init__(self, name, type, classroom, teacher, year, group): 
        self.name = name
        self.type = type
        self.classroom = classroom
        self.teacher = teacher
        self.year = year
        self.group = group

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_classroom(self, classroom):
        self.classroom = classroom

    def get_classroom(self):
        return self.classroom
    
    def set_teacher(self, teacher):
        self.teacher = teacher

    def get_teacher(self):
        return self.teacher
    
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year
    
    def set_group(self, group):
        self.group = group

    def get_group(self):
        return self.group
    
    def set_schedule(self, schedule):
        self.schedule = schedule

    