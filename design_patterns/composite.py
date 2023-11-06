class Class:
    schedule = None

    def __init__(self, name, type): 
        self.name = name
        self.type = type
    

    def set_name(self, name):
        self.name = name


    def set_type(self, type):
        self.type = type


    def set_schedule(self, schedule):
        self.schedule = schedule


    def getAvailability(self, other):
        if self.schedule.day == other.day and self.schedule.start_time == other.start_time and self.schedule.end_time == other.end_time:
            return False
        return True


# Composite Component
class Schedule:
    def __init__(self, day, start_time, end_time):
        self.day = day 
        self.start_time = start_time
        self.end_time = end_time   
        self.classes = [] 


    def add(self, component):
        self.classes.append(component)


    def remove(self, component):
        self.classes.remove(component)


    def getAvailability(self):
        for class_it in self.classes:
            is_available = class_it.getAvailability(self)
            print("Schedule = " + str(self.day) + ", " + str(self.start_time) + ", " +  str(self.end_time) + 
                  " is available on class " + class_it.name + ": " + str(is_available))


# Usage
if __name__ == "__main__":
    class_obj = Class("Metode formale", "Laborator")
    
    schedule     = Schedule("Monday", "08:00", "10:00")
    newSchedule1 = Schedule("Monday", "08:00", "10:00")
    newSchedule2 = Schedule("Friday", "08:00", "10:00")

    class_obj.set_schedule(schedule)
    newSchedule1.add(class_obj)
    newSchedule2.add(class_obj)

    newSchedule1.getAvailability()
    newSchedule2.getAvailability()

