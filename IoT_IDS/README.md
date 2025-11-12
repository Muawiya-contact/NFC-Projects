# IoT Intrusion Detection System (Information Security Project)

**Course:** Information Security / Network Security  
**Semester:** 3rd 
**Submitted To:** Prof. Khalid Mehmood Khan  
**Submitted By:**

- 🧠 _Moavia Amir_ (2k24_BSAI_72) — [📧 contactmuawia@gmail.com](mailto:contactmuawia@gmail.com)
- ⚙️ _Muhammad Ramzam_ (2k24_BSAI_31) — [📧 Ramzam@gmail.com](mailto:Ramzam@gmail.com)

---

## 📘 Project Overview

**IoT Intrusion Detection System** is a lightweight, classroom‑safe IDS that monitors MQTT traffic from ESP8266/NodeMCU sensors, detects anomalous behaviours (message‑rate floods, large‑payload floods, and tampering), and displays real‑time alerts on a local dashboard. The project demonstrates practical information security techniques for protecting IoT deployments and is intended for educational demonstration on owned devices and isolated networks.

---

## 🔍 Problem Statement

IoT devices are often resource‑constrained and poorly secured, making them vulnerable to message floods, tampering, and spoofing. These attacks can degrade service availability, corrupt telemetry, and open attack surfaces in smart systems. This project demonstrates how a simple IDS can detect such conditions and help preserve **integrity** and **availability** of IoT systems.

---

## 🎯 Objectives

- Build a reproducible IDS that monitors MQTT topics from ESP sensors.
- Detect two core attack types:
  1. **Message‑rate flood** — many small messages per second.
  2. **Byte‑rate flood** — large payloads causing bandwidth spikes.
- Demonstrate tampering/spoofing and an optional proxy (MITM) simulation.
- Provide a minimal web UI showing live sensor data and alert status.
- Ensure the demo is safe and limited to owned/isolated networks.

---

## 🧠 System Overview

| Component             | Purpose                                                     |
| --------------------- | ----------------------------------------------------------- |
| **ESP8266 / NodeMCU** | Sensor (publishes temperature) and optional attacker device |
| **Laptop**            | Runs Mosquitto MQTT broker, IDS (Python), and Flask web UI  |
| **Phone**             | Optional attacker (MQTT app or Termux) to simulate attacks  |
| **Software stack**    | Mosquitto, Python (paho-mqtt, Flask), Arduino IDE           |

---

## 🔬 Working Principle (Simple)

1. ESP sensor publishes JSON messages to `home/sensor/temp` at 1 msg/sec.
2. Laptop (broker + IDS) subscribes to `home/sensor/#` and measures:
   - messages/sec per topic (msg_rate)
   - bytes/sec per topic (byte_rate)
3. If `msg_rate` or `byte_rate` exceeds set thresholds → IDS raises an **ALERT** and the web UI shows a red warning.
4. Attacks are simulated safely using a second ESP or a phone (MQTT app / Termux).

---

## 🛠 Hardware & Software Requirements

**Hardware**

- ESP8266 / NodeMCU (sensor)
- Optional second ESP (attacker) or smartphone
- Laptop with Wi‑Fi and USB port

**Software**

- Mosquitto MQTT broker
- Python 3.8+ with `paho-mqtt` and `Flask`
- Arduino IDE (for flashing ESP)
- (Optional) Termux or MQTT mobile app

---

## 🚀 Quick Start (classroom demo)

1. Install and start Mosquitto on laptop.
2. Upload `esp_sensor.ino` to an ESP and set `BROKER_IP` to your laptop IP.
3. Run `python3 ids_web.py` on laptop (default thresholds: `MSG_THRESHOLD=30 msg/s`, `BYTES_THRESHOLD=4000 B/s`).
4. Open the UI: `http://<laptop-ip>:5000` — confirm **OK** status.
5. Simulate attacks:
   - **Message‑rate flood:** start phone/ESP attacker with interval `50 ms` → IDS triggers message‑rate alert.
   - **Byte‑rate flood:** phone (Termux) publishes ~900B every `200 ms` → IDS triggers byte‑rate alert.
6. Stop attacker → status returns to OK.

> **Safety:** Only run tests on your own devices and local network. Do not run attacks on external or institutional networks.

---

## 📂 Folder Structure

```
IoT_IDS/
├─ README.md # (this file)
├─ requirements.txt # paho-mqtt, Flask
├─ esp/
│ ├─ esp_sensor.ino
│ └─ esp_attacker.ino
├─ python/
│ ├─ ids_web.py
│ ├─ phone_attacker.py
│ └─ mqtt_proxy.py
└─ slides/
└─ one_slide.txt
```

---

## 🔧 Tuning & Extensions

- Adjust `MSG_THRESHOLD` and `BYTES_THRESHOLD` in `ids_web.py` to match your classroom network.
- Possible extensions: add rate‑limiting actions (block/quarantine), store alerts to CSV for the report, integrate cloud dashboards (ThingSpeak/Blynk), or add authentication and TLS for MQTT.

---

## 🧾 Deliverables & Evaluation Evidence

- Live demo (2–3 minutes): normal → message flood → large‑payload flood → tamper/proxy.
- Source code: ESP sketches + Python scripts in the repo.
- Report / screenshots showing alert and logs.

---

## 📫 Contact

- Moavia Amir — contactmuawia@gmail.com
- Muhammad Ramzam — Ramzam@gmail.com

---
