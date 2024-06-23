"""
This is a test module.
"""

from pathlib import Path
import json
import pytest
from gendiff.diff import generate_diff

@pytest.mark.parametrize("path", [Path('./tests/fixtures')])
def test_run_gendiff(path: Path):
    """
    This function tests the `generate_diff` function with different input files.
    """
    got_json = generate_diff(path / 'file1.json', path / 'file2.json')
    got_yaml = generate_diff(path / 'file1.yaml', path / 'file2.yaml')
    got_nested_json = generate_diff(path / 'file_nested1.json', path / 'file_nested2.json')
    got_nested_yaml = generate_diff(path / 'file_nested1.yaml', path / 'file_nested2.yaml')
    got_plain = generate_diff(path / 'file_nested1.yaml', path / 'file_nested2.yaml', 'plain')

    with open(path / 'res_stylish', 'r', encoding="utf-8") as f:
        expected = f.read().strip() # json.load(f)
    with open(path / 'res_stylish_nested', 'r', encoding="utf-8") as f1:
        expected_nested = f1.read().strip()
    with open(path / 'plain', 'r', encoding="utf-8") as f2:
        expected_plain = f2.read().strip()
    assert got_json == expected
    assert got_yaml == expected
    # assert got_nested_json == expected_nested
    # assert got_nested_yaml == expected_nested
    assert got_plain == expected_plain

# import pytest
# from gendiff.diff import generate_diff
#
#
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
