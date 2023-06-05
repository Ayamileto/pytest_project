import pytest

from pytest_proj.utils import arrs


@pytest.mark.parametrize('array, index, default, expected', [
    ([1, 2, 3], 1, "test", 2),
    ([], -1, "test", "test")
])
def test_get(array, index, default, expected):
    assert arrs.get(array, index, default) == expected


@pytest.mark.parametrize('call, start, end, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, None, [2, 3]),
    ([], 0, 0, []),
    ([1, 2, 3, 4], -1, None, [4]),
    ([1, 2, 3, 4], -20, None, [1, 2, 3, 4])

])
def test_my_slice(call, start, end, expected):
    assert arrs.my_slice(call, start, end) == expected
