import re


def email_validation_check(email):
    """
    for email, valid syntax returns True, else False.
    :param email:
    :return:
    """
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))
