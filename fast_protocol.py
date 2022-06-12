from __future__ import annotations
from typing import Protocol as _Protocol, runtime_checkable as _runtime_checkable


class FastProtocolBuilder:
    """Creates protocols at runtime which can be used for checking if objects provide the correct interface.

    >>> from fast_protocol import protocol
    >>> Callable = protocol("__call__")
    >>> match x:
    >>>     case Callable():
    >>>         print("x is callable")

    Alternatively you can use isinstance
    >>> from fast_protocol import protocol
    >>> Callable = protocol("__call__")
    >>> if isinstance(x, Callable):
    >>>     print("x is callable")

    Protocols are generated with the name "FastProtocol." This name can be overriden by creating a new instance of
    FastProtocolBuilder with the desired name. The name can be set traditionally by calling the FastProtocolBuilder
    passing it the name of the protocol. Alternatively you can pass the protocol name as a subscript to an existing
    FastProtocolBuilder which will return a new instance initialized with the given name.

    Traditional approach:
    >>> Callable = FastProtocolBuilder("Callable")("__call__")

    Alternative approach:
    >>> Callable = protocol["Callable"]("__call__")
    """
    def __init__(self, name: str):
        self.name = name

    def __call__(self, *attrs: str) -> _Protocol:
        return _runtime_checkable(
            type(
                self.name,
                (_Protocol,),
                {name: None for name in attrs}
            )
        )

    def __getitem__(self, name) -> FastProtocolBuilder:
        return FastProtocolBuilder(name)


protocol = FastProtocolBuilder("FastProtocol")
