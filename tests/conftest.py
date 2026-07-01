from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Keep tests isolated because the API stores data in memory.
    original_state = deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_state)
