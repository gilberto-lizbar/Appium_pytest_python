import pytest


@pytest.mark.order(1)
def test_loginApp():
    print("This is loginApp test")


def test_searchApp():
    print("This is searchApp test")


@pytest.mark.order(2)
def test_createUser():
    print("This is createUser test")


def test_editUser():
    print("This is editUser test")


@pytest.mark.order(3)
def test_deleteUser():
    print("This is deleteUser test")


def test_logoutUser():
    print("This is logoutUser test")
