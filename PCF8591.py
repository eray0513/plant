import smbus

_bus = smbus.SMBus(1)
_address = 0x48

def setup(addr=0x48, bus=1):
    global _bus, _address
    _address = addr
    _bus = smbus.SMBus(bus)

def read(chn):
    """Read analog input 0-3, returns 0-255."""
    _bus.write_byte(_address, 0x40 | (chn & 0x03))
    _bus.read_byte(_address)          # discard stale first reading
    return _bus.read_byte(_address)

def write(value):
    """Write 0-255 to the analog output (AOUT)."""
    _bus.write_byte_data(_address, 0x40, int(value))

# aliases used by some kit examples
analogRead = read
analogWrite = write
