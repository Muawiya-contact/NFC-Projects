# Smart Home Simulator

A small IoT demo built with Python, Flask, and OOP. An Android phone acts as a
smart light: a Flask server running in Termux exposes a `/flash` endpoint and
toggles the phone's actual torch through `termux-torch`. A laptop acts as the
controller, sending HTTP POST requests over the local Wi-Fi network to turn the
light on, off, or make it blink. No extra hardware is needed.

[Video demo on LinkedIn](https://www.linkedin.com/posts/contactmuawia_python-oop-iot-activity-7317201126267777024-MT_F?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE83puMB2usKBg0a3tbcCz_4_33IjoRwOfw)

## How it works

- `smart_light_server.py` runs on the phone. A `SmartFlashlight` class holds
  the light state and calls `termux-torch on/off`; a `FlashController` class
  maps incoming actions to it. Flask serves `POST /flash` on port 5000 and
  returns the resulting state as JSON.
- `controller.py` runs on the laptop. It asks for the phone's IP address, then
  shows a menu (Flash ON, Flash OFF, Blink, Exit) and sends the corresponding
  `{"action": "on"|"off"}` requests. Blink alternates on/off with a short delay.

Both devices must be on the same network.

## Files

```
controller.py           # laptop client with the menu
smart_light_server.py   # phone-side Flask server (Termux)
```

## Running it

On the phone (server), install Termux from F-Droid, then:

```
pkg update
pkg install python
pip install flask termux-api
termux-setup-storage
python smart_light_server.py
```

On the laptop (client):

```
pip install flask requests
python controller.py
```

Enter the phone's IP address when prompted, then pick an action from the menu.

## Credits

Course: Object-Oriented Programming (OOP), 2nd semester
Submitted to: Prof. Khalid Mehmood Khan
Submitted by: Moavia Amir (2k24_BSAI_72) and Muhammad Dawood (2k24_BSAI_48)

Author: Muawiya — [Coding_Moves on YouTube](https://www.youtube.com/@Coding_Moves)
