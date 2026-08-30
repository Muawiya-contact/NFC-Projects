# IoT Intrusion Detection System

A lightweight, classroom-safe intrusion detection system for IoT networks. An ESP8266/NodeMCU sensor publishes temperature readings over MQTT, and a Python IDS running alongside a Mosquitto broker watches the traffic for anomalies — message-rate floods, large-payload (byte-rate) floods, and tampering — raising real-time alerts on a local Flask dashboard. Built as an Information Security course project to demonstrate how a simple IDS helps preserve the integrity and availability of resource-constrained IoT deployments. This repository currently contains the project proposal (`IoT_IDS-Proposal.pdf`); see it for the full design.

## How it works

1. The ESP sensor publishes JSON messages to `home/sensor/temp` about once per second.
2. A laptop runs the Mosquitto broker and the IDS, which subscribes to `home/sensor/#` and tracks messages/sec and bytes/sec per topic.
3. When either rate exceeds its threshold (defaults: 30 msg/s, 4000 B/s), the IDS raises an alert and the web UI at `http://<laptop-ip>:5000` turns red.
4. Attacks are simulated with a second ESP or a phone (MQTT app or Termux): a ~50 ms publish interval triggers the message-rate alert; ~900 B payloads every 200 ms trigger the byte-rate alert. Stopping the attacker returns the status to OK. A proxy (MITM) simulation demonstrates tampering.

## Requirements

- ESP8266 / NodeMCU (sensor), plus an optional second ESP or smartphone as the attacker
- Laptop with Wi-Fi: Mosquitto MQTT broker, Python 3.8+ with `paho-mqtt` and `Flask`
- Arduino IDE for flashing the ESP

## Running the demo

1. Install and start Mosquitto on the laptop.
2. Flash the sensor sketch to the ESP with `BROKER_IP` set to the laptop's IP.
3. Start the IDS/web script with Python 3 and open `http://<laptop-ip>:5000`.
4. Run the flood simulations from the second device and watch the alerts fire.

Thresholds can be tuned to match the local network. Only run the attack simulations on your own devices and an isolated network — never on external or institutional networks.

## Credits

Course: Information Security / Network Security, 3rd semester
Instructor: Prof. Khalid Mehmood Khan

Team:
- Moavia Amir (2k24_BSAI_72) — contactmuawia@gmail.com
- Muhammad Ramzam (2k24_BSAI_31) — ramzan381.biz@gmail.com
