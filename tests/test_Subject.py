import unittest

from classes.Teacher import Teacher
from classes.Subject import Subject

class TestSubject(unittest.TestCase):
    
    def test_add_teacher(self):
        # Arrange
        teacher = Teacher("Tiplea Ferucio Laurentiu")
        subject = Subject("Securitatea informatiei", "Mandatory", 3)

        # Act
        subject.add_teacher(teacher)

        # Assert
        self.assertIn(teacher, subject.teachers)
        self.assertEqual(1, len(subject.teachers))


if __name__ == '__main__':
    unittest.main()