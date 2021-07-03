import pytest
from handler import detect_language


@pytest.mark.parametrize("test_input, expected", [
    ('This text is written in English', 'en'),
    ('Этот текст написан mostly по-русски', 'ru'),
    ('Ten tekst jest napisany w jezyku polskim, ale bez znakow diakrytycznych', 'pl'),
    ('Текст написаний українською', 'uk')
])
def test_detect_language(test_input, expected):
    assert detect_language(test_input) == expected
