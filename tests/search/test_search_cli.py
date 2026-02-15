import pytest
import pytest_mock
import pathlib
from typer.testing import CliRunner

from python_kt_1.cli import app


runner = CliRunner()


def test_search_command_simple(
    text_file: pathlib.Path,
    mocker: pytest_mock.MockerFixture,
    capfd: pytest.CaptureFixture,
):
    """Проверка cli-команды search без дополнительных опций.

    - запуск с корректным путём к одному текстовому файлу
    - единожды вызывает юз-кейс
    - выводит результат в консоль
    - завершается корректно

    """

    from python_kt_1 import use_cases

    spy = mocker.spy(use_cases, "search")

    result = runner.invoke(app, ["search", "Hello", str(text_file)])

    spy.assert_called_once_with("Hello", text_file, False)
    captured = capfd.readouterr()

    assert len(captured.out) > 0
    assert result.exit_code == 0


def test_search_command_with_regex(
    text_file: pathlib.Path,
    mocker: pytest_mock.MockerFixture,
    capfd: pytest.CaptureFixture,
):
    """Проверка cli-команды search для поиска по регулярному выражению.

    - запуск с корректным путём к одному текстовому файлу
    - единожды вызывает юз-кейс, передавая флаг
    - выводит результат в консоль
    - завершается корректно

    """
    from python_kt_1 import use_cases

    spy = mocker.spy(use_cases, "search")

    result = runner.invoke(app, ["search", ".ello", str(text_file), "--regex"])

    spy.assert_called_once_with(".ello", text_file, True)
    captured = capfd.readouterr()

    assert len(captured.out) > 0
    assert result.exit_code == 0
