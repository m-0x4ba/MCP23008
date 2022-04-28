# mcp23008

This is a Python module to control the MCP23008 I2C Port Expander.

## Requirements

* `smbus` (install with `pip3 install smbus`)
* A MCP23008 connected to an I2C port

## Examples

### Read Input

```python
import time
from mcp23008 import MCP23008

mcp = MCP23008()

pin = 0

mcp.set_pin_direction(pin, True)

while True:
    value = mcp.get_pin_value(pin)
    print(value)
    time.sleep(1)
```

### Write Output

```python
import time
from mcp23008 import MCP23008

mcp = MCP23008()

pin = 0

mcp.set_pin_direction(pin, False)

while True:
    mcp.set_pin_value(pin, True)
    time.sleep(1)
    mcp.set_pin_value(pin, False)
    time.sleep(1)
```
