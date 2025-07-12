import os
os.environ['BLINKA_FT232H'] = '1'
import board
import adafruit_mcp4725
from time import sleep

# returns an addressable DAC instance. see the following for an example on how to use it:
# https://learn.adafruit.com/mcp4725-12-bit-dac-tutorial/python-circuitpython
def setup() -> adafruit_mcp4725.MCP4725:
    i2c = board.I2C()
    dac = adafruit_mcp4725.MCP4725(i2c)
    
    return dac

# basic wrapper to output a real voltage to a 12 bit DAC
def set_voltage(dac, voltage, MAX=4095, MIN=0, VIN=3.3):
    if MAX > 4095 or MIN < 0:
        raise ValueError("MAX must be <= 4095 and MIN must be >= 0")
    if voltage < 0 or voltage > VIN:
        raise ValueError(f"Voltage must be between 0 and {VIN} volts")
    
    step = (VIN / MAX)
    
    value = int(voltage / step)
    if value < MIN:
        value = MIN
    elif value > MAX:
        value = MAX
        
    dac.raw_value = value

# creates a 0 - voltage - 0 pulse on the DAC output
# duration is in seconds, default is 100 usec
def do_pulse(dac, voltage=1.0, duration=0.0001):
    set_voltage(dac, 0.0) # set to 0V before pulse
    set_voltage(dac, voltage)
    sleep(duration)
    set_voltage(dac, 0.0) # set to 0V after pulse

# just sets the voltage to 1.0V for fun!
def main():
    dac = setup()    
    
    # set_voltage(dac, 1.0)
    do_pulse(dac, voltage=1.0)
    
if __name__ == "__main__":
    main()