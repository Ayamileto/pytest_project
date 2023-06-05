import pytest

from pytest_proj.utils import dicts


data = {"vcs": "mercurial"}


def test_get_val():
    assert dicts.get_val(data, "vcs") == 'mercurial'
    assert dicts.get_val(data, "vcs", "git") == 'mercurial'
    assert dicts.get_val({}, "vcs", "git") == 'git'
    assert dicts.get_val({}, "vcs", "bazaar") == 'bazaar'


def test_get_val_collection_type():
    with pytest.raises(TypeError):
        dicts.get_val("not a dictionary", "key")
        dicts.get_val(None, "key")


def test_get_val_key_value():
    with pytest.raises(ValueError):
        dicts.get_val(data, 123)


