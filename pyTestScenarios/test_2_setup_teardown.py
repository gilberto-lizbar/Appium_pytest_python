import pytest


def setup_module(module):
    print("DB connection start")


def teardown_module(module):
    print("DB connection closed")


def setup_function(function):
    print("appium server start")


def teardown_function(function):
    print("stop server")


def test_login():
    print("login test")


def test_logout():
    print("login test")
