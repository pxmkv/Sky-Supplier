from machine import ADC, Pin
import time

# Constants for distance calculations
VOLTAGE_SUPPLY = 3.3  # Voltage supplied to ADC
ADC_RESOLUTION = 4095  # For a 12-bit ADC

# Create ADC object on the appropriate pin (adjust 'Pin' number according to your setup)
adc = ADC(Pin(25))  # Example uses GPIO 36, adjust as needed
adc.width(ADC.WIDTH_12BIT)
adc.atten(ADC.ATTN_11DB)

def read_distance():
    # Read ADC value
    adc_value = adc.read()
    # Convert ADC value to voltage
    voltage = (adc_value / ADC_RESOLUTION) * VOLTAGE_SUPPLY
    # Convert voltage to distance (using a calibration curve or a derived formula)
    if voltage == 0:
        return float('inf')  # Avoid division by zero, return 'infinity' if no reading
    distance = 27.86 * (voltage ** -1.15)  # Example formula, might need calibration for accuracy
    return distance

while True:
    distance = read_distance()
    print(f"Distance: {distance:.2f} cm")
    time.sleep(0.1)  # Delay for 1 second before next read
