import pytest
import unittest.mock


@pytest.mark.with_fakefs
@pytest.mark.parametrize("counter", range(2))
def test_fs_and_mocker(
    client,
    fs,
    counter,
):
    with unittest.mock.patch("mysite.views.foo") as mocker:
        client.get("/foo/")
        mocker.assert_called()


@pytest.mark.without_fakefs
@pytest.mark.parametrize("counter", range(2))
def test_mocker(
    client,
    counter,
):
    with unittest.mock.patch("mysite.views.foo") as mocker:
        client.get("/foo/")
        mocker.assert_called()

