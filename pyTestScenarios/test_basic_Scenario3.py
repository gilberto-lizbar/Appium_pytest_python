import pytest


@pytest.fixture(scope='module')
def setup():
    print("DB connection start")

    yield
    print("DB connection closed")


@pytest.fixture(scope='function')
def before_Each_function():
    print("appium server start")

    yield
    print("appium server stop")


def test_login(setup, before_Each_function):
    print("login test")


def test_logout(setup, before_Each_function):
    print("logout test")


#@pytest.mark.usefixtures("setup", "before_Each_function")
#def test_other():
#    print("other test")
