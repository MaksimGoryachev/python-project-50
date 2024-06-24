"""
This is a test module.
"""

from pathlib import Path
import pytest
from gendiff.diff import generate_diff


def read_file(path: Path) -> str:
    """
    This function reads a file.
    """
    with open(path, 'r', encoding="utf-8") as file:
        return file.read().strip()

@pytest.mark.parametrize("path", [Path('./tests/fixtures')])
def test_run_gendiff(path: Path):
    """
    This function tests the `generate_diff` function with different input files.
    """
    got_json = generate_diff(path / 'file1.json', path / 'file2.json')
    got_yaml = generate_diff(path / 'file1.yaml', path / 'file2.yaml')
    expected = read_file(path /'res_stylish')
    assert got_json == expected
    assert got_yaml == expected

    got_nested_json = generate_diff(path / 'file_nested1.json',
                                    path / 'file_nested2.json', 'stylish')
    got_nested_yaml = generate_diff(path / 'file_nested1.yaml',
                                    path / 'file_nested2.yaml', 'stylish')
    expected_nested = read_file(path /'res_stylish_nested')
    assert got_nested_json == expected_nested
    assert got_nested_yaml == expected_nested

    got_plain = generate_diff(path / 'file_nested1.yaml',
                              path / 'file_nested2.yaml', 'plain')
    expected_plain = read_file(path / 'res_plain')
    assert got_plain == expected_plain

    got_json_nested = generate_diff(path / 'file_nested1.json',
                                    path / 'file_nested2.json', 'json')

    expected_json = read_file(path /'res_json_nested')
    assert got_json_nested == expected_json

# @pytest.mark.parametrize('first_file, second_file, expected', [
#     ('./tests/fixtures/file1.json', './tests/fixtures/file2.json',
#      './tests/fixtures/res_stylish'),
#     ('./tests/fixtures/file1.yaml', './tests/fixtures/file2.yaml',
#      './tests/fixtures/res_stylish')])
# def test_run_gendiff(first_file, second_file, expected):
#     """
#     This function tests the `generate_diff` function with different input files.
#     """
#     got_generate_diff = generate_diff(first_file, second_file)
#     with open(expected, 'r', encoding="utf-8") as f:
#         expected = f.read()
#     assert got_generate_diff == expected
