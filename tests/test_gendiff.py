"""
This is a test module.
"""

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

from pathlib import Path
import pytest
from gendiff.diff import generate_diff

@pytest.mark.parametrize("path", [Path('./tests/fixtures')])
def test_run_gendiff(path: Path):
    """
    This function tests the `generate_diff` function with different input files.
    """
    got_json = generate_diff(path / 'file1.json', path / 'file2.json')
    got_yaml = generate_diff(path / 'file1.yaml', path / 'file2.yaml')
    with open(path / 'res_stylish', 'r', encoding="utf-8") as f:
        expected = f.read()
    assert got_json == expected
    assert got_yaml == expected


@pytest.mark.parametrize("path", [Path('./tests/fixtures')])
def test_path_parametrization(path: Path):
    test_run_gendiff(path)
