# ⚙️ ResQTemp — Smart Temperature & Rescue Alert System  

**Course:** Computer Organization & Assembly Language (COAL)  
**Semester:** 3rd  
**Submitted To:** Prof. Ghulam Mustafa  
**Submitted By:**  
- 🧠 *Moavia Amir* (2k24_BSAI_72) — [📧 contactmuawia@gmail.com](mailto:contactmuawia@gmail.com)  
- ⚙️ *Muhammad Dawood* (2k24_BSAI_31) — [📧 muhammaddawood@vu.edu.pk](mailto:muhammad.dawood@vu.edu.pk)

---

## 📘 Project Overview  

**ResQTemp** is a microcontroller-based **smart temperature control and rescue alert system** integrating **Assembly-level programming** with **IoT and GSM communication**.  
It demonstrates how **low-level hardware control** (in Assembly) can synchronize with **modern IoT automation** to enhance safety and real-time monitoring.

The project monitors temperature using an **LM35 sensor**, controls **fan and LED** responses, and triggers **rescue alerts via SMS and IoT dashboard** after a safety delay if overheating persists.  
Through an **ESP8266 web interface**, users can remotely view temperature data, device status, and location-based alerts in emergency mode.

---

## 🧩 Problem Statement  

Conventional temperature monitoring systems lack **intelligent decision logic** and **remote visibility**.  
In industrial or laboratory environments, a delayed response to overheating can lead to serious equipment or safety issues.  

**ResQTemp** bridges this gap by merging:  
- **Precision hardware control** (Assembly-level logic)  
- **Smart IoT connectivity**  
- **Real-time rescue response** via automated SMS and web alerts  

---

## 🎯 Objectives  

- Implement a temperature monitoring system using Assembly language on Arduino.  
- Activate safety outputs (LED/Fan) when temperature crosses threshold.  
- Introduce a 15-second delay before triggering emergency mode (avoiding false alerts).  
- Send a **rescue SMS using SIM900A** and update IoT dashboard via ESP8266 after the delay.  
- Display live readings and system status on a hosted IoT web page.  
- Optionally share GPS/location data for emergency tracking.  

---

## 🧠 System Overview  

| Component Type | Description |
|----------------|-------------|
| **Microcontroller** | Arduino UNO programmed in Assembly (COAL core) |
| **Sensor** | LM35 – Temperature sensor (analog input) |
| **Outputs** | LED indicator, Cooling Fan, Buzzer |
| **IoT Module** | ESP8266 Wi-Fi Module |
| **GSM Module** | SIM900A — sends rescue SMS automatically |
| **Web Page** | HTML + CSS dashboard showing live data & alerts |
| **Language Stack** | Assembly (Arduino), C++ (IoT & GSM logic), HTML/CSS (Web UI) |

---

## 🔬 Working Principle  

1. The **LM35 sensor** outputs an analog voltage proportional to temperature.  
2. Arduino executes **Assembly instructions** to:
   - Compare current temperature with threshold  
   - Control fan/LED indicators  
   - Start a **15-second timer** if overheating continues  
3. If temperature remains high after 15 seconds:
   - Arduino signals the **ESP8266** to update IoT dashboard  
   - Arduino triggers the **SIM900A module** to send a **rescue SMS** to predefined numbers  
4. The ESP8266 dashboard displays:
   - Current temperature  
   - System status: *Normal / Overheat / Rescue Mode*  
5. Users can monitor and control the system remotely via the IoT dashboard while receiving immediate SMS alerts.  

---

## 🧰 Hardware Requirements  

- Arduino UNO  
- LM35 Temperature Sensor  
- ESP8266 Wi-Fi Module  
- SIM900A GSM Module  
- LED, Fan, Buzzer  
- Breadboard, Jumper Wires, Resistors  
- Power Supply (5V)

---

## 💻 Software Requirements  

- Arduino IDE  
- Assembly/C++ Compiler Support  
- HTML + CSS for Web Dashboard  
- Serial Monitor or Web Browser for live data  

---

## 🚀 Expected Outcomes  

- Fully functional hardware prototype controlling temperature automatically.  
- Real-time monitoring via IoT dashboard hosted on ESP8266.  
- Automated **rescue SMS alerts** via SIM900A module.  
- Demonstration of Assembly-level timing and control accuracy.  
- Proof of concept for combining **COAL + IoT + GSM** principles.  

---

## 🔮 Future Enhancements  

- Add ultrasonic sensor for object detection.  
- Integrate camera module for live streaming.  
- Build a mobile app for remote monitoring.  
- Connect to platforms like **ThingSpeak** or **Blynk** for cloud storage.  

---

## 🧾 Folder Structure  

```txt
COAL-ResQTemp/
│
├── assembly/
│   └── main.asm
│
├── esp_web/
│   ├── index.html
│   └── style.css
│
├── circuits/
│   └── circuit_diagram.png
│
├── RQT-Proposal.pdf
├── RQT-Report.pdf
└── README.md  ← (this file)
```
## 🧩 Learning Impact

This project combines ***Computer Organization & Assembly Language*** concepts with ***IoT-based automation + GSM automation***, demonstrating:

+ Real-world integration of low-level control and networked intelligence

+ Strong understanding of hardware-software interfacing

+ Application of COAL principles in modern embedded systems

## 🏁 Conclusion

***ResQTemp*** showcases the power of **combining Assembly programming** precision with **IoT and GSM innovation**.
It reflects the **NFC IET vision** — merging faith, innovation, and engineering excellence to create impactful, **intelligent systems**.

## 📫 Contact  

For collaboration or guidance, connect via:  

- [🌐 GitHub Profile](https://github.com/Muawiya-contact)  
- [🎥 YouTube Channel — Coding Moves](https://www.youtube.com/@Coding_Moves)
- [📧 Email](mailto:contactmuawia@gmail.com)

---