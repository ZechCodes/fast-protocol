# fast-protocol
A very simple Python module to declare protocols for checking if objects provide the desired interface.

## Installation
```shell
pip install fast-protocol
```

## Usage
To create a Fast Protocol just call the `fast_protocol.protocol` function passing it the names of the methods/attributes that the protocol should support.
```python
from fast_protocol import protocol

def example():
    ...

Callable = protocol("__call__")  # Create a protocol that matches objects with a dunder call method
match example:
    case Callable():
        print("example is callable")
```
This can be used outside a `match` statement using `isinstance`.
```python
if isinstance(example, Callable):
    print("example is callable")
```

Protocols are generated with the name `"FastProtocol"`. This name can be changed by creating a new instance of
`FastProtocolBuilder`. The name can be set traditionally by passing the name of the protocol to the `FastProtocolBuilder` class. Alternatively you can pass the protocol name as a subscript to an existing `FastProtocolBuilder` which will return a new instance that uses that name.

**Traditional approach:**
```python
from fast_protocol import FastProtocolBuilder

Callable = FastProtocolBuilder("Callable")("__call__")
```
**Alternative approach:**
```python
from fast_protocol import protocol

Callable = protocol["Callable"]("__call__")
```
