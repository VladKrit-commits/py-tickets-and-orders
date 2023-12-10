from db.models import User


def set_user_fields(
        user: User,
        username: str = None,
        password: int = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> None:
    if username:
        user.username = username
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if password:
        user.set_password(password)
    user.save()


def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> User:
    user = User.objects.create_user(username=username, password=password)
    set_user_fields(
        user,
        email=email,
        first_name=first_name,
        last_name=last_name
    )
    return user


def get_user(user_id: int) -> User:
    return User.objects.get(id=user_id)


def update_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> User:
    user = get_user(user_id)
    set_user_fields(
        user,
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name
    )
    return user
