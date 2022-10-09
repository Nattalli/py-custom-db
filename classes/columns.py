from dataclasses import dataclass


@dataclass
class Column:
    name: str
    type: int


@dataclass
class IntColumn:
    _value: int

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def name(self, value: int) -> None:
        if isinstance(value, int):
            self._value = value
        else:
            raise TypeError(f"Column type should be Integer, now it has "
                            f"{type(value)} type!")


@dataclass
class StrColumn:
    _value: str

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def name(self, value: str) -> None:
        if isinstance(value, str):
            self._value = value
        else:
            raise TypeError(f"Column type should be String, now it has "
                            f"{type(value)} type!")


@dataclass
class CharColumn:
    _value: str

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def name(self, value: str) -> None:
        if isinstance(value, str) and len(value) == 1:
            self._value = value
        else:
            raise TypeError(f"Column type should be Charset, now it has "
                            f"{type(value)} type!")


@dataclass
class RealColumn:
    _value: float

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def name(self, value: float) -> None:
        if isinstance(value, float):
            self._value = value
        else:
            raise TypeError(f"Column type should be Real, now it has "
                            f"{type(value)} type!")


@dataclass
class HTMLColumn:
    _value: str

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def name(self, value: str) -> None:
        if isinstance(value, str):
            open_tag = value.count("<")
            close_tag = value.count(">")
            if open_tag != close_tag:
                assert ValueError("Count of open and close tags should be equal!")
            if open_tag == 0 or close_tag == 0:
                assert ValueError("HTML file should contain at least 1 tag")
            self._value = value
        else:
            raise TypeError(f"Column type should be HTML, now it has "
                            f"{type(value)} type!")


@dataclass
class StrInvlColumn:
    _value: list

    @property
    def value(self) -> list:
        return self._value

    @value.setter
    def name(self, value: list) -> None:
        if isinstance(value, list) and isinstance(value[0], str) \
                and isinstance(value[1], str):
            if value[0] > value[1]:
                assert ValueError("First value should be less than second")
            self._value = value
        else:
            raise TypeError(f"Column type should be String Invl, now it has "
                            f"{type(value)} type with ({type(value[0])} and"
                            f" {type(value[1])}) elements!")


COLUMN_TYPES = [
    (0, "int", IntColumn),
    (1, "real", RealColumn),
    (2, "char", CharColumn),
    (3, "str", StrColumn),
    (4, "html", HTMLColumn),
    (5, "strInvl", StrInvlColumn)
]
