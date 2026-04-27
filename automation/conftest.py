import os
import pytest


def pytest_collection_modifyitems(config, items):
    if os.getenv("CI") == "true":
        skip_marker = pytest.mark.skip(reason="Skipping Selenium tests in CI")

        for item in items:
            item.add_marker(skip_marker)
