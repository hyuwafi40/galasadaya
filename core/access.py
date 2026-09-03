ROLE_LEVELS = {
    "reguler": 1,
    "administrator": 2,
    "developer": 3,
}


def get_user_role(user):
    if not user.is_authenticated:
        return None
    if user.is_superuser:
        return "developer"
    if user.is_staff:
        return "administrator"
    return "reguler"


def has_access(user, required_role="reguler"):
    role = get_user_role(user)
    if role is None:
        return False
    return ROLE_LEVELS.get(role, 0) >= ROLE_LEVELS.get(required_role, 0)
