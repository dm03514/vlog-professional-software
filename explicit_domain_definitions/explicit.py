class User:
    def __init__(self, first_name, last_name, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id


def create_user(first_name: str, last_name: str) -> User:
    user = User(
        first_name = first_name,
        last_name = last_name
    )
    user.id = first_name + last_name
    return user


# user = create_user(...)

def enroll_user(user: User):
    # ...
    pass


def remove_user(user: User):
    # ...
    pass


def notify_user(user: User):
    # ...
    pass