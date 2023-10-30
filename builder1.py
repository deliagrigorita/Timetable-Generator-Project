# Product: Subject
class Subject:
    def __init__(self, name,teacher,room,resource):
        self.name = name
        self.teacher = teacher
        self.room = room 
        self.resource = resource

# Builder interface
class SubjectBuilder:
    def set_name(self, name):
        pass

    def set_teacher(self, teacher):
        pass

    def set_room(self, room):
        pass

    def set_resource(self, resource):
        pass

# Concrete Builder 
class ConcreteSubjectBuilder(SubjectBuilder):
    def __init__(self):
        self.subject = Subject()

    def set_name(self, name):
        self.subject.name = name

    def set_teacher(self, teacher):
        self.subject.teacher = teacher

    def set_room(self, room):
        self.subject.room = room

    def set_resource(self, resource):
        self.subject.resource = resource

    def get_subject(self):
        return self.subject

# Director
class SubjectDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_subject(self, name, teacher, room, resource):
        self.builder.set_name(name)
        self.builder.set_teacher(teacher)
        self.builder.set_room(room)
        self.builder.set_resource(resource)
        return self.builder.get_subject()

# Usage
if __name__ == '__main__':
    concrete_subject_builder = ConcreteSubjectBuilder()  
    director = SubjectDirector(concrete_subject_builder)  
    subject = director.construct_subject("OOP", "MR ?", "Room C413", "Projector")  
    
