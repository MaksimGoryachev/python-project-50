from unittest.mock import patch
import pytest
from gendiff.scripts.run_gendiff import main


def test_main_raises_value_error():
    with patch('gendiff.cli.parsing_args') as mock_parsing_args:
        # Настраиваем mock для возврата недопустимых аргументов
        mock_parsing_args.return_value = {
            'first_file': 'file1.txt',
            'second_file': 'file2.txt',
            'format': 'unknown_format'  # Неизвестный формат
        }

        with pytest.raises(SystemExit) as pytest_exit:
            main()

        assert pytest_exit.value.code == 2


def test_main_oserror_exit_code():
    with patch('gendiff.cli.parsing_args') as mock_parsing_args, \
            patch('gendiff.diff.generate_diff') as mock_generate_diff:
        # Настраиваем mock для генерации исключения OSError
        mock_parsing_args.return_value = lambda: None  # Заглушка для аргументов

        # Принудительно вызываем OSError при вызове generate_diff
        mock_generate_diff.side_effect = OSError

        with pytest.raises(SystemExit) as pytest_exit:
            main()  # Вызов вашей функции main

        assert pytest_exit.value.code == 2
