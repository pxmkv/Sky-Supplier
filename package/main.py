from mpl3115a2 import MPL3115A2
from machine import I2C, Pin, ADC
import time
i2c = I2C(sda=Pin(21), scl=Pin(22))
mpl = MPL3115A2(i2c, mode=MPL3115A2.ALTITUDE)

VOLTAGE_SUPPLY = 3.3  # Voltage supplied to ADC
ADC_RESOLUTION = 4095  # For a 12-bit ADC

ir_l = ADC(Pin(25)) 
ir_l.width(ADC.WIDTH_12BIT)
ir_l.atten(ADC.ATTN_11DB)
ir_f = ADC(Pin(0)) 
ir_f.width(ADC.WIDTH_12BIT)
ir_f.atten(ADC.ATTN_11DB)
ir_r = ADC(Pin(4)) 
ir_r.width(ADC.WIDTH_12BIT)
ir_r.atten(ADC.ATTN_11DB)


def read_distance(ir):
    adc_value = ir.read()
    voltage = (adc_value / ADC_RESOLUTION) * VOLTAGE_SUPPLY
    if voltage == 0:
        return float('inf')  # Avoid division by zero, return 'infinity' if no reading
    distance = 27.86 * (voltage ** -1.15)  # Example formula, might need calibration for accuracy
    return distance
def sensor_read():
    return [read_distance(ir_l),read_distance(ir_f),read_distance(ir_r),mpl.altitude(),mpl.temperature()]


while True:
    print(sensor_read())
    time.sleep(0.1)  # Delay for 1 second before next read
