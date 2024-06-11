import pytest
from gendiff.diff import generate_diff


@pytest.mark.parametrize('first_file, second_file, expected', [
    ('./tests/fixtures/file1.json', './tests/fixtures/file2.json',
     './tests/fixtures/res_stylish.txt'),
])
def test_run_gendiff(first_file, second_file, expected):
    got_json = generate_diff(first_file, second_file)
    with open(expected, 'r') as f:
        expected = f.read()
    assert got_json == expected
