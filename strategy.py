# Teacher class
class Teacher:
    def __init__(self, name, idd, subject):
        self.name = name
        self.idd = idd
        self.subject = subject

# Classroom class
class Classroom:
    def __init__(self, name):
        self.name = name

# Strategy interface
class TimetableStrategy:
    def show_timetable(self, obj):
        pass

# Concrete strategies
class ScheduleOptimizationTeacher(TimetableStrategy):
    def optimize_schedule(self, teacher):
        return f"Optimizing schedule for teacher {teacher.name}"

class ScheduleOptimizationClassroom(TimetableStrategy):
    def optimize_schedule(self, classroom):
        return f"Optimizing schedule for classroom {classroom.name}"

# Context
class ScheduleOptimizer:
    def __init__(self, strategy):
        self.strategy = strategy

    def optimize_schedule(self, obj):
        return self.strategy.optimize_schedule(obj)

# Usage
if __name__ == '__main__':
    teacher = Teacher("John Doe", 123, "Math")
    classroom = Classroom("Math Classroom")
    teacher_optimizer = ScheduleOptimizer(ScheduleOptimizationTeacher())
    classroom_optimizer = ScheduleOptimizer(ScheduleOptimizationClassroom())
    print(teacher_optimizer.optimize_schedule(teacher))
    print(classroom_optimizer.optimize_schedule(classroom))
