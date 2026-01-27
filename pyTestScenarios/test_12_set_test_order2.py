import pytest


@pytest.mark.order(before="test_logoutUser")
def test_searchApp():
    print("This is searchApp test")


@pytest.mark.order(after="test_loginApp")
def test_logoutUser():
    print("This is logoutUser test")


@pytest.mark.order()
def test_loginApp():
    print("This is loginApp test")
