

# Product
class Class():
    def get_details(self):
        pass

class Room():
    def room_info(self):
        pass

# Concrete Products
class Course(Class):
    def get_details(self):
        return 

class Laboratory(Class):
    def get_details(self):
        return 
    
class Seminar(Class):
    def get_details(self):
        return

class Event(Class):
    def get_details(self):
        return

class CourseRoom(Room):
    def room_info(self):
        return "Room 1"

class LaboratoryRoom(Room):
    def room_info(self):
        return "Room 2"

class SeminarRoom(Room):
    def room_info(self):
        return "Room 3"

class EventRoom(Room):
    def room_info(self):
        return "Room 2"

# Creator
class ClassCreator():
    def create_class(self):
        pass

    def create_room(self):
        pass

# Concrete Factory/Creator
class ClassFactory(ClassCreator):
    def create_class(class_type):
        if class_type == "Course":
            return Course(), CourseRoom()
        elif class_type == "Laboratory":
            return Laboratory(), LaboratoryRoom()
        elif class_type == "Seminar":
            return Seminar(), SeminarRoom()
        elif class_type == "Event":
            return Event(), EventRoom()
        else:
            raise ValueError("Invalid subject type.")
