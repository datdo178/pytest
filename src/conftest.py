import pytest


@pytest.fixture(scope='session')
def init_value():
    return 5

@pytest.fixture(scope='session')
def double_init_value(init_value):
    return init_value * 2

@pytest.fixture(scope='session')
def value(init_value, double_init_value):
    print('\nRun fixture')
    return double_init_value + init_value

@pytest.fixture(autouse=True)
def welcomeMessage():
    print('\nWelcome')