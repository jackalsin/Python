import quick2wire.i2c as i2c

address = 0x68
iodir_register = 0x00
gpio_register = 0x09

with i2c.I2CMaster() as bus:    
    bus.transaction(
        i2c.writing_bytes(address, iodir_register, 0xFF))

    read_results = bus.transaction(
        i2c.writing_bytes(address, gpio_register),
        i2c.reading(address, 1))

    gpio_state = read_results[0][0]

    print("%02x" % gpio_state)
