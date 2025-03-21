import random
from abc import abstractmethod
from collections.abc import Callable, Iterator, MutableMapping, Sequence
from typing import Any, Literal
from typing_extensions import TypeAlias

class SequenceGenerator:
    length: int | None
    requested_entropy: str
    rng: random.Random
    @property
    @abstractmethod
    def symbol_count(self) -> int: ...
    def __init__(self, entropy: int | None = None, length: int | None = None, rng: random.Random | None = None) -> None: ...
    @property
    def entropy_per_symbol(self) -> float: ...
    @property
    def entropy(self) -> float: ...
    def __next__(self) -> str: ...
    def __call__(self, returns: None | int | Callable[[Any], Iterator[Any]] = None) -> str | list[str] | Iterator[str]: ...
    def __iter__(self) -> Iterator[str]: ...

_Charset: TypeAlias = Literal["ascii_72", "ascii_62", "ascii_50", "hex"]
default_charsets: dict[_Charset, str]

class WordGenerator(SequenceGenerator):
    charset: _Charset
    chars: str | bytes | None
    def __init__(
        self,
        chars: str | bytes | None = None,
        charset: _Charset | None = None,
        *,
        entropy: int | None = None,
        length: int | None = None,
        rng: random.Random | None = None,
    ) -> None: ...
    @property
    def symbol_count(self) -> int: ...

def genword(
    entropy: int | None = None,
    length: int | None = None,
    returns: None | int | Callable[[Any], Iterator[Any]] = None,
    *,
    chars: str | None = None,
    charset: _Charset | None = None,
    rng: random.Random | None = None,
) -> str | list[str] | Iterator[str]: ...

class WordsetDict(MutableMapping[Any, Any]):
    paths: dict[str, str] | None
    def __init__(self, *args, **kwds) -> None: ...
    def __getitem__(self, key: str) -> tuple[str | bytes, ...]: ...
    def set_path(self, key: str, path: str) -> None: ...
    def __setitem__(self, key: str, value: tuple[str | bytes, ...]) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __contains__(self, key: object) -> bool: ...

default_wordsets: WordsetDict
_Wordset: TypeAlias = Literal["eff_long", "eff_short", "eff_prefixed", "bip39"]

class PhraseGenerator(SequenceGenerator):
    wordset: _Wordset
    words: Sequence[str | bytes] | None
    sep: str | None
    def __init__(
        self,
        wordset: _Wordset | None = None,
        words: Sequence[str | bytes] | None = None,
        sep: str | bytes | None = None,
        *,
        entropy: int | None = None,
        length: int | None = None,
        rng: random.Random | None = None,
    ) -> None: ...
    @property
    def symbol_count(self) -> int: ...

def genphrase(
    entropy: int | None = None,
    length: int | None = None,
    returns: None | int | Callable[[Any], Iterator[Any]] = None,
    *,
    wordset: _Wordset | None = None,
    words: Sequence[str | bytes] | None = None,
    sep: str | bytes | None = None,
    rng: random.Random | None = None,
) -> str | list[str] | Iterator[str]: ...
