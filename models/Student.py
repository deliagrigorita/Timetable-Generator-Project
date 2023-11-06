from models import User


class Student(User):
    def __init__(self, user_id: int, user_name: str, user_matricol: str):
        super().__init__(user_id, user_name)
        self.matricol = user_matricol
