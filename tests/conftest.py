from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state() -> None:
    # Keep tests isolated from mutations to the in-memory activity store.
    original_activities = deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_activities)
