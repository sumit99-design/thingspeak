import psutil
import paho.mqtt.publish as publish
import time

CHANNEL = "3503222"
HOST = "mqtt3.thingspeak.com"

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    payload = f"field1={cpu}&field2={ram}"

    publish.single(
        "channels/" + CHANNEL + "/publish",
        payload,
        hostname=HOST,
        transport="websockets",
        port=80,
        client_id="YOUR_CLIENT_ID",
        auth={
            "username": "YOUR_USERNAME",
            "password": "YOUR_PASSWORD"
        }
    )

    print("CPU:", cpu, "RAM:", ram)
    time.sleep(20)
