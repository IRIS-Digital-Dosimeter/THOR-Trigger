import lib

# get a DAC instance
dac = lib.setup()

from time import sleep

# every second, output a 1.0V pulse for 100 usec
while True:
    lib.do_pulse(dac, voltage=1.0, duration=0.0001)
    
    sleep(1)