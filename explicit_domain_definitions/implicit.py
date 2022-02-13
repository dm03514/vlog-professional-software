
def enroll_user(first_name: str, last_name: str):
    id = first_name + last_name
    insert_user_into_db(id, first_name, last_name)


def remove_user(first_name: str, last_name: str):
    id = first_name + last_name
    delete_user_from_db(id, first_name, last_name)


def notify_user(first_name: str, last_name: str):
    id = first_name + last_name
    send_user_notification(id)


def insert_user_into_db(*args, **kwargs): pass
def delete_user_from_db(*args, **kwargs): pass
def send_user_notification(*args, **kwargs): pass
