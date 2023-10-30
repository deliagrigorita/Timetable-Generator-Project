#Teacher class
class Teacher:
    def __init__(self, name, idd, subject):
        self.name = name
        self.idd = idd
        self.subject = subject

#Classroom class
class Classroom:
    def __init__(self, name):
        self.name = name

# Strategy interface
class TimetableStrategy():
    
    def show_timetable(self, teacher):
        pass

# Concrete strategies
class ScheduleOptimizationTeacher(TimetableStrategy):
    def optimize_schedule(self, Teacher):
        return 
    
class ScheduleOptimizationClassroom(TimetableStrategy):
    def optimize_schedule(self, Classroom):
        return 
    

#Context
class ScheduleOptimizer:
    def optimize_schedule(self, teacher):
        return self.strategy.optimize_schedule(teacher)
    def optimize_schedule(self, classroom):
        return self.strategy.optimize_schedule(classroom)

# Usage
if __name__ == '__main__':
    teacher = Teacher("John Doe")
    optimizer = ScheduleOptimizer(ScheduleOptimizationTeacher())
    print(optimizer.optimize_schedule(teacher))
