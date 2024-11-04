import sys
import pytest
from gendiff.cli import parsing_args


def test_parsing_args_requires_two_files():
    with pytest.raises(SystemExit) as pytest_exit:
        parsing_args()  # Вызов функции без аргументов
    assert pytest_exit.value.code != 0  # Проверка, что код завершения не = 0


def test_parsing_args_with_invalid_format():
    with pytest.raises(SystemExit) as pytest_exit:
        # Используем mock для передачи аргументов командной строки
        sys.argv = ['script_name', 'file1', 'file2',
                    '--format', 'invalid_format']
        parsing_args()  # Вызов функции с неправильным форматом
    assert pytest_exit.value.code != 0  # Проверка, что код завершения не = 0
