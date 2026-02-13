import pytest

SENTENCES = (
    "При расставании слез не было пролито из родительских глаз; дана была полтина меди на расход и лакомства и, что гораздо важнее, умное наставление. ",
    "«Смотри же, Павлуша, учись, не дури и не повесничай, а больше всего угождай учителям и начальникам. ",
    "Коли будешь угождать начальнику, то, хоть и в науке не успеешь и таланту бог не дал, все пойдешь в ход и всех опередишь. ",
    "С товарищами не водись, они тебя добру не научат; а если уж пошло на то, так водись с теми, которые побогаче, чтобы при случае могли быть тебе полезными. ",
    "Не угощай и не потчевай никого, а веди себя лучше так, чтобы тебя угощали; а больше всего береги и копи копейку: эта вещь надежнее всего на свете. ",
    "Товарищ или приятель тебя надует и в беде первый тебя выдаст, а копейка не выдаст, в какой бы беде ты ни был. ",
    "Все сделаешь и все прошибешь на свете копейкой».",
    "Давши такое наставление, отец расстался с сыном потащился вновь домой на своей соро́ке, и с тех пор уже никогда он больше его не видел, но слова и наставления заронились глубоко ему в душу.",
)


@pytest.fixture(scope="session")
def sentence():
    return SENTENCES[1]


@pytest.fixture(scope="session")
def paragraph_one_sentence():
    return SENTENCES[0]


@pytest.fixture(scope="session")
def paragraph_two_sentences():
    return SENTENCES[1] + SENTENCES[2]


@pytest.fixture(scope="session")
def paragraph_four_sentences():
    return " ".join(SENTENCES[3:7])


@pytest.fixture(scope="session")
def text():
    return "\n".join(
        [
            SENTENCES[0],
            SENTENCES[1] + SENTENCES[2],
            " ".join(SENTENCES[3:7]),
            SENTENCES[7],
        ]
    )


@pytest.fixture(scope="session")
def text_file(tmp_path_factory: pytest.TempPathFactory):
    fake_file = tmp_path_factory.mktemp("data") / "text_1.txt"

    fake_file.write_text("Hello\nWorld")

    return fake_file


@pytest.fixture(scope="session")
def output_file(tmp_path_factory: pytest.TempPathFactory):
    fake_file = tmp_path_factory.mktemp("output") / "text_1.txt"
    fake_file.touch()

    return fake_file
