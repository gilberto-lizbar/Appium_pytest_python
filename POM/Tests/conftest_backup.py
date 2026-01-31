import pytest

# << ***************Test Reports Configuration On Failure***************
@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    # Handle both old and new pytest versions
    if hasattr(outcome, 'get_result'):
        rep = outcome.get_result()
    else:
        rep = outcome  # pytest 9.x returns the report directly
    setattr(item, "rep_" + rep.when, rep)
    return rep
# ***************Test Reports Configuration On Failure*************** >>
