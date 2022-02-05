import os
import pytest

if "campaigns.csv" in os.listdir():
    os.remove("campaigns.csv")


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
