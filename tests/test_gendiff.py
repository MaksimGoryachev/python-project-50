from pathlib import Path
import pytest
from gendiff.diff import generate_diff


def read_file(path: Path) -> str:
    """
    This function reads a file.
    """
    with open(path, 'r', encoding="utf-8") as file:
        return file.read().strip()


FIXTURES_PATH = Path('tests/fixtures')


@pytest.mark.parametrize('file1, file2, expected_file, format_', [
    ('file1.json', 'file2.json', 'res_stylish', 'stylish'),
    ('file1.yaml', 'file2.yaml', 'res_stylish', 'stylish'),
    ('file_nested1.json', 'file_nested2.json', 'res_json_nested', 'json'),
    ('file_nested1.yaml', 'file_nested2.yaml', 'res_plain', 'plain'),
])
def test_run_gendiff(file1, file2, expected_file, format_):
    """
    This function tests the `generate_diff` function with different input files.
    """
    got = generate_diff(FIXTURES_PATH / file1, FIXTURES_PATH / file2, format_)
    expected = read_file(FIXTURES_PATH / expected_file)
    assert got == expected
