import pytest
from script.deploy import deploy_favorites

@pytest.fixture(scope="function")
def favorites_contract():
    return deploy_favorites()