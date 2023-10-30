import datetime

# Class (Publisher)
class Class:
    exam_date = None

    def __init__(self, name, type): 
        self.name = name
        self.type = type
        self._observers = []


    def set_name(self, name):
        self.name = name


    def set_type(self, type):
        self.type = type


    def notify(self, modifier = None): 
        for observer in self._observers:
            if modifier != observer:
                observer.update()
        

    def attach(self, observer): 
        if observer not in self._observers:
            self._observers.append(observer)


    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass


    def set_exam_date(self, new_exam_date):
        if new_exam_date is not None and not self.has_exam_date():  
            self.exam_date = new_exam_date
            self.notify()
        else:
            print("Error: Exam date cannot be None")


    def has_exam_date(self):
        return self.exam_date is not None


# Notification (Subscriber)
class Notification:
    def __init__(self, title, message): 
        self.title = title
        self.message = message

    def update(self):
        print('Notification: Title: ' + str(self.title) + ', Message: '+str(self.message))


# Usage
if __name__ == '__main__':
    class_obj = Class("Metode formale", "Laborator")
    notif1 = Notification("Exam", "Exam date has been posted!")

    class_obj.attach(notif1)
    class_obj.set_exam_date(datetime.datetime(2023, 1, 23))

