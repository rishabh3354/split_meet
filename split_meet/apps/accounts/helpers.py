import re


def email_validation_check(email):
    """
    for email, valid syntax returns True, else False.
    :param email:
    :return:
    """
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def check_if_password_match(password, repassword):
    if password == repassword:
        return True
    else:
        return False
