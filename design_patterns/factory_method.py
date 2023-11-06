# Product
class Class:
    def get_details(self):
        pass

class Room:
    def room_info(self):
        pass

# Concrete Products
class Course(Class):
    def get_details(self):
        return "This is a course."

class Laboratory(Class):
    def get_details(self):
        return "This is a laboratory."

class Seminar(Class):
    def get_details(self):
        return "This is a seminar."

class Event(Class):
    def get_details(self):
        return "This is an event."

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
        return "Room 4"

# Creator
class ClassCreator:
    def create_class(self, class_type):
        pass

    def create_room(self, room_type):
        pass

# Concrete Factory/Creator
class ClassFactory(ClassCreator):
    def create_class(self, class_type):
        if class_type == "Course":
            return Course()
        elif class_type == "Laboratory":
            return Laboratory()
        elif class_type == "Seminar":
            return Seminar()
        elif class_type == "Event":
            return Event()
        else:
            raise ValueError("Invalid subject type.")

    def create_room(self, room_type):
        if room_type == "Course":
            return CourseRoom()
        elif room_type == "Laboratory":
            return LaboratoryRoom()
        elif room_type == "Seminar":
            return SeminarRoom()
        elif room_type == "Event":
            return EventRoom()
        else:
            raise ValueError("Invalid room type.")

# Usage
if __name__ == '__main__':
    factory = ClassFactory()
    course, course_room = factory.create_class("Course"), factory.create_room("Course")
    print(course.get_details())
    print(course_room.room_info())
