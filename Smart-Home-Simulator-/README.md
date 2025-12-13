# 🏠 Smart Home Simulator 🔦 | Powered by Python OOP + Flask + IoT

Welcome to the **Smart Home Simulator** — a creative and fully functional IoT-based project where your **smartphone** acts as a **Smart Flashlight** (Light Device), and your **laptop** acts as the **Controller**! Built entirely using **Python**, **Flask**, and **Object-Oriented Programming (OOP)** concepts. No extra hardware required! 💻📱

**Course:** Object-Oriented Programming (OOP)
**Semester:** 2rd  
**Submitted To:** Prof. Khalid Mehmood Khan
**Submitted By:**  
-  *Moavia Amir* (2k24_BSAI_72)  
-  *Muhammad Dawood* (2k24_BSAI_48) 
---
[![Watch Demo](thumbnail.jpg)](https://www.linkedin.com/posts/contactmuawia_python-oop-iot-activity-7317201126267777024-MT_F?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE83puMB2usKBg0a3tbcCz_4_33IjoRwOfw)
## 💡 Project Highlights

- ✅ Fully **Object-Oriented** Python structure
- ✅ Real-time **client-server communication** via HTTP
- ✅ Turns ON/OFF simulated Smart Flashlight remotely
- ✅ Uses only a **laptop & phone** to simulate real-world IoT
- ✅ Manual IP input = 🔌 easily connect to any smart device on same network
- ✅ Bonus: 🔁 Blink effect included!
- ✅ Future-ready: Easily expandable to other smart home devices

---

## ⚙️ Technologies Used

- 🐍 Python 3
- 🌐 Flask (REST API)
- 📡 Wi-Fi LAN (Local Network Communication)
- 🧠 Object-Oriented Programming (OOP)
- 📱 Termux (on Android for server)

---

## 🧱 Project Structure

```
smart-home-simulator/
│
├── controller.py        # 💻 Laptop - sends commands to the smart light
├── smart_light_server.py  # 📱 Phone - handles light states via Flask
├── README.md            # 📘 You're here!
```
# 🚀 How It Works
Think of this like a real-world smart home controller, but using basic devices and Python logic.

## 🔁 Communication Flow:
Run smart_light_server.py on your friend’s phone (Android + Termux + Flask)

Run controller.py on your laptop

Enter the phone’s IP address in your controller

Control light via options:

 1️⃣ Flash ON

 2️⃣ Flash OFF

 3️⃣ Blink

Flash is simulated as a virtual smart light using OOP

# 🔧 Setup Instructions
## 📱 On Phone (Server):
1. Install Termux from F-Droid

2. Run these commands in Termux:
``` 
pkg update
pkg install python
pip install flask termux-api
termux-setup-storage
```
3. Run the smart light server:
``` 
python smart_light_server.py
```
# 💻 On Laptop (Client):
1. Install Flask & Requests:
```
pip install flask requests
```
2. Run the controller:
```
python controller.py
```
3. Enter IP of the phone when prompted

# 🎮 Sample Controller Menu
```
Select the action:
1. Flash ON
2. Flash OFF
3. Blink
4. Exit
```
# 👨‍💻 Code Sample (Flashlight Class)
```python
class SmartFlashlight:
    def __init__(self):
        self.state = "off"

    def turn_on(self):
        self.state = "on"
        return "Smart Flashlight is ON"

    def turn_off(self):
        self.state = "off"
        return "Smart Flashlight is OFF"

    def get_state(self):
        return self.state
```
# 🛠️ Future Improvements
- 📡 Auto IP detection & device scanning

- 📱 Mobile-friendly web GUI

- 📲 Integrate with real flashlight or LED (via GPIO/Arduino)

- 📈 Analytics & dashboard for smart home actions

- 🌍 Control multiple devices (Fan, AC, etc.)

# 🧠 What We Learned
- Real-world implementation of OOP in Python

- Building REST APIs with Flask

- Local network-based IoT simulation

- Client-server architecture

- Collaboration and modular design in code

# 🙋 Author
👨‍💻 Muawiya — <a href="https://www.youtube.com/@Coding_Moves" target="_blank">@Coding_Moves</a>

# 🌟 Show Your Support
If you found this project inspiring:

+ ⭐ Star this repo

+ 📢 Share with friends

+ 📽️ Watch the video demo on YouTube

+ 🔗 Post it on LinkedIn with us!









