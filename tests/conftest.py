
import os, sys
import pytest

sys.path.append("..")

from src.restapi.app import app as _app

@pytest.fixture
def client():
    _app.config.from_object('src.restapi.config.TestingConfig')

    with _app.test_client() as client:
        yield client
