from smbus import SMBus


REG_IODIR = 0x00  # IO direction
REG_IPOL = 0x01  # Input polarity
REG_GPINTEN = 0x02  # Interrupt on change
REG_DEFVAL = 0x03  # Default value
REG_INTCON = 0x04  # Interrupt control
REG_IOCON = 0x05  # Configuration
REG_GPPU = 0x06  # Pull-up resistor
REG_INTF = 0x07  # Interrupt flag
REG_INTCAP = 0x08  # Interrupt capture
REG_GPIO = 0x09  # Port
REG_OLAT = 0x0A  # Output latch


class MCP23008:
    def __init__(self, address=0x20, bus=1):
        self.address = address
        self.bus = SMBus(bus)

    def _get_bit(self, byte: int, bit: int) -> bool:
        return bool((byte >> bit) & 1)

    def _set_bit(self, byte: int, bit: int, value: bool) -> int:
        if value:
            return byte | (1 << bit)
        else:
            return byte & ~(1 << bit)

    def _read_register(self, register: int) -> int:
        return self.bus.read_byte_data(self.address, register)

    def _write_register(self, register: int, value: int) -> None:
        self.bus.write_byte_data(self.address, register, value)

    def _read_register_bit(self, register: int, bit: int) -> bool:
        return self._get_bit(self._read_register(register), bit)

    def _write_register_bit(self, register: int, bit: int, value: bool) -> None:
        self._write_register(register, self._set_bit(self._read_register(register), bit, value))

    def set_pin_direction(self, pin: int, direction: bool) -> None:
        """
        Set the pin direction.

        :param pin: Pin number (0-7)
        :param direction: True for input, False for output
        """
        self._write_register_bit(REG_IODIR, pin, direction)

    def get_pin_direction(self, pin: int) -> bool:
        """
        Get the pin direction.

        :param pin: Pin number (0-7)
        :return: True for input, False for output
        """
        return self._read_register_bit(REG_IODIR, pin)

    def set_pin_value(self, pin: int, value: bool) -> None:
        """
        Set pin value.

        :param pin: Pin number (0-7)
        :param value: True for high, False for low
        """
        self._write_register_bit(REG_GPIO, pin, value)

    def get_pin_value(self, pin: int) -> bool:
        """
        Get pin value.

        :param pin: Pin number (0-7)
        :return: True for high, False for low
        """
        return self._read_register_bit(REG_GPIO, pin)

    def set_input_polarity(self, pin: int, value: bool) -> None:
        """
        Set input polarity.

        :param pin: Pin number (0-7)
        :param value: True for inverted, False for normal
        """
        self._write_register_bit(REG_IPOL, pin, value)

    def get_input_polarity(self, pin: int) -> bool:
        """
        Get input polarity.

        :param pin: Pin number (0-7)
        :return: True for inverted, False for normal
        """
        return self._read_register_bit(REG_IPOL, pin)

    def set_pullup(self, pin: int, value: bool) -> None:
        """
        Set pull-up resistor.

        :param pin: Pin number (0-7)
        :param value: True for enabled, False for disabled
        """
        self._write_register_bit(REG_GPPU, pin, value)

    def get_pullup(self, pin: int) -> bool:
        """
        Get pull-up resistor.

        :param pin: Pin number (0-7)
        :return: True for enabled, False for disabled
        """
        return self._read_register_bit(REG_GPPU, pin)

    # Not tested

    # def set_interrupt_on_change(self, pin: int, value: bool) -> None:
    #     self._write_register_bit(REG_GPINTEN, pin, value)

    # def get_interrupt_on_change(self, pin: int) -> bool:
    #     return self._read_register_bit(REG_GPINTEN, pin)

    # def set_interrupt_default_value(self, pin: int, value: bool) -> None:
    #     self._write_register_bit(REG_DEFVAL, pin, value)

    # def get_interrupt_default_value(self, pin: int) -> bool:
    #     return self._read_register_bit(REG_DEFVAL, pin)

    # def set_interrupt_control(self, pin: int, value: bool) -> None:
    #     self._write_register_bit(REG_INTCON, pin, value)

    # def get_interrupt_control(self, pin: int) -> bool:
    #     return self._read_register_bit(REG_INTCON, pin)

    # def get_interrupt_capture(self, pin: int) -> bool:
    #     return self._read_register_bit(REG_INTCAP, pin)

    # def set_output_latch(self, pin: int, value: bool) -> None:
    #     self._write_register_bit(REG_OLAT, pin, value)

    # def get_output_latch(self, pin: int) -> bool:
    #     return self._read_register_bit(REG_OLAT, pin)

    # def get_interrupt_flag(self, pin: int) -> bool:
    #     return self._read_register_bit(REG_INTF, pin)
