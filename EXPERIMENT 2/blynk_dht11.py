import BlynkLib
import board
import adafruit_dht
import time

# --- BLYNK CONFIGURATION ---
# Replace with your actual Auth Token from Blynk Device Info
BLYNK_AUTH = '0aQ7ypo4j-OCPek4-fwQ7Phq1Wxxxxxx'

# Force connection to the new Blynk IoT Cloud
blynk = BlynkLib.Blynk(BLYNK_AUTH, server='blynk.cloud', port=80)

# --- SENSOR CONFIGURATION ---
# DHT11 connected to GPIO 4 (Physical Pin 7)
sensor = adafruit_dht.DHT11(board.D4)

print("Starting Blynk DHT11 Monitoring on Pi 5...")

def send_sensor_data():
    try:
        # Read values from sensor
        temp = sensor.temperature
        humi = sensor.humidity

        if humi is not None and temp is not None:
            # Print to local console for debugging
            print(f"Blynk Update -> Temp: {temp:.1f}°C | Hum: {humi:.1f}%")

            # Send to Blynk Virtual Pins (V0 for Temp, V1 for Hum)
            blynk.virtual_write(0, temp)
            blynk.virtual_write(1, humi)
        else:
            print("Sensor returned null reading...")

    except RuntimeError as error:
        # DHT timing errors are common on Pi 5; we catch and continue
        pass

    except Exception as error:
        sensor.exit()
        raise error


# Main Loop
last_send_time = 0

while True:
    blynk.run()

    # Send data every 5 seconds to avoid flooding the Blynk server
    current_time = time.time()

    if current_time - last_send_time > 5.0:
        send_sensor_data()
        last_send_time = current_time
