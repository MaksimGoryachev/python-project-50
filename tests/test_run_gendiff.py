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
