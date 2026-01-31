import json
import pytest

from ..PageObjects.LoginPageBoth import LoginPageBoth

test_data_path = '../Data/test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]  # Storing in a list all content of 'data' key from json


@pytest.mark.parametrize("data_item", test_list)  # Extract test_list and attached to test_list_item
# Send data_item as an argument of test method to have access to json data
def test_signUp_to_app(setup_function, data_item):
    driver = setup_function  # Calling driver from browserInstance fixture
    loginPage = LoginPageBoth(driver)

    print(f"Testing Sign Up for: {data_item['email']}")
    loginPage.login(data_item['username'], data_item['password'])
