import pytest
import pytest_mock
import pathlib
from typer.testing import CliRunner

from python_kt_1.cli import app


runner = CliRunner()


def test_stats_command_simple(
    text_file: pathlib.Path, mocker: pytest_mock.MockerFixture
):
    """Проверка cli-команды stats без дополнительных опций.

    - запуск с корректным переданным путём
    - внутренний вызов юз-кейса
    - завершается корректно

    """

    from python_kt_1 import use_cases

    spy = mocker.spy(use_cases, "stats")

    result = runner.invoke(app, ["stats", str(text_file)])

    spy.assert_called_once_with("Hello\nWorld")
    assert result.exit_code == 0


def test_stats_command_with_output(
    text_file: pathlib.Path,
    output_file: pathlib.Path,
    mocker: pytest_mock.MockerFixture,
):
    """Проверка cli-команды stats с опцией сохранения в файл.

    - запуск с корректными входным и выходным путями
    - внутренний вызов юз-кейса
    - запись в выходной файл
    - завершается корректно

    """

    from python_kt_1 import use_cases

    spy = mocker.spy(use_cases, "stats")

    result = runner.invoke(app, ["stats", str(text_file), "--output", str(output_file)])

    output_text = output_file.read_text(encoding="utf-8")
    spy.assert_called_once_with("Hello\nWorld")

    assert len(output_text) > 0
    assert result.exit_code == 0


def test_stats_command_with_pos(
    text_file: pathlib.Path, mocker: pytest_mock.MockerFixture
):
    """Проверка cli-команды stats с опцией сохранения в файл.

    - запуск с корректными входным и выходным путями
    - внутренний вызов юз-кейса
    - запись в выходной файл
    - завершается корректно

    """

    from python_kt_1 import use_cases

    spy = mocker.spy(use_cases, "stats")

    result = runner.invoke(app, ["stats", str(text_file), "--pos"])

    spy.assert_called_once_with("Hello\nWorld", True)

    assert result.exit_code == 0
