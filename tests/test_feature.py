import pytest


pytestmark = pytest.mark.skip(reason="TODO: implement these tests")
# or:
# pytest.skip(reason="TODO: implement these tests", allow_module_level=True)
# (see https://docs.pytest.org/en/latest/skipping.html#skipping-test-functions)
# note: doesn't output the reason in the report


def test_feature_1():
    pass


def test_feature_2():
    pass
