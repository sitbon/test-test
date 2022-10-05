import pytest

from app import hello


def test_print_hi(capsys):
    hello.print_hi("pytest")
    captured = capsys.readouterr()
    assert captured.out == "Hi, pytest\n"
    assert captured.err == ""
