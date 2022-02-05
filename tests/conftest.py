import pytest
from helper.helper import launch_driver


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    driver = launch_driver(request.param)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
