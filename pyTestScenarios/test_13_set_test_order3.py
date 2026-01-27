import pytest


@pytest.mark.order()
def test_searchApp():
    print("This is searchApp test")


@pytest.mark.order("last")
def test_logoutUser():
    print("This is logoutUser test")


@pytest.mark.order("first")
def test_loginApp():
    print("This is loginApp test")
