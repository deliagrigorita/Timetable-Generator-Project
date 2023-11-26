class User:
    def __init__(self, user_id: int, user_name: str):
        self.id = user_id
        self.name = user_name

    def show_user_info(self):
        print(f'User ID: {self.id}\nUsername: {self.name}')
