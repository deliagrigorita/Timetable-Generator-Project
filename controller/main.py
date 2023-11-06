from models.User import User
from models.Student import Student


if __name__ == '__main__':
    user1 = User(0, "Boboc Raul")
    student1 = Student(1, "Dutuc Paul", "extra_long_and_safe_matricol")

    user1.show_user_info()
    print('#############################################################')
    student1.show_student_info()
    print('#############################################################')
