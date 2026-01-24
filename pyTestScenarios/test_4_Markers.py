import pytest


@pytest.mark.sanity
def test_login():
    print("login flow")


@pytest.mark.smoke
def test_logout():
    print("logout flow")


@pytest.mark.regression
def test_create():
    print("create flow")


@pytest.mark.skip(reason="this feature is currently incomplete")
def test_skip():
    print("skip test")


@pytest.mark.skip
def test_skip2():
    print("skip test2")
