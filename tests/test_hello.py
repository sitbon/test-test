import pytest

from app import hello


@pytest.mark.parametrize("name1", ["pytest", "world", "you", ""])
@pytest.mark.parametrize("name2", ["alice", "bob", "charlie", ""])
def test_print_hi(capsys, name1, name2):

    if not name1 or not name2:
        with pytest.raises(ValueError):
            hello.print_hi(name1, name2)
    else:
        hello.print_hi(name1, name2)

        captured = capsys.readouterr()
        assert captured.out == f"Hi, {name1} & {name2}!\n"
        assert captured.err == ""
