import unittest

from classes.Class import Class
from classes.Schedule import Schedule
from classes.Teacher import Teacher
from classes.Subject import Subject

class TestClass(unittest.TestCase):

    def test_set_schedule(self):
        # Arrange
        schedule = Schedule("Monday", "08:00", "10:00")
        test_class = Class("Securitatea informatiei", "Laborator", "C401", "Tiplea Ferucio Laurentiu", 2, "B3")

        # Act
        test_class.set_schedule(schedule)
        
        # Assert
        self.assertEqual(test_class.schedule, schedule)
        self.assertEqual("Monday", test_class.schedule.day)
        self.assertEqual("08:00", test_class.schedule.start_time)
        self.assertEqual("10:00", test_class.schedule.end_time)

 
    def test_set_class_teacher_from_subject_teachers(self):
        # Arrange
        teacher1 = Teacher("Tiplea Ferucio Laurentiu")
        teacher2 = Teacher("Nica Anca Maria")
        subject  = Subject("Securitatea informatiei", "Mandatory", 3)

        subject.add_teacher(teacher1)
        subject.add_teacher(teacher2)

        # Act
        test_class = Class("Securitatea informatiei", "Laborator", "C401", subject.teachers[0], 2, "B3")

        # Assert
        self.assertIn(test_class.teacher, subject.teachers)
        self.assertEqual(test_class.teacher, subject.teachers[0])
        self.assertEqual(test_class.teacher.name, "Tiplea Ferucio Laurentiu")
        

    def test_set_name(self):
        # Arrange
        test_class = Class.__new__(Class)

        # Act
        test_class.set_name("Securitatea informatiei")

        #Assert
        self.assertEqual("Securitatea informatiei", test_class.get_name())


if __name__ == '__main__':
    unittest.main()
