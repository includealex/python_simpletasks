import pytest

def caps(s: str) -> str:
    if type(s) != str:
        raise TypeError('На входе ожидалась строка')
    return s.upper()

def test_caps():
    input_str = "abc"
    expected_str = "ABC"
    assert caps(input_str) == expected_str

def test_caps_on_non_string():
    non_string: int = 42
    with pytest.raises(TypeError, match='На входе ожидалась строка'):
        caps(non_string)
