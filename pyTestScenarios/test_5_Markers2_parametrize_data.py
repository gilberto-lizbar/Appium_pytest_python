import pytest


def get_data():
    # This acts as our data source
    return [
        ("gilberto1@test.com", "1234"),
        ("gilberto2@test.com", "1234")
    ]


@pytest.mark.parametrize("username, password", get_data())
def test_loginFlow(username, password):
    print(f"\nTesting with: {username} and {password}")
