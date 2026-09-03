from core.models.brand import Brand


def get_brand():
    return Brand.get_solo()


def set_verifier(profile, user):
    profile._verifier = user
