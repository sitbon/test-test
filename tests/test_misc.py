import pytest


def test_misc_raises():
    with pytest.raises(ValueError, match=r"Error 4") as excinfo:
        raise ValueError("Error 4")

    assert excinfo.value.args[0] == "Error 4"


@pytest.mark.xfail(raises=ValueError, reason="Error 4 Simulation")
def test_misc_xfail():
    raise ValueError("Error 4")
