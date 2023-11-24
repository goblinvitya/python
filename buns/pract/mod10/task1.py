import re


def valid_password(password):
    chars = re.findall('[^a-zA-Z0-9]', password)
    if len(set(chars)) < 3:
        return False

    if len(password) < 8:
        return False

    if re.findall(r'(\w)\1', password) is None:
        return False

    if re.search(r'\d', password) is None:
        return False

    if re.search(r'[,\.!?]', password) is not None:
        return False

    return True


def test_valid_password():
    """
    >>> valid_password('rtG&3FG#Tr^e')
    True
    >>> valid_password('a^A1@*@1Aa')
    True
    >>> valid_password('oF^a1D@y5%e6')
    True
    >>> valid_password('enroi#$*rkdeR#$*092uwedchf34tguv394h')
    True
    >>> valid_password('пароль')
    False
    >>> valid_password('password')
    False
    >>> valid_password('qwerty')
    False
    >>> valid_password('lOngPa$$W0Rd')
    False
    """
    pass


test_valid_password()
